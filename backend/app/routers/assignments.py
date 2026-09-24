from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.app.dependencies.auth import get_current_student, require_approved_faculty
from backend.app.dependencies.db import get_db
from backend.app.models.assignment import Assignment, AssignmentSubmission
from backend.app.models.user import FacultyProfile, StudentProfile
from backend.app.schemas.assignment import (
    AssignmentResponse,
    AssignmentSubmissionResponse,
    CreateAssignmentRequest,
    EvaluateAssignmentRequest,
    SubmitAssignmentRequest,
)
from backend.app.schemas.common import ApiResponse
from backend.app.services.notification_service import NotificationService

router = APIRouter(prefix="/assignments", tags=["Assignments"])


@router.post("", response_model=ApiResponse[AssignmentResponse], status_code=status.HTTP_201_CREATED)
def create_assignment(
    req: CreateAssignmentRequest,
    faculty: FacultyProfile = Depends(require_approved_faculty),
    db: Session = Depends(get_db),
):
    assignment = Assignment(
        faculty_id=faculty.id,
        college_id=faculty.college_id,
        title=req.title.strip(),
        description=req.description.strip(),
        subject=req.subject.strip(),
        topic=req.topic.strip(),
        max_marks=req.max_marks,
        due_date=req.due_date,
        published=req.published,
        target_departments=req.target_departments or [faculty.department],
        target_years=req.target_years or [],
        target_sections=req.target_sections or [],
    )
    db.add(assignment)
    db.commit()
    db.refresh(assignment)

    # Dispatch targeted notification
    NotificationService.notify_targeted_students(
        db=db,
        college_id=faculty.college_id,
        target_departments=assignment.target_departments,
        target_years=assignment.target_years,
        target_sections=assignment.target_sections,
        target_student_ids=[],
        notification_type="NEW_ASSIGNMENT",
        title="📋 New Course Assignment Assigned",
        message=f"{faculty.user.name if faculty.user else 'Faculty'} created '{assignment.title}' for {assignment.subject}.",
        reference_id=assignment.id,
        action_route="/my-college",
        action_params={"assignmentId": assignment.id},
    )

    return ApiResponse(
        success=True,
        message="Assignment created and distributed to class.",
        data=assignment,
    )


@router.get("", response_model=ApiResponse[List[AssignmentResponse]])
def get_assignments(
    faculty: Optional[FacultyProfile] = Depends(require_approved_faculty),
    db: Session = Depends(get_db),
):
    assignments = db.query(Assignment).filter(Assignment.faculty_id == faculty.id).order_by(Assignment.created_at.desc()).all()
    return ApiResponse(
        success=True,
        message="Assignments retrieved.",
        data=assignments,
    )


@router.post("/{id}/submit", response_model=ApiResponse[AssignmentSubmissionResponse])
def submit_assignment(
    id: str,
    req: SubmitAssignmentRequest,
    student: StudentProfile = Depends(get_current_student),
    db: Session = Depends(get_db),
):
    assignment = db.query(Assignment).filter(Assignment.id == id).first()
    if not assignment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Assignment not found.")

    sub = db.query(AssignmentSubmission).filter(AssignmentSubmission.assignment_id == id, AssignmentSubmission.student_id == student.id).first()
    if not sub:
        sub = AssignmentSubmission(
            assignment_id=id,
            student_id=student.id,
            submission_text=req.submission_text,
            file_path=req.file_path,
            status="SUBMITTED",
        )
        db.add(sub)
    else:
        sub.submission_text = req.submission_text
        sub.file_path = req.file_path
        sub.status = "SUBMITTED"

    db.commit()
    db.refresh(sub)
    return ApiResponse(
        success=True,
        message="Assignment submitted successfully!",
        data=sub,
    )


@router.post("/submissions/{submission_id}/evaluate", response_model=ApiResponse[AssignmentSubmissionResponse])
def evaluate_submission(
    submission_id: str,
    req: EvaluateAssignmentRequest,
    faculty: FacultyProfile = Depends(require_approved_faculty),
    db: Session = Depends(get_db),
):
    sub = db.query(AssignmentSubmission).filter(AssignmentSubmission.id == submission_id).first()
    if not sub:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Submission not found.")

    sub.score = req.score
    sub.feedback = req.feedback.strip()
    sub.status = "EVALUATED"
    db.commit()
    db.refresh(sub)

    # Notify student
    NotificationService.send_notification(
        db=db,
        user_id=sub.student.user_id,
        notification_type="QUIZ_RESULT",
        title="📝 Assignment Evaluated",
        message=f"Your submission for '{sub.assignment.title}' received score {sub.score}/{sub.assignment.max_marks}.",
        reference_id=sub.id,
    )

    return ApiResponse(
        success=True,
        message="Submission evaluated.",
        data=sub,
    )
