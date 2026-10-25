import json
import logging
from typing import List, Optional
from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Query,
    WebSocket,
    WebSocketDisconnect,
    status,
)
from sqlalchemy.orm import Session

from backend.app.database import SessionLocal
from backend.app.dependencies.auth import get_current_user
from backend.app.dependencies.db import get_db
from backend.app.models.user import RoleEnum, User
from backend.app.schemas.common import ApiResponse
from backend.app.schemas.live_interview import (
    CreateLiveInterviewBookingRequest,
    LiveInterviewBookingResponse,
    LiveInterviewFeedbackResponse,
    LiveMeetingChatMessageRequest,
    LiveMeetingChatMessageResponse,
    LiveMeetingRoomResponse,
    RescheduleLiveInterviewRequest,
    SubmitLiveInterviewFeedbackRequest,
)
from backend.app.services.live_interview_service import (
    LiveInterviewService,
    live_signaling_manager,
)
from backend.app.utils.security import decode_access_token

logger = logging.getLogger("skillexa.routers.live_interview")

router = APIRouter(prefix="/live-interview", tags=["SkillExa Live Interview (Human-to-Human)"])


def _format_booking_response(b) -> LiveInterviewBookingResponse:
    return LiveInterviewBookingResponse(
        id=b.id,
        student_id=b.student_id,
        student_name=b.student.name if b.student else "Student",
        student_email=b.student.email if b.student else "",
        teacher_id=b.teacher_id,
        teacher_name=b.teacher.name if b.teacher else "Teacher",
        teacher_email=b.teacher.email if b.teacher else "",
        college_id=b.college_id,
        interview_category=b.interview_category.value if hasattr(b.interview_category, "value") else str(b.interview_category),
        subject=b.subject,
        scheduled_at=b.scheduled_at,
        duration_minutes=b.duration_minutes,
        instructions=b.instructions,
        preparation_materials=b.preparation_materials,
        booking_status=b.booking_status.value if hasattr(b.booking_status, "value") else str(b.booking_status),
        room_id=b.room.id if b.room else None,
        secure_room_id=b.room.secure_room_id if b.room else None,
        has_feedback=b.feedback is not None,
        created_at=b.created_at,
    )


# -----------------------------------------------------------------------------
# 1. Bookings Management
# -----------------------------------------------------------------------------
@router.post("/bookings", response_model=ApiResponse[LiveInterviewBookingResponse], status_code=status.HTTP_201_CREATED)
def create_interview_booking(
    req: CreateLiveInterviewBookingRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Teacher or Placement Trainer schedules a live human-to-human interview with a student.
    Validates times, detects conflicting bookings, generates secure room, and dispatches notification.
    """
    booking = LiveInterviewService.create_booking(db, current_user, req)
    return ApiResponse(
        success=True,
        message="Live interview booked successfully and candidate notified.",
        data=_format_booking_response(booking),
    )


@router.get("/bookings", response_model=ApiResponse[List[LiveInterviewBookingResponse]])
def get_user_interview_bookings(
    status: Optional[str] = Query(None, description="Filter by booking status"),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Retrieve all scheduled, confirmed, or completed interview bookings accessible to the authenticated user.
    """
    bookings = LiveInterviewService.get_user_bookings(db, current_user, status)
    return ApiResponse(
        success=True,
        message="Interview bookings retrieved.",
        data=[_format_booking_response(b) for b in bookings],
    )


@router.get("/bookings/{booking_id}", response_model=ApiResponse[LiveInterviewBookingResponse])
def get_interview_booking_details(
    booking_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Retrieve details of a specific interview booking with authorization check.
    """
    booking = LiveInterviewService.get_booking_by_id(db, booking_id, current_user)
    return ApiResponse(
        success=True,
        message="Booking details retrieved.",
        data=_format_booking_response(booking),
    )


@router.post("/bookings/{booking_id}/confirm", response_model=ApiResponse[LiveInterviewBookingResponse])
def confirm_interview_booking(
    booking_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Confirm an interview booking.
    """
    booking = LiveInterviewService.confirm_booking(db, booking_id, current_user)
    return ApiResponse(
        success=True,
        message="Interview confirmed.",
        data=_format_booking_response(booking),
    )


@router.post("/bookings/{booking_id}/cancel", response_model=ApiResponse[LiveInterviewBookingResponse])
def cancel_interview_booking(
    booking_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Cancel an interview booking and release the meeting room.
    """
    booking = LiveInterviewService.cancel_booking(db, booking_id, current_user)
    return ApiResponse(
        success=True,
        message="Interview cancelled.",
        data=_format_booking_response(booking),
    )


@router.post("/bookings/{booking_id}/reschedule", response_model=ApiResponse[LiveInterviewBookingResponse])
def reschedule_interview_booking(
    booking_id: str,
    req: RescheduleLiveInterviewRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Reschedule an existing live interview booking (Faculty / Admin only).
    """
    booking = LiveInterviewService.reschedule_booking(db, booking_id, current_user, req)
    return ApiResponse(
        success=True,
        message="Interview rescheduled successfully.",
        data=_format_booking_response(booking),
    )


@router.post("/bookings/{booking_id}/room", response_model=ApiResponse[LiveMeetingRoomResponse])
def create_or_prepare_meeting_room(
    booking_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Prepare or create a secure meeting room for an authorized interview booking.
    """
    room = LiveInterviewService.prepare_or_get_room(db, booking_id, current_user)
    join_info = LiveInterviewService.join_room(db, room.secure_room_id, current_user)
    return ApiResponse(
        success=True,
        message="Meeting room ready.",
        data=LiveMeetingRoomResponse.model_validate(join_info),
    )


# -----------------------------------------------------------------------------
# 2. Meeting Room & Real-Time Video Coordination
# -----------------------------------------------------------------------------
@router.get("/validate-room/{room_code}", response_model=ApiResponse[dict])
def validate_interview_room_code(
    room_code: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Validate room code exists, belongs to user, and is eligible to be joined.
    """
    summary = LiveInterviewService.validate_room_code(db, room_code, current_user)
    return ApiResponse(
        success=True,
        message="Room code verified.",
        data=summary,
    )


@router.post("/rooms/{room_id}/join", response_model=ApiResponse[LiveMeetingRoomResponse])
def join_meeting_room(
    room_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Authenticate participant, verify relationship to the interview, record entry, and issue STUN credentials.
    """
    join_info = LiveInterviewService.join_room(db, room_id, current_user)
    return ApiResponse(
        success=True,
        message="Room joined successfully.",
        data=LiveMeetingRoomResponse.model_validate(join_info),
    )


@router.post("/rooms/{room_id}/admit", response_model=ApiResponse[dict])
async def admit_waiting_student(
    room_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Faculty admits the candidate from the waiting room into the active interview room.
    """
    res = LiveInterviewService.admit_student(db, room_id, current_user)
    await live_signaling_manager.broadcast_to_room(
        room_id=room_id,
        message={"type": "student-admitted"},
    )
    return ApiResponse(
        success=True,
        message="Candidate admitted to live interview.",
        data=res,
    )


@router.post("/rooms/{room_id}/end", response_model=ApiResponse[dict])
async def end_meeting_room_for_all(
    room_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Faculty concludes the interview for all participants, terminates signaling, and records completion.
    """
    res = LiveInterviewService.end_interview(db, room_id, current_user)
    await live_signaling_manager.broadcast_to_room(
        room_id=room_id,
        message={"type": "interview-ended", "by": current_user.name},
    )
    return ApiResponse(
        success=True,
        message="Interview ended for all participants.",
        data=res,
    )


@router.post("/rooms/{room_id}/leave", response_model=ApiResponse[dict])
def leave_meeting_room(
    room_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Record participant departure and release resources.
    """
    LiveInterviewService.leave_room(db, room_id, current_user)
    return ApiResponse(
        success=True,
        message="Left meeting room.",
        data={"room_id": room_id, "status": "LEFT"},
    )


@router.get("/rooms/{room_id}", response_model=ApiResponse[LiveMeetingRoomResponse])
def get_meeting_room_status(
    room_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Retrieve authorized room metadata and active participant statuses.
    """
    join_info = LiveInterviewService.join_room(db, room_id, current_user)
    return ApiResponse(
        success=True,
        message="Room status retrieved.",
        data=LiveMeetingRoomResponse.model_validate(join_info),
    )


@router.get("/rooms/{room_id}/messages", response_model=ApiResponse[List[LiveMeetingChatMessageResponse]])
def get_room_chat_messages(
    room_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Retrieve chronological in-meeting chat history for authorized participants.
    """
    messages = LiveInterviewService.get_room_messages(db, room_id, current_user)
    res = [
        LiveMeetingChatMessageResponse(
            id=m.id,
            room_id=m.room_id,
            sender_id=m.sender_id,
            sender_name=m.sender.name if m.sender else "Participant",
            sender_role=m.sender.role.value if m.sender and hasattr(m.sender.role, "value") else "participant",
            message_content=m.message_content,
            created_at=m.created_at,
        )
        for m in messages
    ]
    return ApiResponse(
        success=True,
        message="Chat messages retrieved.",
        data=res,
    )


@router.post("/rooms/{room_id}/messages", response_model=ApiResponse[LiveMeetingChatMessageResponse])
def send_room_chat_message(
    room_id: str,
    req: LiveMeetingChatMessageRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Send and persist an in-meeting chat message.
    """
    # Verify room authorization
    room = LiveInterviewService.get_room_by_identifier(db, room_id, current_user)
    msg = LiveInterviewService.save_chat_message(db, room.id, current_user.id, req.message)
    return ApiResponse(
        success=True,
        message="Message sent.",
        data=LiveMeetingChatMessageResponse(
            id=msg.id,
            room_id=msg.room_id,
            sender_id=msg.sender_id,
            sender_name=current_user.name,
            sender_role=current_user.role.value if hasattr(current_user.role, "value") else str(current_user.role),
            message_content=msg.message_content,
            created_at=msg.created_at,
        ),
    )


# -----------------------------------------------------------------------------
# 3. Interview Feedback & Evaluation Reports
# -----------------------------------------------------------------------------
@router.post("/bookings/{booking_id}/feedback", response_model=ApiResponse[LiveInterviewFeedbackResponse])
def submit_interview_feedback(
    booking_id: str,
    req: SubmitLiveInterviewFeedbackRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Teacher submits structured post-interview evaluation report and score.
    """
    fb = LiveInterviewService.submit_feedback(db, booking_id, current_user, req)
    return ApiResponse(
        success=True,
        message="Interview feedback and evaluation report submitted successfully.",
        data=LiveInterviewFeedbackResponse(
            id=fb.id,
            booking_id=fb.booking_id,
            teacher_id=fb.teacher_id,
            teacher_name=fb.teacher.name if fb.teacher else "Teacher",
            technical_score=fb.technical_score,
            communication_feedback=fb.communication_feedback,
            problem_solving_feedback=fb.problem_solving_feedback,
            strengths=fb.strengths or [],
            areas_for_improvement=fb.areas_for_improvement or [],
            teacher_comments=fb.teacher_comments,
            recommended_topics=fb.recommended_topics or [],
            submitted_at=fb.submitted_at,
        ),
    )


@router.get("/bookings/{booking_id}/feedback", response_model=ApiResponse[LiveInterviewFeedbackResponse])
def get_interview_feedback(
    booking_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Retrieve interview evaluation feedback if the user is authorized.
    """
    fb = LiveInterviewService.get_feedback(db, booking_id, current_user)
    return ApiResponse(
        success=True,
        message="Interview feedback retrieved.",
        data=LiveInterviewFeedbackResponse(
            id=fb.id,
            booking_id=fb.booking_id,
            teacher_id=fb.teacher_id,
            teacher_name=fb.teacher.name if fb.teacher else "Teacher",
            technical_score=fb.technical_score,
            communication_feedback=fb.communication_feedback,
            problem_solving_feedback=fb.problem_solving_feedback,
            strengths=fb.strengths or [],
            areas_for_improvement=fb.areas_for_improvement or [],
            teacher_comments=fb.teacher_comments,
            recommended_topics=fb.recommended_topics or [],
            submitted_at=fb.submitted_at,
        ),
    )


# -----------------------------------------------------------------------------
# 4. WebRTC Real-Time Signaling WebSocket Endpoint
# -----------------------------------------------------------------------------
@router.websocket("/ws/{room_id}")
async def live_webrtc_signaling_websocket(
    websocket: WebSocket,
    room_id: str,
    token: Optional[str] = Query(None),
    db: Session = Depends(get_db),
):
    """
    Section 5: Real-time WebRTC Signaling & in-meeting synchronization.
    Authenticates token, verifies authorization for room, exchanges offers,
    answers, ICE candidates, chat, and screen-sharing events.
    """
    # 1. Token validation
    auth_token = token
    if not auth_token:
        # Check Authorization query header or subprotocols
        auth_header = websocket.headers.get("authorization")
        if auth_header and auth_header.startswith("Bearer "):
            auth_token = auth_header.split("Bearer ")[1].strip()

    if not auth_token:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION, reason="Missing authentication token")
        return

    payload = decode_access_token(auth_token)
    if not payload or not payload.get("sub"):
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION, reason="Invalid authentication token")
        return

    user_id = payload.get("sub")

    # 2. Check room authorization with database session
    user = db.query(User).filter(User.id == user_id, User.is_active == True).first()
    if not user:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION, reason="User not found")
        return

    try:
        room = LiveInterviewService.get_room_by_identifier(db, room_id, user)
    except HTTPException as e:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION, reason=e.detail)
        return

    user_name = user.name
    user_role = "teacher" if user.id == room.booking.teacher_id else "student"
    internal_room_id = room.id

    # 3. Connect to signaling manager
    await live_signaling_manager.connect(
        room_id=room_id,
        user_id=user_id,
        user_name=user_name,
        role=user_role,
        websocket=websocket,
    )

    try:
        while True:
            raw_data = await websocket.receive_text()
            try:
                data = json.loads(raw_data)
            except Exception:
                continue

            msg_type = data.get("type")

            # Route 1: WebRTC SDP Offer / Answer
            if msg_type in ["offer", "answer"]:
                await live_signaling_manager.broadcast_to_room(
                    room_id=room_id,
                    message={
                        "type": msg_type,
                        "sdp": data.get("sdp"),
                        "sender_id": user_id,
                        "sender_name": user_name,
                    },
                    exclude_user_id=user_id,
                )

            # Route 2: ICE Candidates
            elif msg_type == "ice-candidate":
                await live_signaling_manager.broadcast_to_room(
                    room_id=room_id,
                    message={
                        "type": "ice-candidate",
                        "candidate": data.get("candidate"),
                        "sender_id": user_id,
                    },
                    exclude_user_id=user_id,
                )

            # Route 3: In-Meeting Real-Time Chat
            elif msg_type == "chat-message":
                text = (data.get("message") or "").strip()
                if text:
                    saved_msg = LiveInterviewService.save_chat_message(
                        db, internal_room_id, user_id, text
                    )
                    created_iso = saved_msg.created_at.isoformat()
                    msg_id = saved_msg.id

                    # Broadcast to everyone including sender confirmation
                    await live_signaling_manager.broadcast_to_room(
                        room_id=room_id,
                        message={
                            "type": "chat-message",
                            "id": msg_id,
                            "sender_id": user_id,
                            "sender_name": user_name,
                            "sender_role": user_role,
                            "message": text,
                            "timestamp": created_iso,
                        },
                    )

            # Route 4: Media Status Updates (Mic toggle, Cam toggle)
            elif msg_type == "media-state":
                await live_signaling_manager.broadcast_to_room(
                    room_id=room_id,
                    message={
                        "type": "media-state",
                        "sender_id": user_id,
                        "mic_on": data.get("mic_on", True),
                        "cam_on": data.get("cam_on", True),
                    },
                    exclude_user_id=user_id,
                )

            # Route 5: Screen Sharing Status
            elif msg_type == "screen-share-status":
                await live_signaling_manager.broadcast_to_room(
                    room_id=room_id,
                    message={
                        "type": "screen-share-status",
                        "sender_id": user_id,
                        "sender_name": user_name,
                        "is_sharing": data.get("is_sharing", False),
                    },
                    exclude_user_id=user_id,
                )

            # Route 6: Admit Waiting Student (Faculty Host)
            elif msg_type == "admit-student":
                if user_role in ["teacher", "admin"]:
                    LiveInterviewService.admit_student(db, room_id, user)
                    await live_signaling_manager.broadcast_to_room(
                        room_id=room_id,
                        message={"type": "student-admitted"},
                    )

            # Route 7: End Interview for Everyone (Faculty Host)
            elif msg_type == "end-interview":
                if user_role in ["teacher", "admin"]:
                    LiveInterviewService.end_interview(db, room_id, user)
                    await live_signaling_manager.broadcast_to_room(
                        room_id=room_id,
                        message={"type": "interview-ended", "by": user_name},
                    )

    except WebSocketDisconnect:
        live_signaling_manager.disconnect(room_id, user_id)
        # Notify remaining peer that this participant left
        await live_signaling_manager.broadcast_to_room(
            room_id=room_id,
            message={
                "type": "peer-left",
                "user_id": user_id,
                "name": user_name,
            },
        )
    except Exception as e:
        logger.warning(f"WebSocket exception in room {room_id}: {e}")
        live_signaling_manager.disconnect(room_id, user_id)
