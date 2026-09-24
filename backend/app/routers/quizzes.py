from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from backend.app.dependencies.auth import get_current_student, require_approved_faculty
from backend.app.dependencies.db import get_db
from backend.app.models.quiz import Question, Quiz, QuizAttempt
from backend.app.models.user import FacultyProfile, StudentProfile
from backend.app.schemas.common import ApiResponse
from backend.app.schemas.quiz import (
    CreateQuestionRequest,
    CreateQuizRequest,
    QuestionForFacultyResponse,
    QuizAttemptResultResponse,
    QuizDetailForFacultyResponse,
    QuizResponse,
    StartQuizAttemptResponse,
    SubmitQuizRequest,
)
from backend.app.services.notification_service import NotificationService
from backend.app.services.quiz_service import QuizService

router = APIRouter(tags=["Quizzes & Assessments"])


@router.post("/faculty/quizzes", response_model=ApiResponse[QuizResponse], status_code=status.HTTP_201_CREATED)
def create_faculty_quiz(
    req: CreateQuizRequest,
    faculty: FacultyProfile = Depends(require_approved_faculty),
    db: Session = Depends(get_db),
):
    quiz = QuizService.create_quiz(db, faculty, req)

    # Dispatch targeted notification
    if quiz.visibility.value != "community" and quiz.published:
        NotificationService.notify_targeted_students(
            db=db,
            college_id=faculty.college_id,
            target_departments=quiz.target_departments,
            target_years=quiz.target_years,
            target_sections=quiz.target_sections,
            target_student_ids=quiz.target_student_ids,
            notification_type="NEW_QUIZ",
            title="📝 New Quiz Assessment Active",
            message=f"{faculty.user.name if faculty.user else 'Faculty'} created '{quiz.title}' for {quiz.topic}.",
            reference_id=quiz.id,
            action_route="/quizzpage",
            action_params={"quizId": quiz.id, "topic": quiz.topic, "subject": quiz.subject},
        )

    return ApiResponse(
        success=True,
        message="Faculty quiz created successfully!",
        data=QuizResponse(
            id=quiz.id,
            faculty_id=quiz.faculty_id,
            faculty_name=faculty.user.name if faculty.user else "Faculty",
            faculty_designation=faculty.designation,
            college_id=quiz.college_id,
            college_name=faculty.college.name if faculty.college else "College",
            title=quiz.title,
            description=quiz.description,
            section=quiz.section,
            subject=quiz.subject,
            topic=quiz.topic,
            subtopic=quiz.subtopic,
            language=quiz.language,
            difficulty=quiz.difficulty,
            duration_minutes=quiz.duration_minutes,
            total_marks=quiz.total_marks,
            negative_marks=quiz.negative_marks,
            questions_count=len(quiz.questions),
            visibility=quiz.visibility,
            published=quiz.published,
            created_at=quiz.created_at,
            updated_at=quiz.updated_at,
        ),
    )


@router.get("/faculty/quizzes", response_model=ApiResponse[List[QuizResponse]])
def get_my_quizzes(
    faculty: FacultyProfile = Depends(require_approved_faculty),
    db: Session = Depends(get_db),
):
    quizzes = db.query(Quiz).filter(Quiz.faculty_id == faculty.id).order_by(Quiz.created_at.desc()).all()
    results = [
        QuizResponse(
            id=q.id,
            faculty_id=q.faculty_id,
            faculty_name=faculty.user.name if faculty.user else "Faculty",
            faculty_designation=faculty.designation,
            college_id=q.college_id,
            college_name=faculty.college.name if faculty.college else "College",
            title=q.title,
            description=q.description,
            section=q.section,
            subject=q.subject,
            topic=q.topic,
            subtopic=q.subtopic,
            language=q.language,
            difficulty=q.difficulty,
            duration_minutes=q.duration_minutes,
            total_marks=q.total_marks,
            negative_marks=q.negative_marks,
            questions_count=len(q.questions),
            visibility=q.visibility,
            published=q.published,
            created_at=q.created_at,
            updated_at=q.updated_at,
        )
        for q in quizzes
    ]
    return ApiResponse(
        success=True,
        message="Faculty quizzes retrieved.",
        data=results,
    )


@router.get("/faculty/quizzes/{id}", response_model=ApiResponse[QuizDetailForFacultyResponse])
def get_faculty_quiz_detail(
    id: str,
    faculty: FacultyProfile = Depends(require_approved_faculty),
    db: Session = Depends(get_db),
):
    quiz = db.query(Quiz).filter(Quiz.id == id).first()
    if not quiz:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Quiz not found.")

    questions = db.query(Question).filter(Question.quiz_id == quiz.id).order_by(Question.order_index).all()
    return ApiResponse(
        success=True,
        message="Quiz details retrieved.",
        data=QuizDetailForFacultyResponse(
            id=quiz.id,
            faculty_id=quiz.faculty_id,
            faculty_name=faculty.user.name if faculty.user else "Faculty",
            faculty_designation=faculty.designation,
            college_id=quiz.college_id,
            college_name=faculty.college.name if faculty.college else "College",
            title=quiz.title,
            description=quiz.description,
            section=quiz.section,
            subject=quiz.subject,
            topic=quiz.topic,
            subtopic=quiz.subtopic,
            language=quiz.language,
            difficulty=quiz.difficulty,
            duration_minutes=quiz.duration_minutes,
            total_marks=quiz.total_marks,
            negative_marks=quiz.negative_marks,
            questions_count=len(questions),
            visibility=quiz.visibility,
            published=quiz.published,
            created_at=quiz.created_at,
            updated_at=quiz.updated_at,
            questions=[QuestionForFacultyResponse.model_validate(q) for q in questions],
        ),
    )


@router.post("/faculty/quizzes/{id}/questions", response_model=ApiResponse[QuestionForFacultyResponse], status_code=status.HTTP_201_CREATED)
def add_question(
    id: str,
    req: CreateQuestionRequest,
    faculty: FacultyProfile = Depends(require_approved_faculty),
    db: Session = Depends(get_db),
):
    question = QuizService.add_question_to_quiz(db, id, faculty, req)
    return ApiResponse(
        success=True,
        message="Question added to quiz.",
        data=QuestionForFacultyResponse.model_validate(question),
    )


# ---------------- Student Quiz APIs ----------------

@router.post("/quizzes/{id}/start", response_model=ApiResponse[StartQuizAttemptResponse])
def start_quiz(
    id: str,
    student: StudentProfile = Depends(get_current_student),
    db: Session = Depends(get_db),
):
    """Start an attempt. Questions are provided without correct answers to prevent client leakage."""
    attempt_res = QuizService.start_quiz_attempt(db, id, student)
    return ApiResponse(
        success=True,
        message="Quiz attempt initialized.",
        data=attempt_res,
    )


@router.post("/quizzes/submit", response_model=ApiResponse[QuizAttemptResultResponse])
def submit_quiz(
    req: SubmitQuizRequest,
    student: StudentProfile = Depends(get_current_student),
    db: Session = Depends(get_db),
):
    """Submit attempt, calculate score, accuracy, negative marks, and topic progress."""
    result = QuizService.submit_quiz_attempt(db, student, req)
    return ApiResponse(
        success=True,
        message="Quiz submitted and evaluated successfully!",
        data=result,
    )


@router.get("/quizzes/history", response_model=ApiResponse[List[dict]])
def get_quiz_history(
    student: StudentProfile = Depends(get_current_student),
    db: Session = Depends(get_db),
):
    attempts = db.query(QuizAttempt).filter(QuizAttempt.student_id == student.id).order_by(QuizAttempt.submitted_at.desc()).all()
    results = [
        {
            "attempt_id": a.id,
            "quiz_id": a.quiz_id,
            "quiz_title": a.quiz.title if a.quiz else "Quiz",
            "subject": a.quiz.subject if a.quiz else "",
            "topic": a.quiz.topic if a.quiz else "",
            "score": a.score,
            "total_marks": a.total_marks,
            "accuracy_percentage": a.accuracy_percentage,
            "time_taken_seconds": a.time_taken_seconds,
            "submitted_at": a.submitted_at.isoformat(),
        }
        for a in attempts
    ]
    return ApiResponse(
        success=True,
        message="Quiz history retrieved.",
        data=results,
    )
