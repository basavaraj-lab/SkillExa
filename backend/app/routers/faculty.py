from typing import List, Optional
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from backend.app.dependencies.auth import require_approved_faculty
from backend.app.dependencies.db import get_db
from backend.app.models.college import CollegeAnnouncement
from backend.app.models.user import FacultyProfile, StudentProfile
from backend.app.schemas.college import (
    AnnouncementResponse,
    CreateAnnouncementRequest,
)
from backend.app.schemas.common import ApiResponse
from backend.app.schemas.progress import (
    FacultyDashboardStatsResponse,
    FacultyStudentPerformanceItem,
)
from backend.app.schemas.user import FacultyProfileResponse
from backend.app.services.progress_service import ProgressService

router = APIRouter(prefix="/faculty", tags=["Faculty"])


@router.get("/profile", response_model=ApiResponse[FacultyProfileResponse])
def get_faculty_profile(
    faculty: FacultyProfile = Depends(require_approved_faculty),
):
    return ApiResponse(
        success=True,
        message="Faculty profile retrieved.",
        data=faculty,
    )


@router.get("/dashboard-stats", response_model=ApiResponse[FacultyDashboardStatsResponse])
def get_faculty_dashboard_stats(
    faculty: FacultyProfile = Depends(require_approved_faculty),
    db: Session = Depends(get_db),
):
    stats = ProgressService.get_faculty_dashboard_stats(db, faculty)
    return ApiResponse(
        success=True,
        message="Dashboard statistics retrieved.",
        data=stats,
    )


@router.get("/performance", response_model=ApiResponse[List[FacultyStudentPerformanceItem]])
def get_class_performance(
    faculty: FacultyProfile = Depends(require_approved_faculty),
    db: Session = Depends(get_db),
):
    """
    Section 25: Return performance dashboard for authorized students in faculty's department.
    """
    items = ProgressService.get_faculty_class_performance(db, faculty)
    return ApiResponse(
        success=True,
        message="Department student performance roster retrieved.",
        data=items,
    )


@router.get("/students", response_model=ApiResponse[List[dict]])
def get_department_students(
    faculty: FacultyProfile = Depends(require_approved_faculty),
    db: Session = Depends(get_db),
):
    """Fetch all students enrolled in faculty's department & college."""
    students = (
        db.query(StudentProfile)
        .filter(StudentProfile.college_id == faculty.college_id, StudentProfile.branch == faculty.department)
        .all()
    )
    result = [
        {
            "id": s.id,
            "user_id": s.user_id,
            "name": s.user.name if s.user else "Student",
            "email": s.user.email if s.user else "",
            "branch": s.branch,
            "academic_year": s.academic_year,
            "section": s.section,
            "roll_number": s.roll_number,
        }
        for s in students
    ]
    return ApiResponse(
        success=True,
        message="Department students retrieved.",
        data=result,
    )


@router.post("/announcements", response_model=ApiResponse[AnnouncementResponse], status_code=status.HTTP_201_CREATED)
def create_announcement(
    req: CreateAnnouncementRequest,
    faculty: FacultyProfile = Depends(require_approved_faculty),
    db: Session = Depends(get_db),
):
    user = faculty.user
    ann = CollegeAnnouncement(
        college_id=faculty.college_id or "clg-default",
        faculty_id=user.id,
        faculty_name=user.name,
        faculty_dept=faculty.department,
        title=req.title.strip(),
        content=req.content.strip(),
        priority=req.priority or "NORMAL",
        is_pinned=req.is_pinned or False,
        target_departments=req.target_departments or [faculty.department],
        target_years=req.target_years or [],
        target_sections=req.target_sections or [],
    )
    db.add(ann)
    db.commit()
    db.refresh(ann)
    return ApiResponse(
        success=True,
        message="Department announcement published!",
        data=ann,
    )
