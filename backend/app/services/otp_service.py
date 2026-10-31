import datetime
import hashlib
import re
import secrets
from typing import Optional
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from backend.app.config import settings
from backend.app.models.otp import OTPVerification
from backend.app.models.user import User
from backend.app.services.smtp_service import SMTPService


EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")


def _hash_otp(email: str, otp_code: str) -> str:
    """Generate salted SHA-256 hash using JWT_SECRET and email."""
    salt = settings.JWT_SECRET
    return hashlib.sha256(f"{salt}:{email.lower()}:{otp_code}".encode("utf-8")).hexdigest()


class OTPService:
    @staticmethod
    def send_otp(db: Session, email: str) -> dict:
        email = email.strip().lower()
        if not email or not EMAIL_REGEX.match(email):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid email format. Please provide a valid email address.",
            )

        # 1. Prevent registration if user already exists
        existing_user = db.query(User).filter(User.email == email).first()
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email address is already registered. Please sign in instead.",
            )

        now = datetime.datetime.utcnow()

        # 2. Rate limiting: Hourly request cap (maximum 5 OTP requests per hour per email)
        one_hour_ago = now - datetime.timedelta(hours=1)
        hourly_count = (
            db.query(OTPVerification)
            .filter(
                OTPVerification.email == email,
                OTPVerification.created_at >= one_hour_ago,
            )
            .count()
        )
        if hourly_count >= 5:
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="Too many OTP requests for this email address. Please try again in 1 hour.",
            )

        # 3. Resend Cooldown (60 seconds)
        existing_otp = (
            db.query(OTPVerification)
            .filter(OTPVerification.email == email)
            .order_by(OTPVerification.created_at.desc())
            .first()
        )

        if existing_otp:
            last_time = existing_otp.last_resend_at or existing_otp.created_at
            seconds_since = (now - last_time).total_seconds()
            if seconds_since < 60:
                wait_seconds = int(60 - seconds_since)
                raise HTTPException(
                    status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                    detail=f"Please wait {wait_seconds} seconds before requesting a new OTP.",
                )

        # 4. Generate cryptographically secure 6-digit OTP (range 100000 - 999999)
        otp_code = f"{secrets.randbelow(900000) + 100000:06d}"
        otp_hash = _hash_otp(email, otp_code)
        expires_at = now + datetime.timedelta(minutes=5)

        if existing_otp:
            existing_otp.otp_hash = otp_hash
            existing_otp.expires_at = expires_at
            existing_otp.attempt_count = 0
            existing_otp.is_verified = False
            existing_otp.last_resend_at = now
            existing_otp.created_at = now
        else:
            otp_record = OTPVerification(
                email=email,
                otp_hash=otp_hash,
                expires_at=expires_at,
                attempt_count=0,
                is_verified=False,
                last_resend_at=now,
                created_at=now,
            )
            db.add(otp_record)

        db.commit()

        # 5. Dispatch via Gmail SMTP (port 587 STARTTLS)
        success, message = SMTPService.send_otp_email(email, otp_code)

        if not success:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to deliver verification code to {email}. {message}",
            )

        # Security: NEVER return the plain OTP in response
        return {
            "message": f"Verification code successfully sent to {email}. Please check your Gmail inbox and enter the 6-digit code.",
            "email": email,
            "expires_in_seconds": 300,
            "delivery_success": True,
        }

    @staticmethod
    def verify_otp(db: Session, email: str, otp_code: str) -> dict:
        email = email.strip().lower()
        otp_code = str(otp_code).strip()

        if not email or not otp_code or len(otp_code) != 6 or not otp_code.isdigit():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Please provide a valid 6-digit verification code.",
            )

        record = (
            db.query(OTPVerification)
            .filter(OTPVerification.email == email)
            .order_by(OTPVerification.created_at.desc())
            .first()
        )

        if not record:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No OTP request found for this email address. Please request a new OTP.",
            )

        # Prevent OTP reuse
        if record.is_verified:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="This verification code has already been used. Please request a new OTP.",
            )

        # Prevent brute force: Maximum 5 attempts
        if record.attempt_count >= 5:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Too many incorrect attempts. This OTP has been invalidated. Please request a new OTP.",
            )

        now = datetime.datetime.utcnow()

        # Check expiration (5 minutes)
        if now > record.expires_at:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="OTP expired. Please request a new OTP.",
            )

        input_hash = _hash_otp(email, otp_code)

        # Constant-time comparison to prevent timing attacks
        if not secrets.compare_digest(input_hash, record.otp_hash):
            record.attempt_count += 1
            if record.attempt_count >= 5:
                # Invalidate immediately
                record.expires_at = now
            db.commit()

            if record.attempt_count >= 5:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Too many incorrect attempts. This OTP has been invalidated. Please request a new OTP.",
                )

            remaining = 5 - record.attempt_count
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid verification code. You have {remaining} attempt(s) remaining.",
            )

        # Verification Success -> Mark verified
        record.is_verified = True
        db.commit()

        return {"message": "Email verified successfully.", "email": email}

    @staticmethod
    def consume_verified_otp(db: Session, email: str) -> bool:
        """
        Verify that email was verified via OTP and consume it to prevent reuse.
        Returns True if a valid verified OTP existed and was consumed.
        """
        email = email.strip().lower()
        now = datetime.datetime.utcnow()

        record = (
            db.query(OTPVerification)
            .filter(
                OTPVerification.email == email,
                OTPVerification.is_verified == True,
            )
            .order_by(OTPVerification.created_at.desc())
            .first()
        )

        if not record:
            return False

        # Must be within 15 minutes of verification
        seconds_since = (now - record.created_at).total_seconds()
        if seconds_since > 900:  # 15 minutes
            db.delete(record)
            db.commit()
            return False

        # Consume the verified OTP record so it can NEVER be reused
        db.delete(record)
        db.commit()
        return True
