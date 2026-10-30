import uuid
from datetime import datetime
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    JSON,
    String,
    Text,
)
from sqlalchemy.orm import relationship
from backend.app.database import Base


def generate_uuid() -> str:
    return str(uuid.uuid4())


class AIProject(Base):
    __tablename__ = "ai_projects"

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    student_id = Column(String(36), nullable=False, index=True, default="guest_student")
    name = Column(String(120), nullable=False, index=True)
    description = Column(Text, nullable=True)
    icon = Column(String(50), nullable=False, default="folder")
    context_prompt = Column(Text, nullable=True)
    is_pinned = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Relationships
    conversations = relationship(
        "AIConversation",
        back_populates="project",
        cascade="all, delete-orphan",
        order_by="desc(AIConversation.updated_at)",
    )
    memory = relationship(
        "AIProjectMemory",
        back_populates="project",
        uselist=False,
        cascade="all, delete-orphan",
    )


class AIConversation(Base):
    __tablename__ = "ai_conversations"

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    project_id = Column(String(36), ForeignKey("ai_projects.id", ondelete="CASCADE"), nullable=False, index=True)
    student_id = Column(String(36), nullable=False, index=True, default="guest_student")
    title = Column(String(255), nullable=False, default="New Conversation")
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Relationships
    project = relationship("AIProject", back_populates="conversations")
    messages = relationship(
        "AIMessage",
        back_populates="conversation",
        cascade="all, delete-orphan",
        order_by="AIMessage.created_at",
    )


class AIMessage(Base):
    __tablename__ = "ai_messages"

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    conversation_id = Column(String(36), ForeignKey("ai_conversations.id", ondelete="CASCADE"), nullable=False, index=True)
    sender_type = Column(String(20), nullable=False, default="user")  # 'user', 'assistant', 'system'
    message_text = Column(Text, nullable=False)
    input_type = Column(String(20), nullable=False, default="text")    # 'text', 'voice'
    search_sources = Column(JSON, default=list)                         # [{'title': ..., 'url': ..., 'snippet': ...}]
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    conversation = relationship("AIConversation", back_populates="messages")


class AIProjectMemory(Base):
    __tablename__ = "ai_project_memories"

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    project_id = Column(String(36), ForeignKey("ai_projects.id", ondelete="CASCADE"), unique=True, nullable=False, index=True)
    memory_summary = Column(Text, nullable=False, default="")
    key_entities = Column(JSON, default=dict)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Relationships
    project = relationship("AIProject", back_populates="memory")

