from typing import Optional, Tuple
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from backend.app.models.college import College
from backend.app.models.user import (
    FacultyProfile,
    RoleEnum,
    StudentProfile,
    User,
    VerificationStatusEnum,
)
from backend.app.schemas.auth import (
    LoginRequest,
    RegisterFacultyRequest,
    RegisterStudentRequest,
    TokenResponse,
)
from backend.app.utils.security import (
    create_access_token,
    hash_password,
    verify_password,
)


class AuthService:
    @staticmethod
    def register_student(db: Session, req: RegisterStudentRequest) -> Tuple[User, StudentProfile]:
        # 1. Check existing email
        if db.query(User).filter(User.email == req.email.lower()).first():
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="An account with this email already exists.",
            )

        # 2. Resolve college if provided
        college_id = req.college_id
        if college_id:
            college = db.query(College).filter((College.id == college_id) | (College.code == college_id)).first()
            if college:
                college_id = college.id

        # 3. Create User
        user = User(
            email=req.email.lower(),
            password_hash=hash_password(req.password),
            name=req.name.strip(),
            role=RoleEnum.STUDENT,
            is_active=True,
        )
        db.add(user)
        db.flush()

        # 4. Create Student Profile
        student_profile = StudentProfile(
            user_id=user.id,
            college_id=college_id,
            branch=req.branch.upper().strip(),
            academic_year=req.academic_year.strip(),
            section=req.section.upper().strip(),
            roll_number=req.roll_number.strip() if req.roll_number else None,
            phone=req.phone.strip() if req.phone else None,
            target_exam=req.target_exam or "Placement",
        )
        db.add(student_profile)
        db.commit()
        db.refresh(user)
        db.refresh(student_profile)
        return user, student_profile

    @staticmethod
    def register_faculty(db: Session, req: RegisterFacultyRequest) -> Tuple[User, FacultyProfile]:
        # 1. Check existing email
        if db.query(User).filter(User.email == req.email.lower()).first():
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="An account with this email already exists.",
            )

        # 2. Resolve college
        college_id = req.college_id
        if college_id:
            college = db.query(College).filter((College.id == college_id) | (College.code == college_id)).first()
            if college:
                college_id = college.id

        # 3. Create User
        user = User(
            email=req.email.lower(),
            password_hash=hash_password(req.password),
            name=req.name.strip(),
            role=RoleEnum.FACULTY,
            is_active=True,
        )
        db.add(user)
        db.flush()

        # 4. Create Faculty Profile (default status: PENDING unless configured)
        faculty_profile = FacultyProfile(
            user_id=user.id,
            college_id=college_id,
            department=req.department.upper().strip(),
            designation=req.designation.strip(),
            office_room=req.office_room.strip() if req.office_room else None,
            subjects_taught=req.subjects_taught or [],
            verification_status=VerificationStatusEnum.APPROVED,  # Default approved for smooth seed/demo flow
            bio=req.bio,
        )
        db.add(faculty_profile)
        db.commit()
        db.refresh(user)
        db.refresh(faculty_profile)
        return user, faculty_profile

    @staticmethod
    def login(db: Session, req: LoginRequest) -> TokenResponse:
        user = db.query(User).filter(User.email == req.email.lower()).first()
        if not user or not verify_password(req.password, user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password.",
            )

        if not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Your account has been deactivated.",
            )

        # Generate JWT
        token = create_access_token(
            subject=user.id,
            claims={
                "email": user.email,
                "name": user.name,
                "role": user.role.value,
            },
        )

        user_info = {
            "id": user.id,
            "email": user.email,
            "name": user.name,
            "role": user.role.value,
        }

        if user.role == RoleEnum.STUDENT and user.student_profile:
            user_info["student_profile"] = {
                "id": user.student_profile.id,
                "college_id": user.student_profile.college_id,
                "branch": user.student_profile.branch,
                "academic_year": user.student_profile.academic_year,
                "section": user.student_profile.section,
            }
        elif user.role == RoleEnum.FACULTY and user.faculty_profile:
            user_info["faculty_profile"] = {
                "id": user.faculty_profile.id,
                "college_id": user.faculty_profile.college_id,
                "department": user.faculty_profile.department,
                "designation": user.faculty_profile.designation,
                "verification_status": user.faculty_profile.verification_status.value,
            }

        return TokenResponse(
            access_token=token,
            token_type="bearer",
            expires_in_minutes=1440,
            user=user_info,
        )
