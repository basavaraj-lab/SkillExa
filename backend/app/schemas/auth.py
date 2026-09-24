from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field
from backend.app.models.user import RoleEnum, VerificationStatusEnum


class RegisterStudentRequest(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=100)
    college_id: Optional[str] = None
    branch: str = Field(..., min_length=2, max_length=50)  # e.g., 'ECE', 'CSE'
    academic_year: str = Field(..., min_length=2, max_length=50)  # e.g., '3rd Year'
    section: str = Field(..., min_length=1, max_length=10)  # e.g., 'A'
    roll_number: Optional[str] = None
    phone: Optional[str] = None
    target_exam: Optional[str] = "Placement"


class RegisterFacultyRequest(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=100)
    college_id: Optional[str] = None
    department: str = Field(..., min_length=2, max_length=50)  # e.g., 'ECE'
    designation: str = Field(default="Assistant Professor", max_length=100)
    subjects_taught: List[str] = Field(default_factory=list)
    office_room: Optional[str] = None
    bio: Optional[str] = None


class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=1)


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in_minutes: int
    user: dict


class TokenData(BaseModel):
    user_id: Optional[str] = None
    email: Optional[str] = None
    role: Optional[RoleEnum] = None
