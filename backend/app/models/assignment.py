import uuid
from datetime import datetime
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Float,
    ForeignKey,
    JSON,
    String,
    Text,
)
from sqlalchemy.orm import relationship
from backend.app.database import Base


def generate_uuid() -> str:
    return str(uuid.uuid4())


class Assignment(Base):
    __tablename__ = "assignments"

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    faculty_id = Column(String(36), ForeignKey("faculty_profiles.id", ondelete="CASCADE"), nullable=False, index=True)
    college_id = Column(String(36), ForeignKey("colleges.id", ondelete="CASCADE"), nullable=True, index=True)

    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    subject = Column(String(100), nullable=False, index=True)
    topic = Column(String(100), nullable=False, index=True)
    
    max_marks = Column(Float, default=100.0, nullable=False)
    due_date = Column(DateTime, nullable=False)
    published = Column(Boolean, default=True, nullable=False)

    target_departments = Column(JSON, default=list)
    target_years = Column(JSON, default=list)
    target_sections = Column(JSON, default=list)
    target_student_ids = Column(JSON, default=list)

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Relationships
    faculty = relationship("FacultyProfile", back_populates="assignments")
    submissions = relationship("AssignmentSubmission", back_populates="assignment", cascade="all, delete-orphan")


class AssignmentSubmission(Base):
    __tablename__ = "assignment_submissions"

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    assignment_id = Column(String(36), ForeignKey("assignments.id", ondelete="CASCADE"), nullable=False, index=True)
    student_id = Column(String(36), ForeignKey("student_profiles.id", ondelete="CASCADE"), nullable=False, index=True)

    submission_text = Column(Text, nullable=True)
    file_path = Column(String(500), nullable=True)
    status = Column(String(50), default="SUBMITTED", nullable=False)  # 'SUBMITTED', 'EVALUATED', 'LATE'
    
    score = Column(Float, nullable=True)
    feedback = Column(Text, nullable=True)
    
    submitted_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    evaluated_at = Column(DateTime, nullable=True)

    # Relationships
    assignment = relationship("Assignment", back_populates="submissions")
    student = relationship("StudentProfile", back_populates="assignment_submissions")
