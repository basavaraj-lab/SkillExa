import enum
import uuid
from datetime import datetime
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Enum,
    ForeignKey,
    JSON,
    String,
    Text,
)
from sqlalchemy.orm import relationship
from backend.app.database import Base


def generate_uuid() -> str:
    return str(uuid.uuid4())


class RoleEnum(str, enum.Enum):
    STUDENT = "student"
    FACULTY = "faculty"
    COLLEGE_ADMIN = "college_admin"


class VerificationStatusEnum(str, enum.Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"


class User(Base):
    __tablename__ = "users"

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    role = Column(Enum(RoleEnum), nullable=False, default=RoleEnum.STUDENT)
    is_active = Column(Boolean, default=True, nullable=False)
    avatar = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Relationships
    student_profile = relationship("StudentProfile", back_populates="user", uselist=False, cascade="all, delete-orphan")
    faculty_profile = relationship("FacultyProfile", back_populates="user", uselist=False, cascade="all, delete-orphan")
    notifications = relationship("Notification", back_populates="user", cascade="all, delete-orphan")
    faculty_follows = relationship("FacultyFollow", foreign_keys="FacultyFollow.student_id", back_populates="student", cascade="all, delete-orphan")
    followers = relationship("FacultyFollow", foreign_keys="FacultyFollow.faculty_id", back_populates="faculty", cascade="all, delete-orphan")


class StudentProfile(Base):
    __tablename__ = "student_profiles"

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    college_id = Column(String(36), ForeignKey("colleges.id", ondelete="SET NULL"), nullable=True, index=True)
    branch = Column(String(100), nullable=False)  # e.g., 'ECE', 'CSE'
    academic_year = Column(String(50), nullable=False)  # e.g., '3rd Year'
    section = Column(String(50), nullable=False)  # e.g., 'A'
    roll_number = Column(String(100), nullable=True)
    phone = Column(String(20), nullable=True)
    target_exam = Column(String(100), nullable=True)  # e.g., 'GATE', 'Placement', 'UPSC'
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Relationships
    user = relationship("User", back_populates="student_profile")
    college = relationship("College", back_populates="students")
    quiz_attempts = relationship("QuizAttempt", back_populates="student", cascade="all, delete-orphan")
    assignment_submissions = relationship("AssignmentSubmission", back_populates="student", cascade="all, delete-orphan")
    coding_submissions = relationship("CodingSubmission", back_populates="student", cascade="all, delete-orphan")
    progress_records = relationship("StudentProgress", back_populates="student", cascade="all, delete-orphan")


class FacultyProfile(Base):
    __tablename__ = "faculty_profiles"

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    college_id = Column(String(36), ForeignKey("colleges.id", ondelete="SET NULL"), nullable=True, index=True)
    department = Column(String(100), nullable=False)  # e.g., 'ECE'
    designation = Column(String(100), nullable=False, default="Assistant Professor")
    office_room = Column(String(100), nullable=True)
    subjects_taught = Column(JSON, default=list, nullable=False)  # List of string subject names
    verification_status = Column(Enum(VerificationStatusEnum), default=VerificationStatusEnum.PENDING, nullable=False, index=True)
    bio = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Relationships
    user = relationship("User", back_populates="faculty_profile")
    college = relationship("College", back_populates="faculty_members")
    notes = relationship("FacultyNote", back_populates="faculty", cascade="all, delete-orphan")
    pdf_notes = relationship("PDFNote", back_populates="faculty", cascade="all, delete-orphan")
    videos = relationship("FacultyVideo", back_populates="faculty", cascade="all, delete-orphan")
    quizzes = relationship("Quiz", back_populates="faculty", cascade="all, delete-orphan")
    assignments = relationship("Assignment", back_populates="faculty", cascade="all, delete-orphan")
    interviews = relationship("Interview", back_populates="faculty", cascade="all, delete-orphan")


class FacultyFollow(Base):
    __tablename__ = "faculty_follows"

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    student_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    faculty_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    student = relationship("User", foreign_keys=[student_id], back_populates="faculty_follows")
    faculty = relationship("User", foreign_keys=[faculty_id], back_populates="followers")
