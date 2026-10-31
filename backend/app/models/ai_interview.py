import enum
import uuid
from datetime import datetime, timezone
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Enum,
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


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class InterviewCategoryEnum(str, enum.Enum):
    TECHNICAL = "Technical"
    HR = "HR"
    BEHAVIORAL = "Behavioral"

    @classmethod
    def _missing_(cls, value):
        if isinstance(value, str):
            val_clean = value.strip().lower()
            for member in cls:
                if member.value.lower() == val_clean or member.name.lower() == val_clean:
                    return member
        return cls.TECHNICAL


class InterviewDifficultyEnum(str, enum.Enum):
    BEGINNER = "Beginner"
    INTERMEDIATE = "Intermediate"
    ADVANCED = "Advanced"
    MEDIUM = "Medium"
    EASY = "Easy"
    HARD = "Hard"

    @classmethod
    def _missing_(cls, value):
        if isinstance(value, str):
            val_clean = value.strip().lower()
            if val_clean in ["medium", "intermediate"]:
                return cls.INTERMEDIATE
            if val_clean in ["easy", "beginner", "basic"]:
                return cls.BEGINNER
            if val_clean in ["hard", "advanced", "expert"]:
                return cls.ADVANCED
            for member in cls:
                if member.value.lower() == val_clean or member.name.lower() == val_clean:
                    return member
        return cls.INTERMEDIATE


class ExperienceLevelEnum(str, enum.Enum):
    STUDENT = "Student"
    FRESHER = "Fresher"
    EXPERIENCED = "Experienced"

    @classmethod
    def _missing_(cls, value):
        if isinstance(value, str):
            val_clean = value.strip().lower()
            for member in cls:
                if member.value.lower() == val_clean or member.name.lower() == val_clean:
                    return member
        return cls.STUDENT


class InterviewModeEnum(str, enum.Enum):
    TEXT = "text"
    VOICE = "voice"
    VOICE_TEXT = "voice_text"

    @classmethod
    def _missing_(cls, value):
        if isinstance(value, str):
            val_clean = value.strip().lower()
            if "voice" in val_clean:
                return cls.VOICE
            return cls.TEXT
        return cls.TEXT


class SessionStatusEnum(str, enum.Enum):
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    INTERRUPTED = "interrupted"


class EvaluationStatusEnum(str, enum.Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"


class QuestionValidationStatusEnum(str, enum.Enum):
    VERIFIED = "verified"
    PENDING = "pending"
    REJECTED = "rejected"


class AIQuestionBank(Base):
    """
    Reusable Question Bank supporting Predefined, AI-generated, and MediaWiki-backed questions.
    """
    __tablename__ = "ai_interview_question_banks"

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    category = Column(Enum(InterviewCategoryEnum), default=InterviewCategoryEnum.TECHNICAL, nullable=False, index=True)
    subject = Column(String(100), nullable=False, index=True)  # e.g., 'Python', 'Operating Systems', 'HR'
    programming_language = Column(String(50), nullable=True, index=True)  # e.g., 'Python', 'C++', 'Java'
    job_role = Column(String(100), nullable=True, index=True)  # e.g., 'Software Developer'
    difficulty = Column(Enum(InterviewDifficultyEnum), default=InterviewDifficultyEnum.INTERMEDIATE, nullable=False, index=True)
    experience_level = Column(Enum(ExperienceLevelEnum), default=ExperienceLevelEnum.STUDENT, nullable=False)

    question_text = Column(Text, nullable=False)
    expected_concepts = Column(JSON, default=list, nullable=False)  # List of required conceptual keywords/ideas
    evaluation_criteria = Column(JSON, default=dict, nullable=False)  # Rubric definition
    sample_answer = Column(Text, nullable=True)
    hints = Column(JSON, default=list, nullable=False)

    question_source = Column(String(50), default="predefined", nullable=False)  # 'predefined', 'ai_generated', 'wikipedia_backed'
    source_reference = Column(String(255), nullable=True)  # Source article or citation url
    created_by = Column(String(36), nullable=True)  # Admin/Faculty User ID or 'system'
    validation_status = Column(Enum(QuestionValidationStatusEnum), default=QuestionValidationStatusEnum.VERIFIED, nullable=False, index=True)
    is_active = Column(Boolean, default=True, nullable=False, index=True)

    created_at = Column(DateTime, default=utc_now, nullable=False)
    updated_at = Column(DateTime, default=utc_now, onupdate=utc_now, nullable=False)

    __table_args__ = (
        Index("idx_qbank_lookup", "category", "subject", "difficulty", "is_active"),
    )


class AIInterviewSession(Base):
    """
    Student AI Mock Interview Session instance.
    """
    __tablename__ = "ai_interview_sessions"

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)

    interview_category = Column(Enum(InterviewCategoryEnum), default=InterviewCategoryEnum.TECHNICAL, nullable=False)
    job_role = Column(String(100), default="Software Developer", nullable=False)
    subject = Column(String(100), nullable=False)
    programming_language = Column(String(50), nullable=True)
    difficulty = Column(Enum(InterviewDifficultyEnum), default=InterviewDifficultyEnum.INTERMEDIATE, nullable=False)
    experience_level = Column(Enum(ExperienceLevelEnum), default=ExperienceLevelEnum.STUDENT, nullable=False)
    interview_mode = Column(Enum(InterviewModeEnum), default=InterviewModeEnum.TEXT, nullable=False)
    preferred_language = Column(String(20), default="English", nullable=False)
    duration_minutes = Column(Integer, default=30, nullable=False)

    status = Column(Enum(SessionStatusEnum), default=SessionStatusEnum.IN_PROGRESS, nullable=False, index=True)
    started_at = Column(DateTime, default=utc_now, nullable=False)
    completed_at = Column(DateTime, nullable=True)

    total_questions = Column(Integer, default=5, nullable=False)
    questions_answered = Column(Integer, default=0, nullable=False)
    total_score = Column(Float, default=0.0, nullable=False)  # Overall normalized percentage 0.0 - 100.0

    created_at = Column(DateTime, default=utc_now, nullable=False)
    updated_at = Column(DateTime, default=utc_now, onupdate=utc_now, nullable=False)

    # Relationships
    user = relationship("User")
    questions = relationship("AIInterviewQuestion", back_populates="interview", cascade="all, delete-orphan", order_by="AIInterviewQuestion.question_number")
    report = relationship("AIInterviewReport", back_populates="interview", uselist=False, cascade="all, delete-orphan")


class AIInterviewQuestion(Base):
    """
    Snapshot of questions presented during a student interview.
    Preserves exact historical question context and scoring rubric.
    """
    __tablename__ = "ai_interview_questions"

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    interview_id = Column(String(36), ForeignKey("ai_interview_sessions.id", ondelete="CASCADE"), nullable=False, index=True)
    question_bank_id = Column(String(36), ForeignKey("ai_interview_question_banks.id", ondelete="SET NULL"), nullable=True, index=True)

    question_number = Column(Integer, nullable=False)
    question_text = Column(Text, nullable=False)
    topic = Column(String(100), nullable=False)
    difficulty = Column(String(50), default="Intermediate", nullable=False)

    expected_concepts = Column(JSON, default=list, nullable=False)
    evaluation_criteria = Column(JSON, default=dict, nullable=False)
    question_source = Column(String(50), default="predefined", nullable=False)
    source_reference = Column(String(255), nullable=True)

    generated_follow_up = Column(Boolean, default=False, nullable=False)
    parent_question_id = Column(String(36), nullable=True)
    asked_at = Column(DateTime, default=utc_now, nullable=False)

    # Relationships
    interview = relationship("AIInterviewSession", back_populates="questions")
    question_bank_item = relationship("AIQuestionBank")
    answer = relationship("AIInterviewAnswer", back_populates="question", uselist=False, cascade="all, delete-orphan")


class AIInterviewAnswer(Base):
    """
    Student submitted answer (text or voice transcript) with multi-criteria evaluation.
    """
    __tablename__ = "ai_interview_answers"

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    interview_question_id = Column(String(36), ForeignKey("ai_interview_questions.id", ondelete="CASCADE"), unique=True, nullable=False)

    answer_text = Column(Text, nullable=False)
    answer_mode = Column(Enum(InterviewModeEnum), default=InterviewModeEnum.TEXT, nullable=False)
    audio_url = Column(String(255), nullable=True)  # Optional audio path if voice answer retained

    submitted_at = Column(DateTime, default=utc_now, nullable=False)

    # Evaluation Scores (Scale 0.0 to 10.0)
    technical_score = Column(Float, nullable=True)
    completeness_score = Column(Float, nullable=True)
    clarity_score = Column(Float, nullable=True)
    communication_score = Column(Float, nullable=True)

    feedback = Column(Text, nullable=True)
    strengths = Column(JSON, default=list, nullable=True)
    improvement_areas = Column(JSON, default=list, nullable=True)
    missing_concepts = Column(JSON, default=list, nullable=True)
    model_answer = Column(Text, nullable=True)
    speech_metrics = Column(JSON, default=dict, nullable=True)  # WPM, pause count, duration (voice mode)

    evaluation_status = Column(Enum(EvaluationStatusEnum), default=EvaluationStatusEnum.PENDING, nullable=False, index=True)

    # Relationships
    question = relationship("AIInterviewQuestion", back_populates="answer")


class AIInterviewReport(Base):
    """
    Final comprehensive interview report generated upon completion.
    """
    __tablename__ = "ai_interview_reports"

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    interview_id = Column(String(36), ForeignKey("ai_interview_sessions.id", ondelete="CASCADE"), unique=True, nullable=False)

    overall_score = Column(Float, default=0.0, nullable=False)  # Scaled 0.0 to 100.0
    technical_summary = Column(Text, nullable=False)
    communication_summary = Column(Text, nullable=False)

    strengths = Column(JSON, default=list, nullable=False)
    improvement_areas = Column(JSON, default=list, nullable=False)
    recommended_topics = Column(JSON, default=list, nullable=False)
    final_feedback = Column(Text, nullable=False)

    generated_at = Column(DateTime, default=utc_now, nullable=False)

    # Relationships
    interview = relationship("AIInterviewSession", back_populates="report")


class EducationalKnowledgeSource(Base):
    """
    Attributed educational references retrieved via MediaWiki (Wikipedia) API.
    """
    __tablename__ = "educational_knowledge_sources"

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    source_name = Column(String(100), default="Wikipedia", nullable=False)
    article_title = Column(String(255), nullable=False, index=True)
    source_url = Column(String(500), nullable=False)
    retrieved_at = Column(DateTime, default=utc_now, nullable=False)
    content_summary = Column(Text, nullable=False)
    attribution = Column(String(500), nullable=False)
    review_status = Column(String(50), default="verified", nullable=False)
