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
from backend.app.models.note import VisibilityEnum


def generate_uuid() -> str:
    return str(uuid.uuid4())


class DifficultyEnum(str, enum.Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


class Quiz(Base):
    __tablename__ = "quizzes"

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    faculty_id = Column(String(36), ForeignKey("faculty_profiles.id", ondelete="CASCADE"), nullable=False, index=True)
    college_id = Column(String(36), ForeignKey("colleges.id", ondelete="CASCADE"), nullable=True, index=True)

    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    
    section = Column(String(50), default="engineering", nullable=False)  # 'engineering' | 'competitive'
    subject = Column(String(100), nullable=False, index=True)
    topic = Column(String(100), nullable=False, index=True)
    subtopic = Column(String(100), nullable=True)
    language = Column(String(50), nullable=True)
    
    difficulty = Column(Enum(DifficultyEnum), default=DifficultyEnum.MEDIUM, nullable=False)
    duration_minutes = Column(Integer, default=15, nullable=False)
    total_marks = Column(Float, default=20.0, nullable=False)
    negative_marks = Column(Float, default=0.25, nullable=False)
    
    visibility = Column(Enum(VisibilityEnum), default=VisibilityEnum.COLLEGE, nullable=False, index=True)
    published = Column(Boolean, default=True, nullable=False, index=True)

    target_departments = Column(JSON, default=list)
    target_years = Column(JSON, default=list)
    target_sections = Column(JSON, default=list)
    target_student_ids = Column(JSON, default=list)

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Relationships
    faculty = relationship("FacultyProfile", back_populates="quizzes")
    questions = relationship("Question", back_populates="quiz", cascade="all, delete-orphan", order_by="Question.order_index")
    attempts = relationship("QuizAttempt", back_populates="quiz", cascade="all, delete-orphan")


class Question(Base):
    __tablename__ = "questions"

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    quiz_id = Column(String(36), ForeignKey("quizzes.id", ondelete="CASCADE"), nullable=True, index=True)
    
    section = Column(String(50), default="engineering", nullable=False, index=True)
    subject = Column(String(100), nullable=False, index=True)
    topic = Column(String(100), nullable=False, index=True)
    subtopic = Column(String(100), nullable=True)
    language = Column(String(50), nullable=True)
    
    difficulty = Column(Enum(DifficultyEnum), default=DifficultyEnum.MEDIUM, nullable=False)
    question_type = Column(String(50), default="mcq")  # 'mcq', 'multiple_choice', 'coding_snippet'
    question_text = Column(Text, nullable=False)
    options = Column(JSON, nullable=False)  # List of string options e.g. ["Option A", "Option B", ...]
    correct_answer = Column(Integer, nullable=False)  # 0-indexed integer of correct option
    explanation = Column(Text, nullable=True)
    marks = Column(Float, default=2.0, nullable=False)
    negative_marks = Column(Float, default=0.5, nullable=False)
    order_index = Column(Integer, default=0, nullable=False)
    
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    quiz = relationship("Quiz", back_populates="questions")


class QuizAttempt(Base):
    __tablename__ = "quiz_attempts"

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    quiz_id = Column(String(36), ForeignKey("quizzes.id", ondelete="CASCADE"), nullable=False, index=True)
    student_id = Column(String(36), ForeignKey("student_profiles.id", ondelete="CASCADE"), nullable=False, index=True)
    
    score = Column(Float, default=0.0, nullable=False)
    total_marks = Column(Float, default=0.0, nullable=False)
    accuracy_percentage = Column(Float, default=0.0, nullable=False)
    
    correct_count = Column(Integer, default=0, nullable=False)
    wrong_count = Column(Integer, default=0, nullable=False)
    unanswered_count = Column(Integer, default=0, nullable=False)
    time_taken_seconds = Column(Integer, default=0, nullable=False)
    
    status = Column(String(50), default="COMPLETED", nullable=False)  # 'IN_PROGRESS', 'COMPLETED'
    started_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    submitted_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    quiz = relationship("Quiz", back_populates="attempts")
    student = relationship("StudentProfile", back_populates="quiz_attempts")
    answers = relationship("QuizAnswer", back_populates="attempt", cascade="all, delete-orphan")


class QuizAnswer(Base):
    __tablename__ = "quiz_answers"

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    attempt_id = Column(String(36), ForeignKey("quiz_attempts.id", ondelete="CASCADE"), nullable=False, index=True)
    question_id = Column(String(36), ForeignKey("questions.id", ondelete="CASCADE"), nullable=False, index=True)
    
    selected_option = Column(Integer, nullable=True)  # None if unanswered
    is_correct = Column(Boolean, default=False, nullable=False)
    time_spent_seconds = Column(Integer, default=0)

    # Relationships
    attempt = relationship("QuizAttempt", back_populates="answers")
    question = relationship("Question")
