from typing import Any, Dict, List, Optional
from sqlalchemy.orm import Session
from backend.app.models.notification import Notification, NotificationTypeEnum
from backend.app.models.user import FacultyFollow, StudentProfile
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
        notification_type: NotificationTypeEnum,
        title: str,
        message: str,
        reference_id: Optional[str] = None,
        action_route: Optional[str] = None,
        action_params: Optional[Dict[str, Any]] = None,
    ):
        """Dispatch notifications only to matching students."""
        if not college_id:
            return

        students = db.query(StudentProfile).filter(StudentProfile.college_id == college_id).all()
        for student in students:
            if CollegeService.matches_student_targeting(
                college_id,
                target_departments,
                target_years,
                target_sections,
                target_student_ids,
                student,
            ):
                notif = Notification(
                    user_id=student.user_id,
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
