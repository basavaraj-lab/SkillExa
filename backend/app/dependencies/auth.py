from typing import List, Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session
from backend.app.dependencies.db import get_db
from backend.app.models.user import (
    FacultyProfile,
    RoleEnum,
    StudentProfile,
    User,
    VerificationStatusEnum,
)
from backend.app.utils.security import decode_access_token

security_bearer = HTTPBearer(auto_error=False)


async def get_current_user(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(security_bearer),
    db: Session = Depends(get_db),
) -> User:
    """Validate Bearer JWT token and fetch active User."""
    if not credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication token missing. Please log in.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token = credentials.credentials
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired authentication token.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user_id: Optional[str] = payload.get("sub")
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token claims.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User account not found.",
        )

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User account has been deactivated.",
        )

    return user


def require_role(allowed_roles: List[RoleEnum]):
    """Enforce role-based access control."""
    def role_checker(current_user: User = Depends(get_current_user)) -> User:
        if current_user.role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Access forbidden: requires one of [{', '.join([r.value for r in allowed_roles])}] role.",
            )
        return current_user

    return role_checker


async def require_approved_faculty(
    current_user: User = Depends(require_role([RoleEnum.FACULTY, RoleEnum.COLLEGE_ADMIN])),
    db: Session = Depends(get_db),
) -> FacultyProfile:
    """
    Enforce that faculty is approved before allowing content publication.
    Returns: FacultyProfile
    """
    faculty_profile = db.query(FacultyProfile).filter(FacultyProfile.user_id == current_user.id).first()
    if not faculty_profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Faculty profile not found.",
        )

    if current_user.role != RoleEnum.COLLEGE_ADMIN and faculty_profile.verification_status != VerificationStatusEnum.APPROVED:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Your faculty account verification status is '{faculty_profile.verification_status.value}'. Only approved faculty can publish content.",
        )

    return faculty_profile


async def get_current_student(
    current_user: User = Depends(require_role([RoleEnum.STUDENT])),
    db: Session = Depends(get_db),
) -> StudentProfile:
    """Fetch verified StudentProfile for the current authenticated student."""
    student_profile = db.query(StudentProfile).filter(StudentProfile.user_id == current_user.id).first()
    if not student_profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student profile not found.",
        )
    return student_profile


async def get_optional_student(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(security_bearer),
    db: Session = Depends(get_db),
) -> Optional[StudentProfile]:
    if not credentials:
        return None
    try:
        user = await get_current_user(credentials, db)
        if user and user.role == RoleEnum.STUDENT:
            return db.query(StudentProfile).filter(StudentProfile.user_id == user.id).first()
    except Exception:
        pass
    return None
