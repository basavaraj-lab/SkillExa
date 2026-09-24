import enum
import uuid
from datetime import datetime
from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from backend.app.database import Base


def generate_uuid() -> str:
    return str(uuid.uuid4())


class SectionTypeEnum(str, enum.Enum):
    ENGINEERING = "engineering"
    COMPETITIVE = "competitive"
    PROGRAMMING = "programming"
    DSA = "dsa"


class Subject(Base):
    __tablename__ = "subjects"

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    code = Column(String(100), unique=True, nullable=False, index=True)
    name = Column(String(255), nullable=False)
    section = Column(Enum(SectionTypeEnum), nullable=False, index=True)
    category = Column(String(100), nullable=True)  # e.g., 'Core', 'Programming', 'Aptitude'
    icon = Column(String(100), nullable=True)
    description = Column(Text, nullable=True)
    order_index = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    topics = relationship("Topic", back_populates="subject_rel", cascade="all, delete-orphan")


class Topic(Base):
    __tablename__ = "topics"

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    subject_id = Column(String(36), ForeignKey("subjects.id", ondelete="CASCADE"), nullable=False, index=True)
    name = Column(String(255), nullable=False, index=True)
    overview = Column(Text, nullable=True)
    theory = Column(Text, nullable=True)
    order_index = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    subject_rel = relationship("Subject", back_populates="topics")
    subtopics = relationship("Subtopic", back_populates="topic_rel", cascade="all, delete-orphan")


class Subtopic(Base):
    __tablename__ = "subtopics"

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    topic_id = Column(String(36), ForeignKey("topics.id", ondelete="CASCADE"), nullable=False, index=True)
    name = Column(String(255), nullable=False)
    content = Column(Text, nullable=True)
    order_index = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    topic_rel = relationship("Topic", back_populates="subtopics")
