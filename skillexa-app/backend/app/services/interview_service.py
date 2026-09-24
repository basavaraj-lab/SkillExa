import uuid
from datetime import datetime
from typing import List, Optional
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from backend.app.models.interview import (
    Interview,
    InterviewQuestion,
    InterviewResult,
    InterviewStatusEnum,
    VideoSession,
)
from backend.app.models.user import FacultyProfile, StudentProfile
from backend.app.schemas.interview import (
    CreateInterviewRequest,
    InterviewEvaluationRequest,
)


class InterviewService:
    @staticmethod
    def create_interview(db: Session, faculty: FacultyProfile, req: CreateInterviewRequest) -> Interview:
        # Check student exists
        student = db.query(StudentProfile).filter(StudentProfile.id == req.student_id).first()
        if not student:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Target student not found.")

        interview = Interview(
            faculty_id=faculty.id,
            student_id=student.id,
            college_id=faculty.college_id,
            title=req.title.strip(),
            interview_type=req.interview_type,
            subject_or_role=req.subject_or_role.strip(),
            difficulty=req.difficulty or "Medium",
            scheduled_at=req.scheduled_at,
            duration_minutes=req.duration_minutes,
            status=InterviewStatusEnum.SCHEDULED,
        )
        db.add(interview)
        db.flush()

        # Add predefined questions
        if req.questions:
            for idx, q_req in enumerate(req.questions):
                q = InterviewQuestion(
                    interview_id=interview.id,
                    question_text=q_req.question_text.strip(),
                    category=q_req.category or "Technical",
                    marks=q_req.marks,
                    order_index=idx,
                )
                db.add(q)

        # Allocate WebRTC Video Room
        room_id = f"room-skillexa-{interview.id[:8]}-{uuid.uuid4().hex[:6]}"
        video_session = VideoSession(
            interview_id=interview.id,
            room_id=room_id,
            faculty_id=faculty.user_id,
            student_id=student.user_id,
            session_status="WAITING",
        )
        db.add(video_session)

        db.commit()
        db.refresh(interview)
        return interview

    @staticmethod
    def evaluate_interview(
        db: Session,
        interview_id: str,
        faculty: FacultyProfile,
        req: InterviewEvaluationRequest,
    ) -> InterviewResult:
        interview = db.query(Interview).filter(Interview.id == interview_id).first()
        if not interview:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Interview not found.")

        if interview.faculty_id != faculty.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You can only evaluate interviews you conducted.")

        # Compute aggregate overall score
        overall = round(
            (req.technical_score * 0.4)
            + (req.problem_solving_score * 0.3)
            + (req.communication_score * 0.15)
            + (req.confidence_score * 0.15),
            2,
        )

        result = db.query(InterviewResult).filter(InterviewResult.interview_id == interview.id).first()
        if not result:
            result = InterviewResult(
                interview_id=interview.id,
                technical_score=req.technical_score,
                communication_score=req.communication_score,
                confidence_score=req.confidence_score,
                problem_solving_score=req.problem_solving_score,
                overall_score=overall,
                strengths=req.strengths,
                weaknesses=req.weaknesses,
                suggestions=req.suggestions,
                overall_feedback=req.overall_feedback.strip(),
                evaluated_at=datetime.utcnow(),
            )
            db.add(result)
        else:
            result.technical_score = req.technical_score
            result.communication_score = req.communication_score
            result.confidence_score = req.confidence_score
            result.problem_solving_score = req.problem_solving_score
            result.overall_score = overall
            result.strengths = req.strengths
            result.weaknesses = req.weaknesses
            result.suggestions = req.suggestions
            result.overall_feedback = req.overall_feedback.strip()
            result.evaluated_at = datetime.utcnow()

        interview.status = InterviewStatusEnum.COMPLETED
        db.commit()
        db.refresh(result)
        return result
