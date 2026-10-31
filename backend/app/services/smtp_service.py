import logging
import os
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from backend.app.config import settings

logger = logging.getLogger("skillexa.smtp")


class SMTPService:
    @staticmethod
    def send_otp_email(to_email: str, otp_code: str) -> tuple[bool, str]:
        """
        Sends custom 6-digit registration OTP via Gmail SMTP.
        Configured via environment variables / backend/.env:
        SMTP_HOST, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD, SMTP_FROM_EMAIL.
        """
        smtp_host = settings.SMTP_HOST or os.getenv("SMTP_HOST", "smtp.gmail.com")
        smtp_port = int(settings.SMTP_PORT or os.getenv("SMTP_PORT", "587"))
        smtp_username = (settings.SMTP_USERNAME or os.getenv("SMTP_USERNAME", os.getenv("SMTP_USER", ""))).strip()
        smtp_password = (settings.SMTP_PASSWORD or os.getenv("SMTP_PASSWORD", "")).strip().replace(" ", "")
        from_email = settings.SMTP_FROM_EMAIL or os.getenv("SMTP_FROM_EMAIL", smtp_username or "noreply@skillexa.com")

        subject = "SkillExa Account Verification Code"

        text_body = f"""SkillExa Platform
Educational & Placement Preparation

YOUR 6-DIGIT VERIFICATION CODE:
{otp_code}

This code is valid for 5 minutes.
Do not share this code with anyone.

If you did not request this verification, you can safely ignore this email.
"""

        html_body = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background-color: #F8FAFC; margin: 0; padding: 24px; }}
    .card {{ max-width: 500px; margin: 0 auto; background: #FFFFFF; border-radius: 16px; border: 1px solid #E2E8F0; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.06); }}
    .header {{ background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 100%); padding: 24px 20px; text-align: center; }}
    .header h1 {{ margin: 0; font-size: 24px; color: #FFFFFF; font-weight: 800; letter-spacing: -0.5px; }}
    .header p {{ margin: 4px 0 0 0; color: #93C5FD; font-size: 13px; }}
    .content {{ padding: 32px 24px; text-align: center; }}
    .title {{ font-size: 18px; font-weight: 700; color: #0F172A; margin: 0 0 8px 0; }}
    .subtitle {{ font-size: 14px; color: #64748B; margin: 0 0 24px 0; line-height: 1.5; }}
    .otp-container {{ background: #EEF2FF; border: 2px dashed #6366F1; border-radius: 12px; padding: 18px 24px; display: inline-block; margin: 0 auto 20px auto; }}
    .otp-code {{ font-size: 32px; font-weight: 800; letter-spacing: 8px; color: #312E81; font-family: 'Courier New', monospace; }}
    .expiry {{ font-size: 12px; color: #DC2626; font-weight: 600; margin-top: 6px; }}
    .warning {{ font-size: 12.5px; color: #64748B; line-height: 1.5; margin: 0 0 8px 0; }}
    .footer {{ background: #F8FAFC; border-top: 1px solid #E2E8F0; padding: 16px 20px; text-align: center; font-size: 11.5px; color: #94A3B8; }}
  </style>
</head>
<body>
  <div class="card">
    <div class="header">
      <h1>SkillExa</h1>
      <p>Educational & Placement Preparation Platform</p>
    </div>
    <div class="content">
      <h2 class="title">Verify Your Email Address</h2>
      <p class="subtitle">Use the 6-digit verification code below to complete your registration on SkillExa.</p>
      <div class="otp-container">
        <div class="otp-code">{otp_code}</div>
        <div class="expiry">Valid for 5 minutes</div>
      </div>
      <p class="warning">Do not share this verification code with anyone. SkillExa staff will never ask for your code.</p>
    </div>
    <div class="footer">
      &copy; 2026 SkillExa Platform. If you did not request this verification, you can safely ignore this email.
    </div>
  </div>
</body>
</html>
"""

        msg = MIMEMultipart("alternative")
        msg["From"] = f"SkillExa Platform <{from_email}>"
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(text_body, "plain"))
        msg.attach(MIMEText(html_body, "html"))

        if not smtp_username or not smtp_password:
            logger.warning(
                "SMTP credentials missing. Please set SMTP_USERNAME and SMTP_PASSWORD in backend/.env or Render environment variables."
            )
            return False, "SMTP credentials missing. Please set SMTP_USERNAME & SMTP_PASSWORD in backend/.env."

        # Attempt 1: Port 587 STARTTLS (Standard Gmail SMTP)
        sent = False
        last_error = ""
        try:
            context = ssl.create_default_context()
            with smtplib.SMTP(smtp_host, smtp_port, timeout=15) as server:
                server.ehlo()
                server.starttls(context=context)
                server.ehlo()
                server.login(smtp_username, smtp_password)
                server.send_message(msg)
                sent = True
        except smtplib.SMTPAuthenticationError as auth_err:
            last_error = "Gmail SMTP authentication failed. Please verify your Gmail App Password."
            logger.error("Gmail SMTP authentication failed for user %s: %s", smtp_username, auth_err)
        except smtplib.SMTPConnectError as conn_err:
            last_error = f"Cannot connect to SMTP server {smtp_host}:{smtp_port}."
            logger.error("Gmail SMTP connection failed: %s", conn_err)
        except (ssl.SSLCertVerificationError, ssl.SSLError):
            try:
                context = ssl._create_unverified_context()
                with smtplib.SMTP(smtp_host, smtp_port, timeout=15) as server:
                    server.ehlo()
                    server.starttls(context=context)
                    server.ehlo()
                    server.login(smtp_username, smtp_password)
                    server.send_message(msg)
                    sent = True
            except Exception as e2:
                last_error = str(e2)
                logger.error("Gmail SMTP unverified SSL attempt failed: %s", e2)
        except Exception as e:
            last_error = str(e)
            logger.error("Gmail SMTP error during STARTTLS: %s", e)

        # Attempt 2: Port 465 SSL fallback if port 587 failed and not auth rejection
        if not sent and "authentication failed" not in last_error.lower():
            try:
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL(smtp_host, 465, context=context, timeout=15) as server:
                    server.login(smtp_username, smtp_password)
                    server.send_message(msg)
                    sent = True
            except Exception as e3:
                last_error = str(e3)
                logger.error("Gmail SMTP SSL fallback failed: %s", e3)

        if sent:
            logger.info("Verification OTP email successfully delivered to %s via Gmail SMTP.", to_email)
            return True, f"Verification OTP email delivered to {to_email} via Gmail SMTP."
        else:
            logger.error("Failed to deliver verification code to %s: %s", to_email, last_error)
            return False, f"Gmail SMTP error: {last_error}"

    @staticmethod
    def send_announcement_email(
        to_email: str,
        student_name: str,
        faculty_name: str,
        college_name: str,
        department: str,
        title: str,
        content: str,
        priority: str = "NORMAL",
    ) -> tuple[bool, str]:
        """
        Sends an official College Announcement email to an enrolled student.
        """
        smtp_host = settings.SMTP_HOST or os.getenv("SMTP_HOST", "smtp.gmail.com")
        smtp_port = int(settings.SMTP_PORT or os.getenv("SMTP_PORT", "587"))
        smtp_username = (settings.SMTP_USERNAME or os.getenv("SMTP_USERNAME", os.getenv("SMTP_USER", ""))).strip()
        smtp_password = (settings.SMTP_PASSWORD or os.getenv("SMTP_PASSWORD", "")).strip().replace(" ", "")
        from_email = settings.SMTP_FROM_EMAIL or os.getenv("SMTP_FROM_EMAIL", smtp_username or "noreply@skillexa.com")

        priority_upper = (priority or "NORMAL").upper()
        priority_color = "#DC2626" if priority_upper == "URGENT" else ("#D97706" if priority_upper == "HIGH" else "#2563EB")
        priority_bg = "#FEF2F2" if priority_upper == "URGENT" else ("#FFFBEB" if priority_upper == "HIGH" else "#EFF6FF")

        subject = f"📢 [{priority_upper}] {title} — {college_name}"

        text_body = f"""SkillExa College Workspace
{college_name} • {department}

OFFICIAL DEPARTMENT ANNOUNCEMENT
--------------------------------------------------
Title: {title}
Priority: {priority_upper}
Published By: {faculty_name} ({department})

Message:
{content}

Log in to your SkillExa student portal to view active notices and academic resources:
http://localhost:8081/my-college
--------------------------------------------------
SkillExa College Notification System
"""

        html_body = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background-color: #F8FAFC; margin: 0; padding: 24px; }}
    .card {{ max-width: 560px; margin: 0 auto; background: #FFFFFF; border-radius: 16px; border: 1px solid #E2E8F0; overflow: hidden; box-shadow: 0 4px 16px rgba(0,0,0,0.06); }}
    .header {{ background: linear-gradient(135deg, #0F172A 0%, #1E3A8A 100%); padding: 24px 22px; color: #FFFFFF; }}
    .badge {{ display: inline-block; background: {priority_bg}; color: {priority_color}; border: 1px solid {priority_color}; font-size: 11px; font-weight: 800; padding: 3px 9px; border-radius: 999px; letter-spacing: 0.5px; margin-bottom: 8px; }}
    .clg-title {{ font-size: 18px; font-weight: 800; margin: 0; color: #FFFFFF; }}
    .clg-sub {{ font-size: 12.5px; color: #93C5FD; margin: 3px 0 0 0; }}
    .content {{ padding: 28px 24px; }}
    .greeting {{ font-size: 14px; color: #64748B; margin: 0 0 16px 0; }}
    .ann-title {{ font-size: 19px; font-weight: 800; color: #0F172A; margin: 0 0 12px 0; line-height: 1.35; }}
    .ann-box {{ background: #F8FAFC; border-left: 4px solid {priority_color}; border-radius: 8px; padding: 16px 18px; margin-bottom: 20px; }}
    .ann-text {{ font-size: 14px; color: #1E293B; line-height: 1.6; margin: 0; white-space: pre-wrap; }}
    .meta-row {{ border-top: 1px solid #E2E8F0; padding-top: 14px; margin-top: 20px; font-size: 12.5px; color: #64748B; }}
    .btn {{ display: inline-block; background: #2563EB; color: #FFFFFF !important; font-weight: 700; font-size: 13.5px; text-decoration: none; padding: 12px 24px; border-radius: 8px; margin-top: 8px; }}
    .footer {{ background: #F8FAFC; border-top: 1px solid #E2E8F0; padding: 16px 20px; text-align: center; font-size: 11.5px; color: #94A3B8; }}
  </style>
</head>
<body>
  <div class="card">
    <div class="header">
      <span class="badge">{priority_upper} NOTICE</span>
      <h1 class="clg-title">{college_name}</h1>
      <p class="clg-sub">{department} Department • SkillExa College Workspace</p>
    </div>
    <div class="content">
      <p class="greeting">Hello {student_name or 'Student'},</p>
      <h2 class="ann-title">{title}</h2>
      <div class="ann-box">
        <p class="ann-text">{content}</p>
      </div>
      <div class="meta-row">
        <strong>Published by:</strong> {faculty_name} ({department})<br/>
        <strong>Status:</strong> Active Official College Announcement
      </div>
      <p style="margin-top: 22px;">
        <a href="http://localhost:8081/my-college" class="btn">View in SkillExa Workspace &rarr;</a>
      </p>
    </div>
    <div class="footer">
      &copy; 2026 SkillExa Platform • You received this because you are an enrolled student at {college_name}.
    </div>
  </div>
</body>
</html>
"""

        msg = MIMEMultipart("alternative")
        msg["From"] = f"{college_name} <{from_email}>"
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(text_body, "plain"))
        msg.attach(MIMEText(html_body, "html"))

        if not smtp_username or not smtp_password:
            logger.warning("SMTP credentials not configured. College announcement not emailed.")
            return True, "Announcement email skipped (SMTP credentials not configured)."

        sent = False
        last_error = ""
        try:
            context = ssl.create_default_context()
            with smtplib.SMTP(smtp_host, smtp_port, timeout=15) as server:
                server.ehlo()
                server.starttls(context=context)
                server.ehlo()
                server.login(smtp_username, smtp_password)
                server.send_message(msg)
                sent = True
        except (ssl.SSLCertVerificationError, ssl.SSLError):
            try:
                context = ssl._create_unverified_context()
                with smtplib.SMTP(smtp_host, smtp_port, timeout=15) as server:
                    server.ehlo()
                    server.starttls(context=context)
                    server.ehlo()
                    server.login(smtp_username, smtp_password)
                    server.send_message(msg)
                    sent = True
            except Exception as e2:
                last_error = str(e2)
        except Exception as e:
            last_error = str(e)

        if not sent:
            try:
                context = ssl._create_unverified_context()
                with smtplib.SMTP_SSL(smtp_host, 465, context=context, timeout=15) as server:
                    server.login(smtp_username, smtp_password)
                    server.send_message(msg)
                    sent = True
            except Exception as e3:
                last_error = str(e3)

        if sent:
            logger.info("Announcement email successfully delivered to %s", to_email)
            return True, f"Announcement email delivered to {to_email} via SMTP."
        else:
            logger.error("Announcement email delivery failed to %s: %s", to_email, last_error)
            return False, f"SMTP delivery failed ({last_error})."
