import enum
import uuid
from datetime import datetime
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Float,
    ForeignKey,
    Index,
    Integer,
    JSON,
    String,
    Text,
)
from sqlalchemy.orm import relationship
from backend.app.database import Base


def generate_uuid() -> str:
    return str(uuid.uuid4())


class AptitudeDifficultyEnum(str, enum.Enum):
    EASY = "Easy"
    INTERMEDIATE = "Intermediate"
    ADVANCED = "Advanced"


class AptitudeAttemptStatusEnum(str, enum.Enum):
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    ABANDONED = "abandoned"


class AptitudeTestAttempt(Base):
    """
    Represents an LLM-generated aptitude test attempt created by a student.
    Contains overall configuration, timing, scoring, and metadata.
    """
    __tablename__ = "aptitude_test_attempts"

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)

    category = Column(String(100), nullable=False, index=True)  # e.g., 'Quantitative Aptitude', 'Logical Reasoning', 'Mixed'
    topic = Column(String(100), nullable=False, index=True)     # e.g., 'Percentages', 'Mixed Topics'
    difficulty = Column(String(50), default="Intermediate", nullable=False, index=True)
    test_mode = Column(String(50), default="standard", nullable=False)  # 'quick', 'standard', 'full', 'custom'

    question_count = Column(Integer, default=10, nullable=False)
    duration_minutes = Column(Integer, default=15, nullable=False)
    status = Column(String(50), default="in_progress", nullable=False, index=True)

    total_marks = Column(Float, default=10.0, nullable=False)
    marks_obtained = Column(Float, default=0.0, nullable=False)
    negative_marks_per_question = Column(Float, default=0.25, nullable=False)
    total_negative_marks = Column(Float, default=0.0, nullable=False)
    final_score = Column(Float, default=0.0, nullable=False)
    accuracy_percentage = Column(Float, default=0.0, nullable=False)

    correct_count = Column(Integer, default=0, nullable=False)
    incorrect_count = Column(Integer, default=0, nullable=False)
    unattempted_count = Column(Integer, default=0, nullable=False)
    time_spent_seconds = Column(Integer, default=0, nullable=False)

    llm_provider = Column(String(50), default="deterministic", nullable=False)
    llm_model = Column(String(100), nullable=True)

    started_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    submitted_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Relationships
    user = relationship("User", foreign_keys=[user_id])
    questions = relationship(
        "AptitudeTestQuestion",
        back_populates="attempt",
        cascade="all, delete-orphan",
        order_by="AptitudeTestQuestion.order_index",
    )
    responses = relationship(
        "AptitudeTestResponse",
        back_populates="attempt",
        cascade="all, delete-orphan",
    )

    __table_args__ = (
        Index("idx_aptitude_attempt_user_status", "user_id", "status"),
        Index("idx_aptitude_attempt_category", "category", "difficulty"),
    )


class AptitudeTestQuestion(Base):
    """
    Stores an individual question generated for a test attempt.
    The correct_answer and explanation are strictly retained on the backend until submission.
    """
    __tablename__ = "aptitude_test_questions"

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    attempt_id = Column(String(36), ForeignKey("aptitude_test_attempts.id", ondelete="CASCADE"), nullable=False, index=True)

    order_index = Column(Integer, default=0, nullable=False)
    question_text = Column(Text, nullable=False)
    options = Column(JSON, nullable=False)  # List of dicts: [{"id": "A", "text": "₹880"}, ...]
    correct_answer = Column(String(10), nullable=False)  # 'A', 'B', 'C', 'D' (Never returned prior to submit)
    explanation = Column(Text, nullable=False)           # Detailed explanation (Never returned prior to submit)

    category = Column(String(100), nullable=False, index=True)
    topic = Column(String(100), nullable=False, index=True)
    difficulty = Column(String(50), nullable=False)
    marks = Column(Float, default=1.0, nullable=False)
    negative_marks = Column(Float, default=0.25, nullable=False)
    question_hash = Column(String(64), nullable=True, index=True)  # Normalized fingerprint for duplicate detection

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    attempt = relationship("AptitudeTestAttempt", back_populates="questions")
    responses = relationship("AptitudeTestResponse", back_populates="question", cascade="all, delete-orphan")


class AptitudeTestResponse(Base):
    """
    Stores a student's answer selection and grading outcome for a question in an attempt.
    """
    __tablename__ = "aptitude_test_responses"

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    attempt_id = Column(String(36), ForeignKey("aptitude_test_attempts.id", ondelete="CASCADE"), nullable=False, index=True)
    question_id = Column(String(36), ForeignKey("aptitude_test_questions.id", ondelete="CASCADE"), nullable=False, index=True)

    selected_option = Column(String(10), nullable=True)  # 'A', 'B', 'C', 'D', or None
    is_correct = Column(Boolean, nullable=True)
    marks_awarded = Column(Float, default=0.0, nullable=False)
    time_spent_seconds = Column(Integer, default=0, nullable=False)
    answered_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    attempt = relationship("AptitudeTestAttempt", back_populates="responses")
    question = relationship("AptitudeTestQuestion", back_populates="responses")

    __table_args__ = (
        Index("idx_aptitude_resp_attempt_q", "attempt_id", "question_id", unique=True),
    )
