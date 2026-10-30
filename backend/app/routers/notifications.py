from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.app.dependencies.auth import get_current_user
from backend.app.dependencies.db import get_db
from backend.app.models.college import CollegeAnnouncement
from backend.app.models.note import FacultyNote
from backend.app.models.notification import Notification, NotificationTypeEnum
from backend.app.models.quiz import Quiz
from backend.app.models.user import RoleEnum, User
from backend.app.schemas.common import ApiResponse
from backend.app.schemas.notification import NotificationResponse

router = APIRouter(prefix="/notifications", tags=["Notifications"])


@router.get("", response_model=ApiResponse[List[NotificationResponse]])
def get_user_notifications(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    query = db.query(Notification).filter(Notification.user_id == current_user.id)
    if current_user.role == RoleEnum.FACULTY:
        query = query.filter(
            ~Notification.type.in_([
                NotificationTypeEnum.NEW_NOTE,
                NotificationTypeEnum.NEW_QUIZ,
                NotificationTypeEnum.NEW_VIDEO,
                NotificationTypeEnum.NEW_ASSIGNMENT,
            ])
        )

    all_notifs = query.order_by(Notification.created_at.desc()).all()

    valid_notifs = []
    seen_keys = set()
    to_delete = []

    for n in all_notifs:
        # Check for duplicates by title + message
        key = (n.title.strip(), n.message.strip())
        if key in seen_keys:
            to_delete.append(n)
            continue

        # Check orphaned reference_id
        if n.reference_id:
            if n.type == NotificationTypeEnum.NEW_NOTE:
                if not db.query(FacultyNote.id).filter(FacultyNote.id == n.reference_id).first():
                    to_delete.append(n)
                    continue
            elif n.type == NotificationTypeEnum.NEW_QUIZ:
                if not db.query(Quiz.id).filter(Quiz.id == n.reference_id).first():
                    to_delete.append(n)
                    continue
            elif n.type == NotificationTypeEnum.ANNOUNCEMENT:
                if not db.query(CollegeAnnouncement.id).filter(CollegeAnnouncement.id == n.reference_id).first():
                    to_delete.append(n)
                    continue

        seen_keys.add(key)
        valid_notifs.append(n)

    if to_delete:
        for d in to_delete:
            db.delete(d)
        db.commit()

    return ApiResponse(
        success=True,
        message="Notifications retrieved.",
        data=[NotificationResponse.model_validate(n) for n in valid_notifs[:50]],
    )


@router.post("/{id}/read", response_model=ApiResponse[dict])
def mark_notification_as_read(
    id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    notif = db.query(Notification).filter(Notification.id == id, Notification.user_id == current_user.id).first()
    if notif:
        notif.is_read = True
        db.commit()

    return ApiResponse(
        success=True,
        message="Notification marked as read.",
        data={"id": id, "is_read": True},
    )


@router.post("/read-all", response_model=ApiResponse[dict])
def mark_all_notifications_read(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    db.query(Notification).filter(Notification.user_id == current_user.id).update({"is_read": True})
    db.commit()
    return ApiResponse(
        success=True,
        message="All notifications marked as read.",
        data={"all_read": True},
    )


@router.delete("/{id}", response_model=ApiResponse[dict])
def delete_notification(
    id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    notif = db.query(Notification).filter(Notification.id == id, Notification.user_id == current_user.id).first()
    if notif:
        db.delete(notif)
        db.commit()
    return ApiResponse(
        success=True,
        message="Notification deleted.",
        data={"id": id, "deleted": True},
    )
