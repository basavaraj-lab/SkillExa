import uuid
from datetime import datetime
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    JSON,
    String,
    Text,
)
from sqlalchemy.orm import relationship
from backend.app.database import Base
from backend.app.models.note import VisibilityEnum


def generate_uuid() -> str:
    return str(uuid.uuid4())


class FacultyVideo(Base):
    __tablename__ = "faculty_videos"

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    faculty_id = Column(String(36), ForeignKey("faculty_profiles.id", ondelete="CASCADE"), nullable=False, index=True)
    college_id = Column(String(36), ForeignKey("colleges.id", ondelete="CASCADE"), nullable=True, index=True)

    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    video_url = Column(String(500), nullable=False)
    thumbnail_url = Column(String(500), nullable=True)
    duration = Column(String(50), default="20 mins")

    section = Column(String(50), default="engineering", nullable=False)
    subject = Column(String(100), nullable=False, index=True)
    topic = Column(String(100), nullable=False, index=True)
    subtopic = Column(String(100), nullable=True)
    language = Column(String(50), nullable=True)

    visibility = Column(Enum(VisibilityEnum), default=VisibilityEnum.COLLEGE, nullable=False, index=True)
    published = Column(Boolean, default=True, nullable=False, index=True)

    target_departments = Column(JSON, default=list)
    target_years = Column(JSON, default=list)
    target_sections = Column(JSON, default=list)
    target_student_ids = Column(JSON, default=list)

    views_count = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Relationships
    faculty = relationship("FacultyProfile", back_populates="videos")
