import enum
import uuid
from datetime import datetime
from typing import Optional
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


class LiveInterviewCategoryEnum(str, enum.Enum):
    TECHNICAL = "Technical Interview"
    HR = "HR Interview"
    PYTHON = "Python Interview"
    C = "C Interview"
    CPP = "C++ Interview"
    JAVA = "Java Interview"
    DSA = "DSA Interview"
    SQL_DBMS = "SQL and DBMS Interview"
    ENGINEERING = "Engineering Subjects"
    CUSTOM = "Custom Interview"


class LiveInterviewStatusEnum(str, enum.Enum):
    SCHEDULED = "Scheduled"
    CONFIRMED = "Confirmed"
    CANCELLED = "Cancelled"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    NO_SHOW = "No Show"


class LiveRoomStatusEnum(str, enum.Enum):
    WAITING = "WAITING"
    ACTIVE = "ACTIVE"
    ENDED = "ENDED"
    EXPIRED = "EXPIRED"


class ParticipantRoleEnum(str, enum.Enum):
    TEACHER = "teacher"
    STUDENT = "student"
    ADMIN = "admin"


class LiveInterviewBooking(Base):
    """
    Section 10: Interview Bookings entity.
    Stores human-to-human interview scheduling between a Teacher and a Student.
    """
    __tablename__ = "live_interview_bookings"

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    student_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    teacher_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    college_id = Column(String(36), ForeignKey("colleges.id", ondelete="SET NULL"), nullable=True, index=True)

    interview_category = Column(Enum(LiveInterviewCategoryEnum), default=LiveInterviewCategoryEnum.TECHNICAL, nullable=False, index=True)
    subject = Column(String(150), nullable=False)
    scheduled_at = Column(DateTime, nullable=False, index=True)
    duration_minutes = Column(Integer, default=45, nullable=False)
    instructions = Column(Text, nullable=True)
    preparation_materials = Column(Text, nullable=True)
    booking_status = Column(Enum(LiveInterviewStatusEnum), default=LiveInterviewStatusEnum.SCHEDULED, nullable=False, index=True)

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Relationships
    student = relationship("User", foreign_keys=[student_id])
    teacher = relationship("User", foreign_keys=[teacher_id])
    room = relationship("LiveMeetingRoom", back_populates="booking", uselist=False, cascade="all, delete-orphan")
    feedback = relationship("LiveInterviewFeedback", back_populates="booking", uselist=False, cascade="all, delete-orphan")


class LiveMeetingRoom(Base):
    """
    Section 10: Meeting Rooms entity.
    Maintains secure, unpredictable room identifiers and room lifecycle.
    """
    __tablename__ = "live_meeting_rooms"

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    booking_id = Column(String(36), ForeignKey("live_interview_bookings.id", ondelete="CASCADE"), unique=True, nullable=False)
    secure_room_id = Column(String(100), unique=True, nullable=False, index=True)  # e.g. 'live-meet-xxxx-xxxx'

    room_status = Column(Enum(LiveRoomStatusEnum), default=LiveRoomStatusEnum.WAITING, nullable=False, index=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    started_at = Column(DateTime, nullable=True)
    ended_at = Column(DateTime, nullable=True)
    expires_at = Column(DateTime, nullable=True)

    # Relationships
    booking = relationship("LiveInterviewBooking", back_populates="room")
    participants = relationship("LiveMeetingParticipant", back_populates="room", cascade="all, delete-orphan")
    chat_messages = relationship("LiveMeetingChatMessage", back_populates="room", cascade="all, delete-orphan", order_by="LiveMeetingChatMessage.created_at")


class LiveMeetingParticipant(Base):
    """
    Section 10: Meeting Participants entity.
    Tracks attendance, join/leave timestamps, and connection status for auditability.
    """
    __tablename__ = "live_meeting_participants"

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    room_id = Column(String(36), ForeignKey("live_meeting_rooms.id", ondelete="CASCADE"), nullable=False, index=True)
    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    role = Column(Enum(ParticipantRoleEnum), nullable=False)

    join_time = Column(DateTime, default=datetime.utcnow, nullable=False)
    leave_time = Column(DateTime, nullable=True)
    connection_status = Column(String(50), default="CONNECTED", nullable=False)  # 'CONNECTED', 'DISCONNECTED', 'LEFT'

    # Relationships
    room = relationship("LiveMeetingRoom", back_populates="participants")
    user = relationship("User")


class LiveMeetingChatMessage(Base):
    """
    Section 10: Meeting Chat Messages entity.
    Stores in-meeting text messages chronologically.
    """
    __tablename__ = "live_meeting_chat_messages"

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    room_id = Column(String(36), ForeignKey("live_meeting_rooms.id", ondelete="CASCADE"), nullable=False, index=True)
    sender_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    message_content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False, index=True)

    # Relationships
    room = relationship("LiveMeetingRoom", back_populates="chat_messages")
    sender = relationship("User")


class LiveInterviewFeedback(Base):
    """
    Section 10: Interview Feedback entity.
    Stores comprehensive human evaluator ratings, qualitative feedback, and recommendations.
    """
    __tablename__ = "live_interview_feedback"

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    booking_id = Column(String(36), ForeignKey("live_interview_bookings.id", ondelete="CASCADE"), unique=True, nullable=False)
    teacher_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)

    technical_score = Column(Float, nullable=False)  # 0 to 100
    communication_feedback = Column(Text, nullable=False)
    problem_solving_feedback = Column(Text, nullable=False)
    strengths = Column(JSON, default=list, nullable=False)
    areas_for_improvement = Column(JSON, default=list, nullable=False)
    teacher_comments = Column(Text, nullable=True)
    recommended_topics = Column(JSON, default=list, nullable=False)

    submitted_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    booking = relationship("LiveInterviewBooking", back_populates="feedback")
    teacher = relationship("User", foreign_keys=[teacher_id])
