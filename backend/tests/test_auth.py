import datetime
from unittest.mock import patch
import pytest
from sqlalchemy.orm import Session

from backend.app.config import settings
from backend.app.models.otp import OTPVerification
from backend.app.models.user import RoleEnum, User
from backend.app.services.otp_service import _hash_otp


def test_complete_otp_registration_flow(client, db_session: Session):
    """
    TASK 6 Tests:
    1. Register with new email & send OTP.
    2. Try incorrect OTP.
    3. Try expired OTP.
    4. Verify OTP with correct code.
    5. Try reusing verified OTP.
    6. Complete student registration.
    7. Try duplicate registration.
    """
    email = "newstudent@kvgce.edu.in"
    otp_code = "123456"

    # Mock SMTP to avoid sending actual email in rapid unit tests
    with patch("backend.app.services.smtp_service.SMTPService.send_otp_email", return_value=(True, "Delivered")):
        # 1. Send OTP
        send_res = client.post("/api/auth/send-otp", json={"email": email})
        assert send_res.status_code == 200
        assert send_res.json()["success"] is True
        assert "Verification code successfully sent" in send_res.json()["message"]
        # Verify OTP is NOT returned in response
        assert "otp" not in send_res.json().get("data", {})
        assert "otp_code" not in send_res.json().get("data", {})

    # Set known OTP hash in database for deterministic test verification
    otp_record = (
        db_session.query(OTPVerification)
        .filter(OTPVerification.email == email)
        .order_by(OTPVerification.created_at.desc())
        .first()
    )
    assert otp_record is not None
    otp_record.otp_hash = _hash_otp(email, otp_code)
    db_session.commit()

    # 2. Try an incorrect OTP (400 Bad Request)
    wrong_res = client.post("/api/auth/verify-otp", json={"email": email, "otp": "999999"})
    assert wrong_res.status_code == 400
    assert "Invalid verification code" in wrong_res.json()["detail"]

    # 3. Try an expired OTP
    otp_record.expires_at = datetime.datetime.utcnow() - datetime.timedelta(seconds=10)
    db_session.commit()
    expired_res = client.post("/api/auth/verify-otp", json={"email": email, "otp": otp_code})
    assert expired_res.status_code == 400
    assert "OTP expired" in expired_res.json()["detail"]

    # Reset expiration to valid future time
    otp_record.expires_at = datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
    db_session.commit()

    # 4. Enter correct OTP
    correct_res = client.post("/api/auth/verify-otp", json={"email": email, "otp": otp_code})
    assert correct_res.status_code == 200
    assert correct_res.json()["success"] is True
    assert correct_res.json()["data"]["email"] == email

    # 5. Try reusing verified OTP (Replay prevention)
    reused_res = client.post("/api/auth/verify-otp", json={"email": email, "otp": otp_code})
    assert reused_res.status_code == 400
    assert "already been used" in reused_res.json()["detail"]

    # 6. Complete student registration
    reg_res = client.post(
        "/api/auth/register/student",
        json={
            "name": "New Student",
            "email": email,
            "password": "SecurePassword123!",
            "branch": "ECE",
            "academic_year": "3rd Year",
            "section": "A",
            "target_exam": "Placement",
        },
    )
    assert reg_res.status_code == 201
    assert reg_res.json()["success"] is True
    assert reg_res.json()["data"]["email"] == email

    # 7. Try duplicate registration with same email -> 409 Conflict
    dup_res = client.post(
        "/api/auth/register/student",
        json={
            "name": "New Student Duplicate",
            "email": email,
            "password": "SecurePassword123!",
            "branch": "ECE",
            "academic_year": "3rd Year",
            "section": "A",
        },
    )
    assert dup_res.status_code == 409


def test_otp_resend_cooldown_and_rate_limiting(client, db_session: Session):
    """Test 60-second cooldown on OTP resend requests."""
    email = "cooldown.test@kvgce.edu.in"

    with patch("backend.app.services.smtp_service.SMTPService.send_otp_email", return_value=(True, "Delivered")):
        # Request 1: succeeds
        res1 = client.post("/api/auth/send-otp", json={"email": email})
        assert res1.status_code == 200

        # Request 2 (immediate): blocked by 60s cooldown -> 429 Too Many Requests
        res2 = client.post("/api/auth/send-otp", json={"email": email})
        assert res2.status_code == 429
        assert "Please wait" in res2.json()["detail"]


def test_otp_brute_force_protection(client, db_session: Session):
    """Test that 5 consecutive failed attempts invalidate the OTP."""
    email = "brute.force@kvgce.edu.in"
    otp_code = "654321"

    with patch("backend.app.services.smtp_service.SMTPService.send_otp_email", return_value=(True, "Delivered")):
        client.post("/api/auth/send-otp", json={"email": email})

    otp_record = (
        db_session.query(OTPVerification)
        .filter(OTPVerification.email == email)
        .order_by(OTPVerification.created_at.desc())
        .first()
    )
    otp_record.otp_hash = _hash_otp(email, otp_code)
    db_session.commit()

    # Attempts 1 to 4: invalid OTP
    for i in range(1, 5):
        res = client.post("/api/auth/verify-otp", json={"email": email, "otp": "000000"})
        assert res.status_code == 400
        assert "attempt(s) remaining" in res.json()["detail"]

    # Attempt 5: invalid OTP -> triggers invalidation
    res5 = client.post("/api/auth/verify-otp", json={"email": email, "otp": "000000"})
    assert res5.status_code == 400
    assert "Too many incorrect attempts" in res5.json()["detail"]

    # Even if correct OTP is provided on 6th attempt, it is rejected
    res6 = client.post("/api/auth/verify-otp", json={"email": email, "otp": otp_code})
    assert res6.status_code == 400
    assert "Too many incorrect attempts" in res6.json()["detail"]


def test_login_and_jwt_route_protection(client, db_session: Session):
    """
    TASK 6 Tests:
    - Log in with correct credentials
    - Log in with incorrect credentials
    - Access protected routes with valid and invalid JWT tokens
    """
    email = "registered.user@kvgce.edu.in"
    password = "CorrectPassword123!"

    # Create verified student user directly in DB
    from backend.app.utils.security import hash_password
    user = User(
        email=email,
        password_hash=hash_password(password),
        name="Registered Student",
        role=RoleEnum.STUDENT,
        is_active=True,
    )
    db_session.add(user)
    db_session.commit()

    # 1. Login with incorrect password -> 401 Unauthorized
    bad_login = client.post(
        "/api/auth/login",
        json={"email": email, "password": "WrongPassword!"},
    )
    assert bad_login.status_code == 401
    assert bad_login.json()["success"] is False

    # 2. Login with non-existent email -> 401 Unauthorized
    non_existent = client.post(
        "/api/auth/login",
        json={"email": "nobody@kvgce.edu.in", "password": password},
    )
    assert non_existent.status_code == 401

    # 3. Login with correct credentials -> 200 OK
    good_login = client.post(
        "/api/auth/login",
        json={"email": email, "password": password},
    )
    assert good_login.status_code == 200
    assert good_login.json()["success"] is True
    token_data = good_login.json()["data"]
    assert "access_token" in token_data
    access_token = token_data["access_token"]
    assert token_data["user"]["email"] == email

    # 4. Access protected route /api/auth/me with valid Bearer token -> 200 OK
    me_res = client.get(
        "/api/auth/me",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    assert me_res.status_code == 200
    assert me_res.json()["data"]["email"] == email

    # 5. Access protected route with invalid / forged token -> 401 Unauthorized
    invalid_token_res = client.get(
        "/api/auth/me",
        headers={"Authorization": "Bearer forged.invalid.jwt.token"},
    )
    assert invalid_token_res.status_code == 401

    # 6. Access protected route without token -> 401 Unauthorized
    no_token_res = client.get("/api/auth/me")
    assert no_token_res.status_code == 401

    # 7. Role-based protection: Student token cannot access faculty-only route -> 403 Forbidden
    fac_res = client.get(
        "/api/faculty/dashboard-stats",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    assert fac_res.status_code == 403


def test_faculty_otp_registration_and_login(client, db_session: Session):
    """Test faculty registration flow after OTP verification."""
    email = "prof.new@kvgce.edu.in"
    otp_code = "456789"

    with patch("backend.app.services.smtp_service.SMTPService.send_otp_email", return_value=(True, "Delivered")):
        client.post("/api/auth/send-otp", json={"email": email})

    otp_record = (
        db_session.query(OTPVerification)
        .filter(OTPVerification.email == email)
        .order_by(OTPVerification.created_at.desc())
        .first()
    )
    otp_record.otp_hash = _hash_otp(email, otp_code)
    db_session.commit()

    # Verify OTP
    v_res = client.post("/api/auth/verify-otp", json={"email": email, "otp": otp_code})
    assert v_res.status_code == 200

    # Register faculty
    reg_res = client.post(
        "/api/auth/register/faculty",
        json={
            "name": "Prof. New Faculty",
            "email": email,
            "password": "FacultyPassword123!",
            "department": "ECE",
            "designation": "Associate Professor",
            "subjects_taught": ["VLSI", "Embedded Systems"],
        },
    )
    assert reg_res.status_code == 201
    assert reg_res.json()["data"]["email"] == email

    # Login as faculty
    login_res = client.post(
        "/api/auth/login",
        json={"email": email, "password": "FacultyPassword123!"},
    )
    assert login_res.status_code == 200
    faculty_token = login_res.json()["data"]["access_token"]

    # Access faculty route -> 200 OK
    fac_res = client.get(
        "/api/faculty/dashboard-stats",
        headers={"Authorization": f"Bearer {faculty_token}"},
    )
    assert fac_res.status_code == 200
    assert fac_res.json()["success"] is True
