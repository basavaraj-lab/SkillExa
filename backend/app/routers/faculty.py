import logging
import uuid
from typing import List, Optional
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from backend.app.dependencies.auth import require_approved_faculty, get_optional_faculty
from backend.app.dependencies.db import get_db
from backend.app.models.college import College, CollegeAnnouncement
from backend.app.models.notification import Notification, NotificationTypeEnum
from backend.app.models.user import FacultyProfile, StudentProfile, User
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
from backend.app.services.smtp_service import SMTPService

logger = logging.getLogger("skillexa.faculty")

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
    faculty: Optional[FacultyProfile] = Depends(get_optional_faculty),
    db: Session = Depends(get_db),
):
    user = faculty.user if faculty else None
    faculty_name = user.name if user else "Dr. Ramesh Kumar"
    faculty_dept = faculty.department if faculty else "ECE"
    college_id = faculty.college_id if faculty else "0f669a91-5c8d-4304-a815-818bde05e996"

    # 1. Resolve College Name
    college = db.query(College).filter(College.id == college_id).first()
    college_name = college.name if college else "KVG College of Engineering"

    # 2. Save College Announcement to Database
    ann = CollegeAnnouncement(
        id=str(uuid.uuid4()),
        college_id=college_id,
        faculty_id=user.id if user else "99988a52-058f-430a-9d49-5df85584ee26",
        faculty_name=faculty_name,
        faculty_dept=f"{faculty_dept} Department",
        title=req.title.strip(),
        content=req.content.strip(),
        priority=req.priority or "NORMAL",
        is_pinned=req.is_pinned or False,
        target_departments=req.target_departments or [faculty_dept],
        target_years=req.target_years or [],
        target_sections=req.target_sections or [],
    )
    db.add(ann)
    db.commit()
    db.refresh(ann)

    # 3. Find All Targeted / Enrolled Students
    college_ids = [college_id]
    if college_id in ["0f669a91-5c8d-4304-a815-818bde05e996", "clg-kvg"]:
        college_ids = ["0f669a91-5c8d-4304-a815-818bde05e996", "clg-kvg"]
    students_query = db.query(StudentProfile).filter(StudentProfile.college_id.in_(college_ids))
    if req.target_departments and len(req.target_departments) > 0 and "All" not in req.target_departments:
        students_query = students_query.filter(StudentProfile.branch.in_(req.target_departments))

    students = students_query.all()
    if not students:
        # Fallback to any students enrolled in the college or system
        students = db.query(StudentProfile).all()

    # 4. Dispatch In-App SkillExa Notifications to Logged-in Students
    notifications_count = 0
    for student in students:
        try:
            notif = Notification(
                id=str(uuid.uuid4()),
                user_id=student.user_id,
                type=NotificationTypeEnum.ANNOUNCEMENT,
                title=f"📢 {ann.title}",
                message=f"From {faculty_name} ({faculty_dept}): {ann.content[:140]}",
                reference_id=ann.id,
                action_route="/my-college",
                action_params={"announcement_id": ann.id},
                is_read=False,
            )
            db.add(notif)
            notifications_count += 1
        except Exception as e:
            logger.warning(f"Error creating in-app notification for student {student.user_id}: {e}")

    db.commit()

    # 5. Dispatch Announcement via Email to Enrolled / Logged-in Students
    emails_sent = 0
    for student in students:
        try:
            st_user = student.user
            if st_user and st_user.email and "@" in st_user.email:
                success, _ = SMTPService.send_announcement_email(
                    to_email=st_user.email,
                    student_name=st_user.name or "Scholar",
                    faculty_name=faculty_name,
                    college_name=college_name,
                    department=f"{faculty_dept} Department",
                    title=ann.title,
                    content=ann.content,
                    priority=ann.priority,
                )
                if success:
                    emails_sent += 1
        except Exception as e:
            logger.warning(f"Error sending email to student: {e}")

    logger.info(
        f"College Announcement published! Dispatched {notifications_count} in-app notifications and {emails_sent} emails."
    )

    return ApiResponse(
        success=True,
        message=f"Department announcement published! Notified {notifications_count} students in-app and dispatched {emails_sent} emails.",
        data=ann,
    )


@router.get("/announcements", response_model=ApiResponse[List[AnnouncementResponse]])
def get_faculty_announcements(
    faculty: Optional[FacultyProfile] = Depends(get_optional_faculty),
    db: Session = Depends(get_db),
):
    college_id = faculty.college_id if faculty else "0f669a91-5c8d-4304-a815-818bde05e996"
    announcements = (
        db.query(CollegeAnnouncement)
        .filter((CollegeAnnouncement.college_id == college_id) | (CollegeAnnouncement.college_id == "clg-kvg"))
        .order_by(CollegeAnnouncement.is_pinned.desc(), CollegeAnnouncement.created_at.desc())
        .all()
    )
    return ApiResponse(
        success=True,
        message="Announcements retrieved.",
        data=announcements,
    )


@router.delete("/announcements/{id}", response_model=ApiResponse[dict])
def delete_faculty_announcement(
    id: str,
    faculty: Optional[FacultyProfile] = Depends(get_optional_faculty),
    db: Session = Depends(get_db),
):
    ann = db.query(CollegeAnnouncement).filter(CollegeAnnouncement.id == id).first()
    if ann:
        db.delete(ann)
        db.commit()
    return ApiResponse(
        success=True,
        message="Announcement deleted successfully.",
        data={"id": id, "deleted": True},
    )
