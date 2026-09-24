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
        smtp_username = settings.SMTP_USERNAME or os.getenv("SMTP_USERNAME", os.getenv("SMTP_USER", ""))
        smtp_password = settings.SMTP_PASSWORD or os.getenv("SMTP_PASSWORD", "")
        from_email = settings.SMTP_FROM_EMAIL or os.getenv("SMTP_FROM_EMAIL", smtp_username or "noreply@skillexa.com")

        subject = "SkillExa Account Verification OTP"

        body = f"""SkillExa Platform

YOUR 6-DIGIT VERIFICATION CODE

{otp_code}

This OTP is valid for 5 minutes.

Do not share this code with anyone.

If you did not request this verification, you can safely ignore this email.
"""

        msg = MIMEMultipart()
        msg["From"] = f"SkillExa Platform <{from_email}>"
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        if not smtp_username or not smtp_password:
            print(f"\n==========================================")
            print(f"[GMAIL SMTP DISPATCH LOG - PENDING SMTP CREDENTIALS]")
            print(f"To: {to_email}")
            print(f"Subject: {subject}")
            print(f"Body:\n{body}")
            print(f"Notice: Set SMTP_USERNAME & SMTP_PASSWORD in backend/.env to send directly to Gmail inboxes.")
            print(f"==========================================\n")
            return True, "OTP generated and logged to backend. Add SMTP credentials to backend/.env to deliver to Gmail."

        try:
            try:
                context = ssl.create_default_context()
                with smtplib.SMTP(smtp_host, smtp_port, timeout=15) as server:
                    server.starttls(context=context)
                    server.login(smtp_username, smtp_password)
                    server.send_message(msg)
            except (ssl.SSLCertVerificationError, ssl.SSLError):
                context = ssl._create_unverified_context()
                with smtplib.SMTP(smtp_host, smtp_port, timeout=15) as server:
                    server.starttls(context=context)
                    server.login(smtp_username, smtp_password)
                    server.send_message(msg)

            print(f"[GMAIL SMTP SUCCESS] Verification OTP email delivered to {to_email}")
            return True, f"Verification OTP email delivered to {to_email} via Gmail SMTP."
        except Exception as e:
            print(f"[GMAIL SMTP ERROR] Failed to send email to {to_email}: {e}")
            return False, f"SMTP delivery failed: {str(e)}"
