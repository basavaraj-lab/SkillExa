from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from backend.app.dependencies.auth import get_current_user
from backend.app.dependencies.db import get_db
from backend.app.models.user import User
from backend.app.schemas.auth import (
    LoginRequest,
    RegisterFacultyRequest,
    RegisterStudentRequest,
    TokenResponse,
)
from backend.app.schemas.common import ApiResponse
from backend.app.schemas.user import UserResponse
from backend.app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Authentication"])


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


from pydantic import BaseModel, EmailStr

class SendOtpRequest(BaseModel):
    email: str
    mobile: str | None = None
    otp: str

@router.post("/send-otp", response_model=ApiResponse[dict])
def send_otp(req: SendOtpRequest):
    print(f"\n==========================================")
    print(f"[SkillExa OTP Dispatch Service]")
    print(f"To: {req.email or req.mobile}")
    print(f"Subject: SkillExa Account Registration OTP Verification Code")
    print(f"Body: Hello! Your 6-digit SkillExa registration OTP code is: {req.otp}. Enter this code to complete your registration.")
    print(f"==========================================\n")
    return ApiResponse(
        success=True,
        message=f"OTP successfully sent to {req.email or req.mobile}",
        data={"recipient": req.email or req.mobile, "status": "DELIVERED"}
    )

@router.get("/me", response_model=ApiResponse[UserResponse])
def get_current_user_profile(current_user: User = Depends(get_current_user)):
    return ApiResponse(
        success=True,
        message="Current user profile retrieved.",
        data=current_user,
    )
