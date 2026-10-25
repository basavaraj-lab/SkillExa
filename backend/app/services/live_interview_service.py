import logging
import uuid
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, List, Optional, Set
from fastapi import HTTPException, WebSocket, WebSocketDisconnect, status
from sqlalchemy import or_, and_
from sqlalchemy.orm import Session

from backend.app.models.live_interview import (
    LiveInterviewBooking,
    LiveInterviewCategoryEnum,
    LiveInterviewFeedback,
    LiveInterviewStatusEnum,
    LiveMeetingChatMessage,
    LiveMeetingParticipant,
    LiveMeetingRoom,
    LiveRoomStatusEnum,
    ParticipantRoleEnum,
)
from backend.app.models.user import RoleEnum, User
from backend.app.schemas.live_interview import (
    CreateLiveInterviewBookingRequest,
    RescheduleLiveInterviewRequest,
    SubmitLiveInterviewFeedbackRequest,
)
from backend.app.services.notification_service import NotificationService
from backend.app.utils.security import decode_access_token

logger = logging.getLogger("skillexa.live_interview")

STUN_SERVERS = [
    {"urls": "stun:stun.l.google.com:19302"},
    {"urls": "stun:stun1.l.google.com:19302"},
    {"urls": "stun:stun2.l.google.com:19302"},
    {"urls": "stun:stun3.l.google.com:19302"},
    {"urls": "stun:stun4.l.google.com:19302"},
]


class LiveInterviewService:
    """
    Core business logic for human-to-human Live Interview bookings,
    room security, participant management, and post-interview feedback.
    """

    @classmethod
    def create_booking(
        cls,
        db: Session,
        teacher: User,
        req: CreateLiveInterviewBookingRequest,
    ) -> LiveInterviewBooking:
        # 1. Authorization: Only faculty and admins can initiate interview bookings
        if teacher.role not in [RoleEnum.FACULTY, RoleEnum.COLLEGE_ADMIN]:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Only authorized teachers or placement trainers can schedule live interviews.",
            )

        # 2. Verify Student
        student = db.query(User).filter(User.id == req.student_id, User.is_active == True).first()
        if not student:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Student account not found or is inactive.",
            )

        if student.role != RoleEnum.STUDENT:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Specified candidate account is not a student.",
            )

        # 3. Schedule Time Validation
        sched_time = req.scheduled_at
        if sched_time.tzinfo is not None:
            sched_time = sched_time.astimezone(timezone.utc).replace(tzinfo=None)

        now = datetime.utcnow()
        if sched_time < now - timedelta(minutes=10):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Interview scheduled time cannot be in the past.",
            )

        new_start = sched_time
        new_end = new_start + timedelta(minutes=req.duration_minutes)

        # 4. Overlap & Scheduling Conflict Check
        # Check active bookings for teacher or student that overlap with proposed window
        active_statuses = [
            LiveInterviewStatusEnum.SCHEDULED,
            LiveInterviewStatusEnum.CONFIRMED,
            LiveInterviewStatusEnum.IN_PROGRESS,
        ]

        conflicts = db.query(LiveInterviewBooking).filter(
            LiveInterviewBooking.booking_status.in_(active_statuses),
            or_(
                LiveInterviewBooking.teacher_id == teacher.id,
                LiveInterviewBooking.student_id == student.id,
            ),
        ).all()

        for b in conflicts:
            b_start = b.scheduled_at
            b_end = b_start + timedelta(minutes=b.duration_minutes)
            if b_start < new_end and b_end > new_start:
                conflicted_role = "Teacher" if b.teacher_id == teacher.id else "Student"
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail=f"Scheduling conflict detected: {conflicted_role} already has an active interview scheduled around this time ({b_start.strftime('%Y-%m-%d %H:%M')}).",
                )

        # 5. Resolve Category Enum safely
        try:
            category_enum = LiveInterviewCategoryEnum(req.interview_category)
        except ValueError:
            category_enum = LiveInterviewCategoryEnum.TECHNICAL

        # 6. Create Booking Record
        college_id = None
        if teacher.faculty_profile and teacher.faculty_profile.college_id:
            college_id = teacher.faculty_profile.college_id
        elif student.student_profile and student.student_profile.college_id:
            college_id = student.student_profile.college_id

        booking = LiveInterviewBooking(
            student_id=student.id,
            teacher_id=teacher.id,
            college_id=college_id,
            interview_category=category_enum,
            subject=req.subject.strip(),
            scheduled_at=sched_time,
            duration_minutes=req.duration_minutes,
            instructions=req.instructions.strip() if req.instructions else None,
            preparation_materials=req.preparation_materials.strip() if req.preparation_materials else None,
            booking_status=LiveInterviewStatusEnum.SCHEDULED,
        )
        db.add(booking)
        db.flush()

        # 7. Create Unique Secure Meeting Room
        secure_room_id = f"live-meet-{uuid.uuid4().hex[:4]}-{uuid.uuid4().hex[:4]}-{uuid.uuid4().hex[:4]}"
        room = LiveMeetingRoom(
            booking_id=booking.id,
            secure_room_id=secure_room_id,
            room_status=LiveRoomStatusEnum.WAITING,
            expires_at=new_end + timedelta(hours=3),  # Room expires 3 hours after scheduled end
        )
        db.add(room)
        db.commit()
        db.refresh(booking)

        # 8. Dispatch notification to student
        try:
            NotificationService.send_notification(
                db=db,
                user_id=student.id,
                notification_type="INTERVIEW_INVITATION",
                title=f"Live Interview Scheduled: {booking.subject}",
                message=f"{teacher.name} scheduled a {booking.interview_category.value} for you on {booking.scheduled_at.strftime('%b %d, %Y at %I:%M %p')}.",
                reference_id=booking.id,
                action_route="/live-interview",
                action_params={"bookingId": booking.id, "roomId": room.secure_room_id},
            )
        except Exception as e:
            logger.warning(f"Could not dispatch notification: {e}")

        return booking

    @classmethod
    def get_user_bookings(
        cls,
        db: Session,
        user: User,
        status_filter: Optional[str] = None,
    ) -> List[LiveInterviewBooking]:
        query = db.query(LiveInterviewBooking)

        if user.role == RoleEnum.STUDENT:
            query = query.filter(LiveInterviewBooking.student_id == user.id)
        elif user.role == RoleEnum.FACULTY:
            query = query.filter(LiveInterviewBooking.teacher_id == user.id)
        # Admin can view all

        if status_filter:
            try:
                st = LiveInterviewStatusEnum(status_filter)
                query = query.filter(LiveInterviewBooking.booking_status == st)
            except ValueError:
                pass

        return query.order_by(LiveInterviewBooking.scheduled_at.desc()).all()

    @classmethod
    def get_booking_by_id(
        cls,
        db: Session,
        booking_id: str,
        user: User,
    ) -> LiveInterviewBooking:
        booking = db.query(LiveInterviewBooking).filter(LiveInterviewBooking.id == booking_id).first()
        if not booking:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Interview booking not found.",
            )

        # Verify access: candidate, interviewer, or admin
        if user.role != RoleEnum.COLLEGE_ADMIN and user.id not in [booking.student_id, booking.teacher_id]:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You are not authorized to view this interview booking.",
            )

        return booking

    @classmethod
    def confirm_booking(
        cls,
        db: Session,
        booking_id: str,
        user: User,
    ) -> LiveInterviewBooking:
        booking = cls.get_booking_by_id(db, booking_id, user)
        if booking.booking_status == LiveInterviewStatusEnum.CANCELLED:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Cannot confirm a cancelled interview booking.",
            )

        booking.booking_status = LiveInterviewStatusEnum.CONFIRMED
        db.commit()
        db.refresh(booking)
        return booking

    @classmethod
    def reschedule_booking(
        cls,
        db: Session,
        booking_id: str,
        user: User,
        req: RescheduleLiveInterviewRequest,
    ) -> LiveInterviewBooking:
        booking = cls.get_booking_by_id(db, booking_id, user)
        # Authorization: only assigned teacher or admin can reschedule
        if user.role != RoleEnum.COLLEGE_ADMIN and user.id != booking.teacher_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Only the interview host or administrator can reschedule this interview.",
            )

        if booking.booking_status in [LiveInterviewStatusEnum.COMPLETED, LiveInterviewStatusEnum.CANCELLED]:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Cannot reschedule an interview that is already {booking.booking_status.value}.",
            )

        sched_time = req.scheduled_at
        if sched_time.tzinfo is not None:
            sched_time = sched_time.astimezone(timezone.utc).replace(tzinfo=None)

        now = datetime.utcnow()
        if sched_time < now - timedelta(minutes=10):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Rescheduled interview start time cannot be in the past.",
            )

        booking.scheduled_at = sched_time
        if req.duration_minutes:
            booking.duration_minutes = req.duration_minutes

        if booking.booking_status == LiveInterviewStatusEnum.CONFIRMED:
            booking.booking_status = LiveInterviewStatusEnum.SCHEDULED

        db.commit()
        db.refresh(booking)

        # Notify student
        try:
            NotificationService.send_notification(
                db=db,
                user_id=booking.student_id,
                notification_type="INTERVIEW_RESCHEDULED",
                title=f"Interview Rescheduled: {booking.subject}",
                message=f"{booking.teacher.name} rescheduled your interview to {booking.scheduled_at.strftime('%b %d, %Y at %I:%M %p')}.",
                reference_id=booking.id,
                action_route="/live-interview",
                action_params={"bookingId": booking.id},
            )
        except Exception:
            pass

        return booking

    @classmethod
    def cancel_booking(
        cls,
        db: Session,
        booking_id: str,
        user: User,
    ) -> LiveInterviewBooking:
        booking = cls.get_booking_by_id(db, booking_id, user)
        if booking.booking_status == LiveInterviewStatusEnum.COMPLETED:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Cannot cancel an already completed interview.",
            )

        booking.booking_status = LiveInterviewStatusEnum.CANCELLED
        if booking.room:
            booking.room.room_status = LiveRoomStatusEnum.ENDED
            booking.room.ended_at = datetime.utcnow()

        db.commit()
        db.refresh(booking)

        # Notify the other participant
        other_user_id = booking.teacher_id if user.id == booking.student_id else booking.student_id
        try:
            NotificationService.send_notification(
                db=db,
                user_id=other_user_id,
                notification_type="INTERVIEW_CANCELLED",
                title=f"Interview Cancelled: {booking.subject}",
                message=f"The scheduled interview on {booking.scheduled_at.strftime('%b %d, %Y')} was cancelled by {user.name}.",
                reference_id=booking.id,
                action_route="/live-interview",
            )
        except Exception:
            pass

        return booking

    @classmethod
    def prepare_or_get_room(
        cls,
        db: Session,
        booking_id: str,
        user: User,
    ) -> LiveMeetingRoom:
        booking = cls.get_booking_by_id(db, booking_id, user)
        if booking.booking_status == LiveInterviewStatusEnum.CANCELLED:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="This interview has been cancelled.",
            )

        room = booking.room
        if not room:
            secure_room_id = f"live-meet-{uuid.uuid4().hex[:4]}-{uuid.uuid4().hex[:4]}-{uuid.uuid4().hex[:4]}"
            room = LiveMeetingRoom(
                booking_id=booking.id,
                secure_room_id=secure_room_id,
                room_status=LiveRoomStatusEnum.WAITING,
                expires_at=booking.scheduled_at + timedelta(minutes=booking.duration_minutes + 180),
            )
            db.add(room)
            db.commit()
            db.refresh(room)

        return room

    @classmethod
    def get_room_by_identifier(
        cls,
        db: Session,
        room_identifier: str,
        user: User,
    ) -> LiveMeetingRoom:
        # Search by secure_room_id or room id
        room = db.query(LiveMeetingRoom).filter(
            or_(
                LiveMeetingRoom.secure_room_id == room_identifier,
                LiveMeetingRoom.id == room_identifier,
            )
        ).first()

        if not room:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Meeting room not found or has been removed.",
            )

        booking = room.booking
        # Authorization check: only assigned student, teacher, or admin can enter
        if user.role != RoleEnum.COLLEGE_ADMIN and user.id not in [booking.student_id, booking.teacher_id]:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Unauthorized: You do not have permission to access this meeting room.",
            )

        return room

    @classmethod
    def join_room(
        cls,
        db: Session,
        room_identifier: str,
        user: User,
    ) -> Dict[str, Any]:
        room = cls.get_room_by_identifier(db, room_identifier, user)
        booking = room.booking

        # Check expiration
        now = datetime.utcnow()
        if room.expires_at and now > room.expires_at:
            room.room_status = LiveRoomStatusEnum.EXPIRED
            db.commit()
            raise HTTPException(
                status_code=status.HTTP_410_GONE,
                detail="Meeting room has expired.",
            )

        if booking.booking_status == LiveInterviewStatusEnum.CANCELLED:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="This interview has been cancelled by the host.",
            )

        if booking.booking_status == LiveInterviewStatusEnum.COMPLETED:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="This interview has already completed.",
            )

        # Determine user role in room
        if user.id == booking.teacher_id:
            role_enum = ParticipantRoleEnum.TEACHER
        elif user.id == booking.student_id:
            role_enum = ParticipantRoleEnum.STUDENT
        else:
            role_enum = ParticipantRoleEnum.ADMIN

        # Check host presence
        host_participant = db.query(LiveMeetingParticipant).filter(
            LiveMeetingParticipant.room_id == room.id,
            LiveMeetingParticipant.user_id == booking.teacher_id,
            LiveMeetingParticipant.connection_status == "CONNECTED",
        ).first()
        host_present = (host_participant is not None) or (role_enum in [ParticipantRoleEnum.TEACHER, ParticipantRoleEnum.ADMIN])

        is_waiting = False
        conn_status = "CONNECTED"

        # If student joins while room is WAITING and host has not started, place in waiting room
        if role_enum == ParticipantRoleEnum.STUDENT and room.room_status == LiveRoomStatusEnum.WAITING:
            is_waiting = True
            conn_status = "WAITING"
        elif role_enum in [ParticipantRoleEnum.TEACHER, ParticipantRoleEnum.ADMIN]:
            room.room_status = LiveRoomStatusEnum.ACTIVE
            if not room.started_at:
                room.started_at = now
            if booking.booking_status in [LiveInterviewStatusEnum.SCHEDULED, LiveInterviewStatusEnum.CONFIRMED]:
                booking.booking_status = LiveInterviewStatusEnum.IN_PROGRESS
            is_waiting = False

        # Record or update participant entry
        participant = db.query(LiveMeetingParticipant).filter(
            LiveMeetingParticipant.room_id == room.id,
            LiveMeetingParticipant.user_id == user.id,
        ).first()

        if not participant:
            participant = LiveMeetingParticipant(
                room_id=room.id,
                user_id=user.id,
                role=role_enum,
                join_time=now,
                connection_status=conn_status,
            )
            db.add(participant)
        else:
            participant.join_time = now
            participant.connection_status = conn_status
            participant.leave_time = None

        db.commit()
        db.refresh(room)

        # Collect active participants list
        participants = (
            db.query(LiveMeetingParticipant)
            .filter(
                LiveMeetingParticipant.room_id == room.id,
                LiveMeetingParticipant.connection_status.in_(["CONNECTED", "WAITING"]),
            )
            .all()
        )

        active_list = []
        for p in participants:
            active_list.append({
                "user_id": p.user_id,
                "name": p.user.name if p.user else "Participant",
                "role": p.role.value,
                "join_time": p.join_time,
                "connection_status": p.connection_status,
            })

        return {
            "room_id": room.id,
            "booking_id": booking.id,
            "secure_room_id": room.secure_room_id,
            "room_status": room.room_status.value,
            "student_id": booking.student_id,
            "student_name": booking.student.name if booking.student else "Student",
            "teacher_id": booking.teacher_id,
            "teacher_name": booking.teacher.name if booking.teacher else "Teacher",
            "interview_category": booking.interview_category.value,
            "subject": booking.subject,
            "scheduled_at": booking.scheduled_at,
            "duration_minutes": booking.duration_minutes,
            "current_user_role": role_enum.value,
            "is_waiting": is_waiting,
            "host_present": host_present,
            "active_participants": active_list,
            "ice_servers": STUN_SERVERS,
        }

    @classmethod
    def admit_student(
        cls,
        db: Session,
        room_identifier: str,
        user: User,
    ) -> Dict[str, Any]:
        room = cls.get_room_by_identifier(db, room_identifier, user)
        booking = room.booking

        if user.role != RoleEnum.COLLEGE_ADMIN and user.id != booking.teacher_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Only the faculty host can admit candidates from the waiting room.",
            )

        now = datetime.utcnow()
        room.room_status = LiveRoomStatusEnum.ACTIVE
        if not room.started_at:
            room.started_at = now
        booking.booking_status = LiveInterviewStatusEnum.IN_PROGRESS

        # Update student participant status to CONNECTED
        student_part = db.query(LiveMeetingParticipant).filter(
            LiveMeetingParticipant.room_id == room.id,
            LiveMeetingParticipant.user_id == booking.student_id,
        ).first()
        if student_part:
            student_part.connection_status = "CONNECTED"

        db.commit()
        db.refresh(room)
        db.refresh(booking)

        return {"room_id": room.id, "secure_room_id": room.secure_room_id, "status": "ADMITTED"}

    @classmethod
    def end_interview(
        cls,
        db: Session,
        room_identifier: str,
        user: User,
    ) -> Dict[str, Any]:
        room = cls.get_room_by_identifier(db, room_identifier, user)
        booking = room.booking

        if user.role != RoleEnum.COLLEGE_ADMIN and user.id != booking.teacher_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Only the faculty host can end the live interview for everyone.",
            )

        now = datetime.utcnow()
        booking.booking_status = LiveInterviewStatusEnum.COMPLETED
        room.room_status = LiveRoomStatusEnum.ENDED
        room.ended_at = now

        # Mark all participants as LEFT
        participants = db.query(LiveMeetingParticipant).filter(
            LiveMeetingParticipant.room_id == room.id,
            LiveMeetingParticipant.connection_status.in_(["CONNECTED", "WAITING"]),
        ).all()
        for p in participants:
            p.connection_status = "LEFT"
            p.leave_time = now

        db.commit()
        db.refresh(booking)
        db.refresh(room)

        return {
            "booking_id": booking.id,
            "room_id": room.id,
            "secure_room_id": room.secure_room_id,
            "status": "COMPLETED",
            "booking_status": "Completed",
            "ended_at": now.isoformat(),
        }

    @classmethod
    def validate_room_code(
        cls,
        db: Session,
        room_code: str,
        user: User,
    ) -> Dict[str, Any]:
        clean_code = room_code.strip()
        room = db.query(LiveMeetingRoom).filter(
            or_(
                LiveMeetingRoom.secure_room_id == clean_code,
                LiveMeetingRoom.id == clean_code,
            )
        ).first()

        if not room:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Interview room code is invalid or does not exist.",
            )

        booking = room.booking
        is_assigned_student = user.id == booking.student_id
        is_assigned_teacher = user.id == booking.teacher_id
        is_admin = user.role == RoleEnum.COLLEGE_ADMIN

        if not (is_assigned_student or is_assigned_teacher or is_admin):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Unauthorized: You are not assigned to this interview room.",
            )

        if booking.booking_status == LiveInterviewStatusEnum.CANCELLED:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="This interview has been cancelled by the host.",
            )

        if booking.booking_status == LiveInterviewStatusEnum.COMPLETED:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="This interview has already completed.",
            )

        return {
            "room_id": room.id,
            "secure_room_id": room.secure_room_id,
            "booking_id": booking.id,
            "subject": booking.subject,
            "interview_category": booking.interview_category.value,
            "scheduled_at": booking.scheduled_at.isoformat(),
            "duration_minutes": booking.duration_minutes,
            "teacher_name": booking.teacher.name if booking.teacher else "Interviewer",
            "student_name": booking.student.name if booking.student else "Candidate",
            "booking_status": booking.booking_status.value,
            "room_status": room.room_status.value,
            "user_role": "teacher" if is_assigned_teacher else ("student" if is_assigned_student else "admin"),
        }

    @classmethod
    def leave_room(
        cls,
        db: Session,
        room_identifier: str,
        user: User,
    ) -> None:
        room = cls.get_room_by_identifier(db, room_identifier, user)
        participant = db.query(LiveMeetingParticipant).filter(
            LiveMeetingParticipant.room_id == room.id,
            LiveMeetingParticipant.user_id == user.id,
        ).first()

        if participant:
            participant.connection_status = "LEFT"
            participant.leave_time = datetime.utcnow()
            db.commit()

    @classmethod
    def get_room_messages(
        cls,
        db: Session,
        room_identifier: str,
        user: User,
    ) -> List[LiveMeetingChatMessage]:
        room = cls.get_room_by_identifier(db, room_identifier, user)
        return (
            db.query(LiveMeetingChatMessage)
            .filter(LiveMeetingChatMessage.room_id == room.id)
            .order_by(LiveMeetingChatMessage.created_at.asc())
            .all()
        )

    @classmethod
    def save_chat_message(
        cls,
        db: Session,
        room_id: str,
        sender_id: str,
        content: str,
    ) -> LiveMeetingChatMessage:
        clean_content = content.strip()[:1000]
        msg = LiveMeetingChatMessage(
            room_id=room_id,
            sender_id=sender_id,
            message_content=clean_content,
        )
        db.add(msg)
        db.commit()
        db.refresh(msg)
        return msg

    @classmethod
    def submit_feedback(
        cls,
        db: Session,
        booking_id: str,
        teacher: User,
        req: SubmitLiveInterviewFeedbackRequest,
    ) -> LiveInterviewFeedback:
        booking = cls.get_booking_by_id(db, booking_id, teacher)

        if teacher.id != booking.teacher_id and teacher.role != RoleEnum.COLLEGE_ADMIN:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Only the interviewer or admin can submit evaluation feedback.",
            )

        existing = db.query(LiveInterviewFeedback).filter(LiveInterviewFeedback.booking_id == booking.id).first()
        if existing:
            existing.technical_score = req.technical_score
            existing.communication_feedback = req.communication_feedback
            existing.problem_solving_feedback = req.problem_solving_feedback
            existing.strengths = req.strengths
            existing.areas_for_improvement = req.areas_for_improvement
            existing.teacher_comments = req.teacher_comments
            existing.recommended_topics = req.recommended_topics
            existing.submitted_at = datetime.utcnow()
            feedback = existing
        else:
            feedback = LiveInterviewFeedback(
                booking_id=booking.id,
                teacher_id=teacher.id,
                technical_score=req.technical_score,
                communication_feedback=req.communication_feedback,
                problem_solving_feedback=req.problem_solving_feedback,
                strengths=req.strengths,
                areas_for_improvement=req.areas_for_improvement,
                teacher_comments=req.teacher_comments,
                recommended_topics=req.recommended_topics,
            )
            db.add(feedback)

        # Mark interview completed
        booking.booking_status = LiveInterviewStatusEnum.COMPLETED
        if booking.room:
            booking.room.room_status = LiveRoomStatusEnum.ENDED
            booking.room.ended_at = datetime.utcnow()

        db.commit()
        db.refresh(feedback)

        # Dispatch notification to student
        try:
            NotificationService.send_notification(
                db=db,
                user_id=booking.student_id,
                notification_type="INTERVIEW_RESULT",
                title=f"Interview Feedback Available: {booking.subject}",
                message=f"{teacher.name} has submitted your interview report. Technical Score: {req.technical_score}/100.",
                reference_id=booking.id,
                action_route="/live-interview",
                action_params={"bookingId": booking.id},
            )
        except Exception:
            pass

        return feedback

    @classmethod
    def get_feedback(
        cls,
        db: Session,
        booking_id: str,
        user: User,
    ) -> LiveInterviewFeedback:
        booking = cls.get_booking_by_id(db, booking_id, user)
        feedback = db.query(LiveInterviewFeedback).filter(LiveInterviewFeedback.booking_id == booking.id).first()
        if not feedback:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Feedback for this interview has not been submitted yet.",
            )
        return feedback


class LiveInterviewSignalingManager:
    """
    Section 5: Real-time WebRTC WebSocket Signaling and in-meeting coordination.
    Handles offer, answer, ICE candidates, chat broadcast, screen-share events,
    and peer presence with token authentication.
    """

    def __init__(self):
        # Mapping: secure_room_id -> Dict[user_id, WebSocket]
        self.rooms: Dict[str, Dict[str, WebSocket]] = {}
        # Mapping: secure_room_id -> Dict[user_id, Dict[str, Any]] (user info like name, role)
        self.user_meta: Dict[str, Dict[str, Dict[str, Any]]] = {}

    async def connect(
        self,
        room_id: str,
        user_id: str,
        user_name: str,
        role: str,
        websocket: WebSocket,
    ):
        await websocket.accept()

        if room_id not in self.rooms:
            self.rooms[room_id] = {}
            self.user_meta[room_id] = {}

        self.rooms[room_id][user_id] = websocket
        self.user_meta[room_id][user_id] = {
            "user_id": user_id,
            "name": user_name,
            "role": role,
            "joined_at": datetime.utcnow().isoformat(),
        }

        # Send welcome/ready message with existing participants in the room
        existing_peers = [
            meta for uid, meta in self.user_meta[room_id].items() if uid != user_id
        ]
        await websocket.send_json({
            "type": "room-joined",
            "user_id": user_id,
            "room_id": room_id,
            "peers": existing_peers,
        })

        # Broadcast peer-joined to all other peers in the room
        await self.broadcast_to_room(
            room_id=room_id,
            message={
                "type": "peer-joined",
                "user_id": user_id,
                "name": user_name,
                "role": role,
            },
            exclude_user_id=user_id,
        )

    def disconnect(self, room_id: str, user_id: str):
        if room_id in self.rooms:
            if user_id in self.rooms[room_id]:
                del self.rooms[room_id][user_id]
            if user_id in self.user_meta[room_id]:
                del self.user_meta[room_id][user_id]

            if len(self.rooms[room_id]) == 0:
                del self.rooms[room_id]
                del self.user_meta[room_id]

    async def broadcast_to_room(
        self,
        room_id: str,
        message: Dict[str, Any],
        exclude_user_id: Optional[str] = None,
    ):
        if room_id not in self.rooms:
            return

        dead_connections = []
        for uid, ws in list(self.rooms[room_id].items()):
            if exclude_user_id and uid == exclude_user_id:
                continue
            try:
                await ws.send_json(message)
            except Exception:
                dead_connections.append(uid)

        for uid in dead_connections:
            self.disconnect(room_id, uid)


live_signaling_manager = LiveInterviewSignalingManager()
