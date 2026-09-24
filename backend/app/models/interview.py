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


class InterviewTypeEnum(str, enum.Enum):
    HR = "HR Interview"
    TECHNICAL = "Technical Interview"
    CODING = "Coding Interview"
    ENGINEERING_VIVA = "Engineering Viva"
    PROJECT_VIVA = "Project Viva"
    PLACEMENT = "Placement Interview"
    CUSTOM = "Custom Interview"


class InterviewStatusEnum(str, enum.Enum):
    SCHEDULED = "Scheduled"
    LIVE = "Live"
    PENDING_EVALUATION = "Pending Evaluation"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"


class Interview(Base):
    __tablename__ = "interviews"

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    faculty_id = Column(String(36), ForeignKey("faculty_profiles.id", ondelete="CASCADE"), nullable=False, index=True)
    student_id = Column(String(36), ForeignKey("student_profiles.id", ondelete="CASCADE"), nullable=False, index=True)
    college_id = Column(String(36), ForeignKey("colleges.id", ondelete="CASCADE"), nullable=True, index=True)

    title = Column(String(255), nullable=False)
    interview_type = Column(Enum(InterviewTypeEnum), default=InterviewTypeEnum.TECHNICAL, nullable=False)
    subject_or_role = Column(String(100), nullable=False)  # e.g., 'Embedded Systems Engineer'
    difficulty = Column(String(50), default="Medium")
    
    scheduled_at = Column(DateTime, nullable=False)
    duration_minutes = Column(Integer, default=30)
    status = Column(Enum(InterviewStatusEnum), default=InterviewStatusEnum.SCHEDULED, nullable=False, index=True)

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Relationships
    faculty = relationship("FacultyProfile", back_populates="interviews")
    student = relationship("StudentProfile")
    questions = relationship("InterviewQuestion", back_populates="interview", cascade="all, delete-orphan", order_by="InterviewQuestion.order_index")
    answers = relationship("InterviewAnswer", back_populates="interview", cascade="all, delete-orphan")
    result = relationship("InterviewResult", back_populates="interview", uselist=False, cascade="all, delete-orphan")
    video_session = relationship("VideoSession", back_populates="interview", uselist=False, cascade="all, delete-orphan")


class InterviewQuestion(Base):
    __tablename__ = "interview_questions"

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    interview_id = Column(String(36), ForeignKey("interviews.id", ondelete="CASCADE"), nullable=False, index=True)
    
    question_text = Column(Text, nullable=False)
    category = Column(String(100), default="Technical")
    marks = Column(Float, default=10.0)
    order_index = Column(Integer, default=0)

    # Relationships
    interview = relationship("Interview", back_populates="questions")


class InterviewAnswer(Base):
    __tablename__ = "interview_answers"

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    interview_id = Column(String(36), ForeignKey("interviews.id", ondelete="CASCADE"), nullable=False, index=True)
    question_id = Column(String(36), ForeignKey("interview_questions.id", ondelete="CASCADE"), nullable=False, index=True)
    
    student_answer = Column(Text, nullable=True)
    notes = Column(Text, nullable=True)

    # Relationships
    interview = relationship("Interview", back_populates="answers")
    question = relationship("InterviewQuestion")


class InterviewResult(Base):
    __tablename__ = "interview_results"

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    interview_id = Column(String(36), ForeignKey("interviews.id", ondelete="CASCADE"), unique=True, nullable=False)
    
    technical_score = Column(Float, default=0.0, nullable=False)
    communication_score = Column(Float, default=0.0, nullable=False)
    confidence_score = Column(Float, default=0.0, nullable=False)
    problem_solving_score = Column(Float, default=0.0, nullable=False)
    overall_score = Column(Float, default=0.0, nullable=False)  # Out of 100
    
    strengths = Column(JSON, default=list, nullable=False)
    weaknesses = Column(JSON, default=list, nullable=False)
    suggestions = Column(JSON, default=list, nullable=False)
    overall_feedback = Column(Text, nullable=False)
    
    evaluated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    interview = relationship("Interview", back_populates="result")


class VideoSession(Base):
    __tablename__ = "video_sessions"

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    interview_id = Column(String(36), ForeignKey("interviews.id", ondelete="CASCADE"), unique=True, nullable=False)
    room_id = Column(String(100), unique=True, nullable=False, index=True)
    
    faculty_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    student_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    
    faculty_joined = Column(Boolean, default=False)
    student_joined = Column(Boolean, default=False)
    session_status = Column(String(50), default="WAITING", nullable=False)  # 'WAITING', 'ACTIVE', 'ENDED'
    
    started_at = Column(DateTime, nullable=True)
    ended_at = Column(DateTime, nullable=True)

    # Relationships
    interview = relationship("Interview", back_populates="video_session")
