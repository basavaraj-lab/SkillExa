import enum
import uuid
from datetime import datetime
from sqlalchemy import (
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
from backend.app.models.quiz import DifficultyEnum


def generate_uuid() -> str:
    return str(uuid.uuid4())


class SubmissionStatusEnum(str, enum.Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    PASSED = "PASSED"
    FAILED = "FAILED"
    TIMEOUT = "TIMEOUT"
    COMPILATION_ERROR = "COMPILATION_ERROR"
    RUNTIME_ERROR = "RUNTIME_ERROR"
    INTERNAL_ERROR = "INTERNAL_ERROR"


class CodingProblem(Base):
    __tablename__ = "coding_problems"

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    problem_num = Column(Integer, default=1, index=True)
    title = Column(String(255), nullable=False, index=True)
    description = Column(Text, nullable=False)
    
    language = Column(String(50), nullable=False, default="python", index=True)  # 'c', 'cpp', 'java', 'python', 'javascript'
    difficulty = Column(Enum(DifficultyEnum), default=DifficultyEnum.MEDIUM, nullable=False, index=True)
    category = Column(String(100), nullable=False, default="Arrays", index=True)
    topic = Column(String(100), nullable=False, default="Arrays", index=True)  # e.g., 'Arrays', 'Strings', 'Linked List', etc.
    subtopic = Column(String(100), nullable=True)
    
    constraints = Column(Text, nullable=True)
    input_format = Column(Text, nullable=True)
    output_format = Column(Text, nullable=True)
    time_complexity = Column(String(100), nullable=True)
    space_complexity = Column(String(100), nullable=True)
    company_tags = Column(JSON, default=list, nullable=False)
    
    examples = Column(JSON, default=list, nullable=False)  # List of {input, output, explanation}
    starter_code = Column(Text, nullable=False)  # Default/fallback starter code
    starter_code_map = Column(JSON, default=dict, nullable=False)  # {"c": "...", "cpp": "...", "java": "...", "python": "..."}
    solution_code = Column(Text, nullable=True)
    
    # Test cases array: list of {input: str, expected: str, is_hidden: bool}
    test_cases = Column(JSON, default=list, nullable=False)
    hidden_test_cases = Column(JSON, default=list, nullable=False)
    
    points = Column(Integer, default=10, nullable=False)
    order_index = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    submissions = relationship("CodingSubmission", back_populates="problem", cascade="all, delete-orphan")


class CodingSubmission(Base):
    __tablename__ = "coding_submissions"

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    student_id = Column(String(36), ForeignKey("student_profiles.id", ondelete="CASCADE"), nullable=False, index=True)
    problem_id = Column(String(36), ForeignKey("coding_problems.id", ondelete="CASCADE"), nullable=False, index=True)
    
    language = Column(String(50), nullable=False)
    code = Column(Text, nullable=False)
    status = Column(Enum(SubmissionStatusEnum), default=SubmissionStatusEnum.PENDING, nullable=False)
    
    test_cases_passed = Column(Integer, default=0, nullable=False)
    total_test_cases = Column(Integer, default=0, nullable=False)
    runtime_ms = Column(Float, nullable=True)
    memory_kb = Column(Float, nullable=True)
    output_logs = Column(Text, nullable=True)
    error_message = Column(Text, nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    student = relationship("StudentProfile", back_populates="coding_submissions")
    problem = relationship("CodingProblem", back_populates="submissions")
