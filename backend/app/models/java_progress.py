"""SQLAlchemy ORM model for tracking Java enterprise programming topic and section progress."""
from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime, Float, Integer, String, UniqueConstraint
from app.database.database import Base


class JavaStudentProgress(Base):
    __tablename__ = "java_student_progress"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(String, index=True, nullable=False, default="1")
    topic_id = Column(Integer, index=True, nullable=False)
    
    # Topic Status: LOCKED, IN_PROGRESS, COMPLETED
    status = Column(String, nullable=False, default="LOCKED")
    
    # Current active or next required section: information, examples, programming, fill-blanks, test, completed
    current_section = Column(String, nullable=False, default="information")
    
    # Section completion flags
    information_completed = Column(Boolean, default=False, nullable=False)
    examples_completed = Column(Boolean, default=False, nullable=False)
    programming_completed = Column(Boolean, default=False, nullable=False)
    fill_blanks_completed = Column(Boolean, default=False, nullable=False)
    test_completed = Column(Boolean, default=False, nullable=False)
    
    # Test details & completion
    test_score = Column(Float, default=0.0, nullable=False)
    topic_completed = Column(Boolean, default=False, nullable=False)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    __table_args__ = (
        UniqueConstraint("student_id", "topic_id", name="uq_java_student_topic"),
    )

    def to_dict(self):
        return {
            "id": self.id,
            "student_id": self.student_id,
            "topic_id": self.topic_id,
            "status": self.status,
            "current_section": self.current_section,
            "information_completed": self.information_completed,
            "examples_completed": self.examples_completed,
            "programming_completed": self.programming_completed,
            "fill_blanks_completed": self.fill_blanks_completed,
            "test_completed": self.test_completed,
            "test_score": self.test_score,
            "topic_completed": self.topic_completed,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
