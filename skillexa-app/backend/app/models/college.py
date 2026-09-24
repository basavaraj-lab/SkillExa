import uuid
from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, JSON, String, Text
from sqlalchemy.orm import relationship
from backend.app.database import Base


def generate_uuid() -> str:
    return str(uuid.uuid4())


class College(Base):
    __tablename__ = "colleges"

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    code = Column(String(50), unique=True, nullable=False, index=True)  # e.g., 'KVG001', 'RVCE01'
    name = Column(String(255), nullable=False)
    city = Column(String(100), nullable=True)
    state = Column(String(100), nullable=True)
    is_verified = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    students = relationship("StudentProfile", back_populates="college")
    faculty_members = relationship("FacultyProfile", back_populates="college")
    announcements = relationship("CollegeAnnouncement", back_populates="college", cascade="all, delete-orphan")


class CollegeAnnouncement(Base):
    __tablename__ = "college_announcements"

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    college_id = Column(String(36), ForeignKey("colleges.id", ondelete="CASCADE"), nullable=False, index=True)
    faculty_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    faculty_name = Column(String(255), nullable=False)
    faculty_dept = Column(String(100), nullable=False)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    priority = Column(String(50), default="NORMAL")  # 'NORMAL', 'HIGH', 'URGENT'
    is_pinned = Column(Boolean, default=False)
    target_departments = Column(JSON, default=list)  # List of department codes, e.g. ['ECE']
    target_years = Column(JSON, default=list)  # e.g. ['3rd Year']
    target_sections = Column(JSON, default=list)  # e.g. ['A']
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    college = relationship("College", back_populates="announcements")
    author = relationship("User")
