from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, WebSocket, WebSocketDisconnect, status
from sqlalchemy.orm import Session
from backend.app.dependencies.auth import get_current_user, require_approved_faculty
from backend.app.dependencies.db import get_db
from backend.app.models.interview import Interview, InterviewResult, VideoSession
from backend.app.models.user import FacultyProfile, User
from backend.app.schemas.common import ApiResponse
from backend.app.schemas.interview import (
    CreateInterviewRequest,
    InterviewEvaluationRequest,
    InterviewQuestionResponse,
    InterviewResponse,
    InterviewResultResponse,
    VideoSessionResponse,
)
from backend.app.services.interview_service import InterviewService
from backend.app.services.notification_service import NotificationService
from backend.app.services.webrtc_service import signaling_manager

router = APIRouter(prefix="/interviews", tags=["Interviews & Viva"])


@router.post("", response_model=ApiResponse[InterviewResponse], status_code=status.HTTP_201_CREATED)
def schedule_interview(
    req: CreateInterviewRequest,
    faculty: FacultyProfile = Depends(require_approved_faculty),
    db: Session = Depends(get_db),
):
    interview = InterviewService.create_interview(db, faculty, req)

    # Dispatch notification to student
    NotificationService.send_notification(
        db=db,
        user_id=interview.student.user_id,
        notification_type="INTERVIEW_INVITATION",
        title=f"🎤 Interview Scheduled: {interview.title}",
        message=f"{faculty.user.name if faculty.user else 'Faculty'} scheduled a {interview.interview_type.value} on {interview.scheduled_at.strftime('%b %d at %I:%M %p')}.",
        reference_id=interview.id,
        action_route="/faculty/live-interview",
        action_params={"interviewId": interview.id, "roomId": interview.video_session.room_id if interview.video_session else ""},
    )

    return ApiResponse(
        success=True,
        message="Interview scheduled and candidate notified.",
        data=InterviewResponse(
            id=interview.id,
            faculty_id=interview.faculty_id,
            faculty_name=faculty.user.name if faculty.user else "Faculty",
            student_id=interview.student_id,
            student_name=interview.student.user.name if interview.student and interview.student.user else "Student",
            college_id=interview.college_id,
            title=interview.title,
            interview_type=interview.interview_type,
            subject_or_role=interview.subject_or_role,
            difficulty=interview.difficulty or "Medium",
            scheduled_at=interview.scheduled_at,
            duration_minutes=interview.duration_minutes,
            status=interview.status,
            questions=[InterviewQuestionResponse.model_validate(q) for q in interview.questions],
            room_id=interview.video_session.room_id if interview.video_session else None,
            created_at=interview.created_at,
        ),
    )


@router.get("", response_model=ApiResponse[List[InterviewResponse]])
def get_interviews(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    if current_user.role.value == "faculty" and current_user.faculty_profile:
        interviews = db.query(Interview).filter(Interview.faculty_id == current_user.faculty_profile.id).order_by(Interview.scheduled_at.desc()).all()
    elif current_user.role.value == "student" and current_user.student_profile:
        interviews = db.query(Interview).filter(Interview.student_id == current_user.student_profile.id).order_by(Interview.scheduled_at.desc()).all()
    else:
        interviews = db.query(Interview).order_by(Interview.scheduled_at.desc()).all()

    results = []
    for i in interviews:
        res = InterviewResultResponse.model_validate(i.result) if i.result else None
        results.append(
            InterviewResponse(
                id=i.id,
                faculty_id=i.faculty_id,
                faculty_name=i.faculty.user.name if i.faculty and i.faculty.user else "Faculty",
                student_id=i.student_id,
                student_name=i.student.user.name if i.student and i.student.user else "Student",
                college_id=i.college_id,
                title=i.title,
                interview_type=i.interview_type,
                subject_or_role=i.subject_or_role,
                difficulty=i.difficulty or "Medium",
                scheduled_at=i.scheduled_at,
                duration_minutes=i.duration_minutes,
                status=i.status,
                questions=[InterviewQuestionResponse.model_validate(q) for q in i.questions],
                result=res,
                room_id=i.video_session.room_id if i.video_session else None,
                created_at=i.created_at,
            )
        )

    return ApiResponse(
        success=True,
        message="Interviews retrieved.",
        data=results,
    )


@router.post("/{id}/evaluate", response_model=ApiResponse[InterviewResultResponse])
def evaluate_interview(
    id: str,
    req: InterviewEvaluationRequest,
    faculty: FacultyProfile = Depends(require_approved_faculty),
    db: Session = Depends(get_db),
):
    result = InterviewService.evaluate_interview(db, id, faculty, req)

    # Notify student of results
    interview = result.interview
    if interview and interview.student:
        NotificationService.send_notification(
            db=db,
            user_id=interview.student.user_id,
            notification_type="INTERVIEW_RESULT",
            title="🎯 Interview Evaluation Complete",
            message=f"Your {interview.interview_type.value} was evaluated by {faculty.user.name if faculty.user else 'Faculty'}. Score: {result.overall_score}/100.",
            reference_id=interview.id,
            action_route="/faculty/evaluation",
        )

    return ApiResponse(
        success=True,
        message="Interview evaluation recorded.",
        data=InterviewResultResponse.model_validate(result),
    )


@router.get("/rooms/{room_id}", response_model=ApiResponse[VideoSessionResponse])
def get_video_room_session(
    room_id: str,
    db: Session = Depends(get_db),
):
    session = db.query(VideoSession).filter(VideoSession.room_id == room_id).first()
    if not session:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Video session room not found.")
    return ApiResponse(
        success=True,
        message="Video session status retrieved.",
        data=VideoSessionResponse(
            room_id=session.room_id,
            interview_id=session.interview_id,
            faculty_id=session.faculty_id,
            student_id=session.student_id,
            session_status=session.session_status,
            faculty_joined=session.faculty_joined,
            student_joined=session.student_joined,
            started_at=session.started_at,
            ended_at=session.ended_at,
        ),
    )


@router.websocket("/ws/{room_id}")
async def websocket_signaling_endpoint(
    websocket: WebSocket,
    room_id: str,
):
    """
    Section 23: WebRTC Real-Time Signaling endpoint.
    Exchanges SDP offer, answer, and ICE candidates between candidate and faculty.
    """
    await signaling_manager.connect(room_id, websocket)
    try:
        while True:
            data = await websocket.receive_json()
            # Forward signaling payload to peer in the room
            await signaling_manager.broadcast_to_room(room_id, data, sender=websocket)
    except WebSocketDisconnect:
        signaling_manager.disconnect(room_id, websocket)
    except Exception:
        signaling_manager.disconnect(room_id, websocket)
