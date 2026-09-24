import datetime
import hashlib
import random
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from backend.app.models.otp import OTPVerification
from backend.app.models.user import User
from backend.app.services.smtp_service import SMTPService


class OTPService:
    @staticmethod
    def send_otp(db: Session, email: str) -> dict:
        email = email.strip().lower()
        if not email or "@" not in email or "." not in email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid email format. Please provide a valid email address.",
            )

        # Check if user already exists
        existing_user = db.query(User).filter(User.email == email).first()
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email address is already registered. Please sign in instead.",
            )

        # Check cooldown (60 seconds)
        now = datetime.datetime.utcnow()
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

        # Generate strictly 6-digit random OTP
        otp_code = str(random.randint(100000, 999999))
        otp_hash = hashlib.sha256(otp_code.encode("utf-8")).hexdigest()
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

        # Send via Gmail SMTP (Never log or expose the OTP in response!)
        success, message = SMTPService.send_otp_email(email, otp_code)

        return {
            "message": "Verification OTP sent to your email.",
            "email": email,
            "expires_in_seconds": 300,
        }

    @staticmethod
    def verify_otp(db: Session, email: str, otp_code: str) -> dict:
        email = email.strip().lower()
        otp_code = otp_code.strip()

        if not email or not otp_code:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email and OTP code are required.",
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

        if record.is_verified:
            return {"message": "Email verified successfully.", "email": email}

        now = datetime.datetime.utcnow()
        if now > record.expires_at:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="OTP expired. Please request a new OTP.",
            )

        if record.attempt_count >= 5:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Too many incorrect attempts. Please request a new OTP.",
            )

        input_hash = hashlib.sha256(otp_code.encode("utf-8")).hexdigest()

        if input_hash != record.otp_hash:
            record.attempt_count += 1
            db.commit()
            if record.attempt_count >= 5:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Too many incorrect attempts. Please request a new OTP.",
                )
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid OTP. Please try again.",
            )

        # Verification Success -> Mark verified
        record.is_verified = True
        db.commit()

        return {"message": "Email verified successfully.", "email": email}
