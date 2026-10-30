from typing import Any, Dict, List, Optional
from sqlalchemy.orm import Session
from backend.app.models.notification import Notification, NotificationTypeEnum
from backend.app.models.user import FacultyFollow, RoleEnum, StudentProfile
from backend.app.services.college_service import CollegeService


class NotificationService:
    @staticmethod
    def send_notification(
        db: Session,
        user_id: str,
        notification_type: NotificationTypeEnum,
        title: str,
        message: str,
        reference_id: Optional[str] = None,
        action_route: Optional[str] = None,
        action_params: Optional[Dict[str, Any]] = None,
    ) -> Notification:
        notif = Notification(
            user_id=user_id,
            type=notification_type,
            title=title,
            message=message,
            reference_id=reference_id,
            action_route=action_route,
            action_params=action_params or {},
            is_read=False,
        )
        db.add(notif)
        db.commit()
        db.refresh(notif)
        return notif

    @staticmethod
    def notify_targeted_students(
        db: Session,
        college_id: Optional[str],
        target_departments: Optional[List[str]],
        target_years: Optional[List[str]],
        target_sections: Optional[List[str]],
        target_student_ids: Optional[List[str]],
        notification_type: Any,
        title: str,
        message: str,
        reference_id: Optional[str] = None,
        action_route: Optional[str] = None,
        action_params: Optional[Dict[str, Any]] = None,
    ):
        """Dispatch notifications only to matching students."""
        college_ids = [college_id] if college_id else []
        if college_id in ["0f669a91-5c8d-4304-a815-818bde05e996", "clg-kvg"]:
            college_ids = ["0f669a91-5c8d-4304-a815-818bde05e996", "clg-kvg"]

        students_query = db.query(StudentProfile)
        if college_ids:
            students_query = students_query.filter(StudentProfile.college_id.in_(college_ids))
        students = students_query.all()

        try:
            notif_enum = NotificationTypeEnum(notification_type) if isinstance(notification_type, str) else notification_type
        except Exception:
            notif_enum = NotificationTypeEnum.ANNOUNCEMENT

        for student in students:
            # Never notify faculty accounts
            if student.user and student.user.role == RoleEnum.FACULTY:
                continue

            if CollegeService.matches_student_targeting(
                college_id,
                target_departments,
                target_years,
                target_sections,
                target_student_ids,
                student,
            ):
                # De-duplicate: avoid inserting duplicate notifications for the same reference or title
                if reference_id:
                    existing = db.query(Notification).filter(
                        Notification.user_id == student.user_id,
                        Notification.reference_id == reference_id,
                    ).first()
                    if existing:
                        continue
                else:
                    existing = db.query(Notification).filter(
                        Notification.user_id == student.user_id,
                        Notification.title == title,
                    ).first()
                    if existing:
                        continue

                notif = Notification(
                    user_id=student.user_id,
                    type=notif_enum,
                    title=title,
                    message=message,
                    reference_id=reference_id,
                    action_route=action_route,
                    action_params=action_params or {},
                    is_read=False,
                )
                db.add(notif)
        db.commit()

    @staticmethod
    def notify_faculty_followers(
        db: Session,
        faculty_user_id: str,
        title: str,
        message: str,
        reference_id: Optional[str] = None,
        action_route: Optional[str] = None,
        action_params: Optional[Dict[str, Any]] = None,
    ):
        """Notify students who follow this faculty member when they publish Community content."""
        follows = db.query(FacultyFollow).filter(FacultyFollow.faculty_id == faculty_user_id).all()
        for follow in follows:
            notif = Notification(
                user_id=follow.student_id,
                type=NotificationTypeEnum.COMMUNITY_UPLOAD,
                title=title,
                message=message,
                reference_id=reference_id,
                action_route=action_route,
                action_params=action_params or {},
                is_read=False,
            )
            db.add(notif)
        db.commit()
