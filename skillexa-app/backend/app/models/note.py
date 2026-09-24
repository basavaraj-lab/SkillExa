import enum
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


def generate_uuid() -> str:
    return str(uuid.uuid4())


class VisibilityEnum(str, enum.Enum):
    COLLEGE = "college"
    DEPARTMENT = "department"
    CLASS = "class"
    SELECTED_STUDENTS = "selected_students"
    COMMUNITY = "community"


class FacultyNote(Base):
    __tablename__ = "faculty_notes"

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    faculty_id = Column(String(36), ForeignKey("faculty_profiles.id", ondelete="CASCADE"), nullable=False, index=True)
    college_id = Column(String(36), ForeignKey("colleges.id", ondelete="CASCADE"), nullable=True, index=True)
    
    title = Column(String(255), nullable=False, index=True)
    description = Column(Text, nullable=True)
    content = Column(Text, nullable=False)  # Core theory text
    
    section = Column(String(50), default="engineering", nullable=False)  # 'engineering' | 'competitive'
    subject = Column(String(100), nullable=False, index=True)
    topic = Column(String(100), nullable=False, index=True)
    subtopic = Column(String(100), nullable=True)
    language = Column(String(50), nullable=True)
    
    important_concepts = Column(JSON, default=list)  # List of strings
    quick_revision = Column(Text, nullable=True)
    
    visibility = Column(Enum(VisibilityEnum), default=VisibilityEnum.COLLEGE, nullable=False, index=True)
    published = Column(Boolean, default=True, nullable=False, index=True)
    
    # Target criteria when visibility != 'community'
    target_departments = Column(JSON, default=list)
    target_years = Column(JSON, default=list)
    target_sections = Column(JSON, default=list)
    target_student_ids = Column(JSON, default=list)
    
    views_count = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Relationships
    faculty = relationship("FacultyProfile", back_populates="notes")
    pdf_notes = relationship("PDFNote", back_populates="note", cascade="all, delete-orphan")


class PDFNote(Base):
    __tablename__ = "pdf_notes"

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    note_id = Column(String(36), ForeignKey("faculty_notes.id", ondelete="SET NULL"), nullable=True, index=True)
    faculty_id = Column(String(36), ForeignKey("faculty_profiles.id", ondelete="CASCADE"), nullable=False, index=True)
    college_id = Column(String(36), ForeignKey("colleges.id", ondelete="CASCADE"), nullable=True, index=True)
    
    title = Column(String(255), nullable=False)
    subject = Column(String(100), nullable=False, index=True)
    topic = Column(String(100), nullable=False, index=True)
    subtopic = Column(String(100), nullable=True)
    
    file_path = Column(String(500), nullable=False)  # Local storage path or URL (NEVER stored as raw blob in DB)
    file_name = Column(String(255), nullable=False)
    file_size_bytes = Column(Integer, nullable=False)
    mime_type = Column(String(100), default="application/pdf", nullable=False)
    version = Column(Integer, default=1, nullable=False)
    
    visibility = Column(Enum(VisibilityEnum), default=VisibilityEnum.COLLEGE, nullable=False, index=True)
    published = Column(Boolean, default=True, nullable=False, index=True)
    
    target_departments = Column(JSON, default=list)
    target_years = Column(JSON, default=list)
    target_sections = Column(JSON, default=list)
    target_student_ids = Column(JSON, default=list)
    
    downloads_count = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Relationships
    note = relationship("FacultyNote", back_populates="pdf_notes")
    faculty = relationship("FacultyProfile", back_populates="pdf_notes")
