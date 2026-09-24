from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr
from backend.app.models.user import RoleEnum, VerificationStatusEnum


class StudentProfileResponse(BaseModel):
    id: str
    user_id: str
    college_id: Optional[str] = None
    college_name: Optional[str] = None
    college_code: Optional[str] = None
    branch: str
    academic_year: str
    section: str
    roll_number: Optional[str] = None
    phone: Optional[str] = None
    target_exam: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True


class FacultyProfileResponse(BaseModel):
    id: str
    user_id: str
    college_id: Optional[str] = None
    college_name: Optional[str] = None
    college_code: Optional[str] = None
    department: str
    designation: str
    office_room: Optional[str] = None
    subjects_taught: List[str] = []
    verification_status: VerificationStatusEnum
    bio: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True


class UserResponse(BaseModel):
    id: str
    email: EmailStr
    name: str
    role: RoleEnum
    is_active: bool
    avatar: Optional[str] = None
    student_profile: Optional[StudentProfileResponse] = None
    faculty_profile: Optional[FacultyProfileResponse] = None
    created_at: datetime

    class Config:
        from_attributes = True


class UpdateStudentProfileRequest(BaseModel):
    name: Optional[str] = None
    branch: Optional[str] = None
    academic_year: Optional[str] = None
    section: Optional[str] = None
    roll_number: Optional[str] = None
    phone: Optional[str] = None
    target_exam: Optional[str] = None


class UpdateFacultyProfileRequest(BaseModel):
    name: Optional[str] = None
    department: Optional[str] = None
    designation: Optional[str] = None
    office_room: Optional[str] = None
    subjects_taught: Optional[List[str]] = None
    bio: Optional[str] = None


class FacultyVerificationRequest(BaseModel):
    verification_status: VerificationStatusEnum
