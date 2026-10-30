from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session

from backend.app.dependencies.auth import get_current_user
from backend.app.dependencies.db import get_db
from backend.app.models.user import User
from backend.app.schemas.auth import (
    GoogleLoginRequest,
    LoginRequest,
    RegisterFacultyRequest,
    RegisterStudentRequest,
    TokenResponse,
)
from backend.app.schemas.common import ApiResponse
from backend.app.schemas.user import UpdateStudentProfileRequest, UserResponse
from backend.app.services.auth_service import AuthService
from backend.app.services.otp_service import OTPService

router = APIRouter(prefix="/auth", tags=["Authentication"])


class SendOTPPayload(BaseModel):
    email: EmailStr


class VerifyOTPPayload(BaseModel):
    email: EmailStr
    otp: str


@router.post("/register", response_model=ApiResponse[dict])
def register_init(payload: SendOTPPayload, db: Session = Depends(get_db)):
    result = OTPService.send_otp(db, payload.email)
    return ApiResponse(
        success=True,
        message="Verification OTP sent to your email.",
        data=result,
    )


@router.post("/send-otp", response_model=ApiResponse[dict])
def send_otp(payload: SendOTPPayload, db: Session = Depends(get_db)):
    result = OTPService.send_otp(db, payload.email)
    return ApiResponse(
        success=True,
        message=result["message"],
        data=result,
    )


@router.post("/verify-otp", response_model=ApiResponse[dict])
def verify_otp(payload: VerifyOTPPayload, db: Session = Depends(get_db)):
    result = OTPService.verify_otp(db, payload.email, payload.otp)
    return ApiResponse(
        success=True,
        message=result["message"],
        data=result,
    )


@router.post("/resend-otp", response_model=ApiResponse[dict])
def resend_otp(payload: SendOTPPayload, db: Session = Depends(get_db)):
    result = OTPService.send_otp(db, payload.email)
    return ApiResponse(
        success=True,
        message="New verification OTP sent to your email.",
        data=result,
    )


@router.post("/register/student", response_model=ApiResponse[dict], status_code=status.HTTP_201_CREATED)
def register_student(req: RegisterStudentRequest, db: Session = Depends(get_db)):
    user, student_profile = AuthService.register_student(db, req)
    return ApiResponse(
        success=True,
        message="Student registered successfully!",
        data={
            "user_id": user.id,
            "email": user.email,
            "name": user.name,
            "role": user.role.value,
            "student_profile_id": student_profile.id,
            "branch": student_profile.branch,
            "academic_year": student_profile.academic_year,
            "section": student_profile.section,
        },
    )


@router.post("/register/faculty", response_model=ApiResponse[dict], status_code=status.HTTP_201_CREATED)
def register_faculty(req: RegisterFacultyRequest, db: Session = Depends(get_db)):
    user, faculty_profile = AuthService.register_faculty(db, req)
    return ApiResponse(
        success=True,
        message="Faculty registered successfully!",
        data={
            "user_id": user.id,
            "email": user.email,
            "name": user.name,
            "role": user.role.value,
            "faculty_profile_id": faculty_profile.id,
            "department": faculty_profile.department,
            "verification_status": faculty_profile.verification_status.value,
        },
    )


@router.post("/login", response_model=ApiResponse[TokenResponse])
def login(req: LoginRequest, db: Session = Depends(get_db)):
    token_response = AuthService.login(db, req)
    return ApiResponse(
        success=True,
        message="Login successful!",
        data=token_response,
    )


@router.post("/google-login", response_model=ApiResponse[TokenResponse])
def google_login(req: GoogleLoginRequest, db: Session = Depends(get_db)):
    """
    Authenticate a user logging in via Google / OAuth.
    Validates user in database, correctly identifies role (student vs faculty),
    and issues JWT token with real database ID and role.
    """
    token_response = AuthService.google_login(db, req)
    return ApiResponse(
        success=True,
        message="Google login successful!",
        data=token_response,
    )


@router.get("/me", response_model=ApiResponse[UserResponse])
def get_current_user_profile(current_user: User = Depends(get_current_user)):
    return ApiResponse(
        success=True,
        message="Current user profile retrieved.",
        data=current_user,
    )


@router.put("/me", response_model=ApiResponse[UserResponse])
def update_current_user_profile(
    req: UpdateStudentProfileRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    if req.name:
        current_user.name = req.name.strip()
    if current_user.student_profile:
        sp = current_user.student_profile
        if req.branch is not None:
            sp.branch = req.branch.strip()
        if req.academic_year is not None:
            sp.academic_year = req.academic_year.strip()
        if req.section is not None:
            sp.section = req.section.strip()
        if req.roll_number is not None:
            sp.roll_number = req.roll_number.strip()
        if req.phone is not None:
            sp.phone = req.phone.strip()
        if req.target_exam is not None:
            sp.target_exam = req.target_exam.strip()
    db.commit()
    db.refresh(current_user)
    return ApiResponse(
        success=True,
        message="Profile updated successfully.",
        data=current_user,
    )
