from datetime import datetime
from typing import Any, Dict, Optional
from pydantic import BaseModel
from backend.app.models.notification import NotificationTypeEnum


class NotificationResponse(BaseModel):
    id: str
    user_id: str
    type: NotificationTypeEnum
    title: str
    message: str
    reference_id: Optional[str] = None
    action_route: Optional[str] = None
    action_params: Dict[str, Any] = {}
    is_read: bool
    created_at: datetime

    class Config:
        from_attributes = True


class MarkNotificationReadRequest(BaseModel):
    notification_id: str
