from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.app.dependencies.auth import get_current_user
from backend.app.dependencies.db import get_db
from backend.app.models.notification import Notification
from backend.app.models.user import User
from backend.app.schemas.common import ApiResponse
from backend.app.schemas.notification import NotificationResponse

router = APIRouter(prefix="/notifications", tags=["Notifications"])


@router.get("", response_model=ApiResponse[List[NotificationResponse]])
def get_user_notifications(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    notifs = (
        db.query(Notification)
        .filter(Notification.user_id == current_user.id)
        .order_by(Notification.created_at.desc())
        .limit(50)
        .all()
    )
    return ApiResponse(
        success=True,
        message="Notifications retrieved.",
        data=[NotificationResponse.model_validate(n) for n in notifs],
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
