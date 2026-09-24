import enum
import uuid
from datetime import datetime
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Enum,
    Float,
    ForeignKey,
    Integer,
    JSON,
    String,
    Text,
)
from sqlalchemy.orm import relationship
from backend.app.database import Base


def generate_uuid() -> str:
    return str(uuid.uuid4())


class NotificationTypeEnum(str, enum.Enum):
    NEW_NOTE = "NEW_NOTE"
    NOTE_UPDATED = "NOTE_UPDATED"
    NEW_PDF = "NEW_PDF"
    NEW_VIDEO = "NEW_VIDEO"
    NEW_QUIZ = "NEW_QUIZ"
    NEW_ASSIGNMENT = "NEW_ASSIGNMENT"
    INTERVIEW_INVITATION = "INTERVIEW_INVITATION"
    QUIZ_RESULT = "QUIZ_RESULT"
    INTERVIEW_RESULT = "INTERVIEW_RESULT"
    COMMUNITY_UPLOAD = "COMMUNITY_UPLOAD"


class Notification(Base):
    __tablename__ = "notifications"

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    
    type = Column(Enum(NotificationTypeEnum), nullable=False, index=True)
    title = Column(String(255), nullable=False)
    message = Column(Text, nullable=False)
    
    reference_id = Column(String(100), nullable=True)
    action_route = Column(String(100), nullable=True)
    action_params = Column(JSON, default=dict)
    
    is_read = Column(Boolean, default=False, nullable=False, index=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    user = relationship("User", back_populates="notifications")


class StudentProgress(Base):
    __tablename__ = "student_progress"

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    student_id = Column(String(36), ForeignKey("student_profiles.id", ondelete="CASCADE"), nullable=False, index=True)
    
    section = Column(String(50), nullable=False, index=True)  # 'engineering' | 'competitive' | 'programming' | 'dsa'
    subject = Column(String(100), nullable=False, index=True)
    topic = Column(String(100), nullable=False, index=True)
    subtopic = Column(String(100), nullable=True)
    
    mastery_percentage = Column(Float, default=0.0, nullable=False)
    quizzes_completed = Column(Integer, default=0, nullable=False)
    quiz_accuracy = Column(Float, default=0.0, nullable=False)
    notes_read = Column(Integer, default=0, nullable=False)
    coding_solved = Column(Integer, default=0, nullable=False)
    
    last_activity_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    student = relationship("StudentProfile", back_populates="progress_records")
