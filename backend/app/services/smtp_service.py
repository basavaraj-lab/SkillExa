import os
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from backend.app.config import settings


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
            print(f"\n=======================================================")
            print(f"🔒 [SKILLEXA VERIFICATION CODE - NO SMTP CONFIGURED]")
            print(f"To: {to_email}")
            print(f"6-Digit Verification Code: {otp_code}")
            print(f"Notice: Set SMTP_USERNAME & SMTP_PASSWORD in backend/.env to send directly to Gmail.")
            print(f"=======================================================\n")
            return False, "SMTP credentials missing. Please set SMTP_USERNAME & SMTP_PASSWORD in backend/.env."

        # Attempt 1: Port 587 STARTTLS
        sent = False
        last_error = ""
        try:
            context = ssl.create_default_context()
            with smtplib.SMTP(smtp_host, smtp_port, timeout=10) as server:
                server.ehlo()
                server.starttls(context=context)
                server.ehlo()
                server.login(smtp_username, smtp_password)
                server.send_message(msg)
                sent = True
        except (ssl.SSLCertVerificationError, ssl.SSLError):
            try:
                context = ssl._create_unverified_context()
                with smtplib.SMTP(smtp_host, smtp_port, timeout=10) as server:
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

        # Attempt 2: Port 465 SSL fallback if port 587 failed
        if not sent:
            try:
                context = ssl._create_unverified_context()
                with smtplib.SMTP_SSL(smtp_host, 465, context=context, timeout=10) as server:
                    server.login(smtp_username, smtp_password)
                    server.send_message(msg)
                    sent = True
            except Exception as e3:
                last_error = str(e3)

        if sent:
            print(f"\n=======================================================")
            print(f"✉️ [GMAIL SMTP SUCCESS] OTP delivered to {to_email}")
            print(f"Verification Code: {otp_code}")
            print(f"=======================================================\n")
            return True, f"Verification OTP email delivered to {to_email} via Gmail SMTP."
        else:
            print(f"\n=======================================================")
            print(f"⚠️ [GMAIL SMTP FAILED] Could not deliver to {to_email}")
            print(f"Error: {last_error}")
            print(f"👉 6-Digit Verification Code for testing: {otp_code}")
            print(f"Notice: Generate a new 16-char App Password at https://myaccount.google.com/apppasswords and update backend/.env")
            print(f"=======================================================\n")
            return False, f"Gmail SMTP rejected credentials ({last_error}). Check App Password in backend/.env."
