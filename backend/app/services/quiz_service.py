from datetime import datetime
from typing import List, Optional
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from backend.app.models.note import VisibilityEnum
from backend.app.models.notification import StudentProgress
from backend.app.models.quiz import (
    Question,
    Quiz,
    QuizAnswer,
    QuizAttempt,
)
from backend.app.models.user import FacultyProfile, StudentProfile
from backend.app.schemas.quiz import (
    AnswerResultItem,
    CreateQuestionRequest,
    CreateQuizRequest,
    QuestionForStudentResponse,
    QuizAttemptResultResponse,
    StartQuizAttemptResponse,
    SubmitQuizRequest,
)
from backend.app.services.college_service import CollegeService


class QuizService:
    @staticmethod
    def create_quiz(db: Session, faculty: FacultyProfile, req: CreateQuizRequest) -> Quiz:
        quiz = Quiz(
            faculty_id=faculty.id,
            college_id=faculty.college_id,
            title=req.title.strip(),
            description=req.description.strip() if req.description else None,
            section=req.section.strip(),
            subject=req.subject.strip(),
            topic=req.topic.strip(),
            subtopic=req.subtopic.strip() if req.subtopic else None,
            language=req.language.strip() if req.language else None,
            difficulty=req.difficulty,
            duration_minutes=req.duration_minutes,
            total_marks=req.total_marks,
            negative_marks=req.negative_marks,
            visibility=req.visibility,
            published=req.published,
            target_departments=req.target_departments or [faculty.department],
            target_years=req.target_years or [],
            target_sections=req.target_sections or [],
            target_student_ids=req.target_student_ids or [],
        )
        db.add(quiz)
        db.flush()

        # Add questions if provided
        if req.questions:
            for idx, q_req in enumerate(req.questions):
                question = Question(
                    quiz_id=quiz.id,
                    section=q_req.section or req.section,
                    subject=q_req.subject or req.subject,
                    topic=q_req.topic or req.topic,
                    subtopic=q_req.subtopic or req.subtopic,
                    language=q_req.language or req.language,
                    difficulty=q_req.difficulty,
                    question_type=q_req.question_type,
                    question_text=q_req.question_text.strip(),
                    options=q_req.options,
                    correct_answer=q_req.correct_answer,
                    explanation=q_req.explanation,
                    marks=q_req.marks,
                    negative_marks=q_req.negative_marks,
                    order_index=idx,
                )
                db.add(question)

        db.commit()
        db.refresh(quiz)
        return quiz

    @staticmethod
    def add_question_to_quiz(db: Session, quiz_id: str, faculty: FacultyProfile, req: CreateQuestionRequest) -> Question:
        quiz = db.query(Quiz).filter(Quiz.id == quiz_id).first()
        if not quiz:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Quiz not found.")

        if quiz.faculty_id != faculty.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You can only add questions to your own quizzes.")

        current_count = db.query(Question).filter(Question.quiz_id == quiz_id).count()

        question = Question(
            quiz_id=quiz.id,
            section=req.section or quiz.section,
            subject=req.subject or quiz.subject,
            topic=req.topic or quiz.topic,
            subtopic=req.subtopic or quiz.subtopic,
            language=req.language or quiz.language,
            difficulty=req.difficulty,
            question_type=req.question_type,
            question_text=req.question_text.strip(),
            options=req.options,
            correct_answer=req.correct_answer,
            explanation=req.explanation,
            marks=req.marks,
            negative_marks=req.negative_marks,
            order_index=req.order_index or current_count,
        )
        db.add(question)
        db.commit()
        db.refresh(question)
        return question

    @staticmethod
    def start_quiz_attempt(db: Session, quiz_id: str, student: StudentProfile) -> StartQuizAttemptResponse:
        quiz = db.query(Quiz).filter(Quiz.id == quiz_id).first()
        if not quiz:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Quiz not found.")

        if not quiz.published:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="This quiz is not currently active.")

        # Create Attempt Record
        attempt = QuizAttempt(
            quiz_id=quiz.id,
            student_id=student.id,
            total_marks=quiz.total_marks,
            status="IN_PROGRESS",
            started_at=datetime.utcnow(),
            submitted_at=datetime.utcnow(),
        )
        db.add(attempt)
        db.commit()
        db.refresh(attempt)

        # Questions for student (without correct answers)
        questions = db.query(Question).filter(Question.quiz_id == quiz.id).order_by(Question.order_index).all()
        student_questions = [
            QuestionForStudentResponse(
                id=q.id,
                quiz_id=q.quiz_id,
                section=q.section,
                subject=q.subject,
                topic=q.topic,
                subtopic=q.subtopic,
                language=q.language,
                difficulty=q.difficulty,
                question_type=q.question_type,
                question_text=q.question_text,
                options=q.options,
                marks=q.marks,
                order_index=q.order_index,
            )
            for q in questions
        ]

        return StartQuizAttemptResponse(
            attempt_id=attempt.id,
            quiz_id=quiz.id,
            title=quiz.title,
            duration_minutes=quiz.duration_minutes,
            total_questions=len(student_questions),
            started_at=attempt.started_at,
            questions=student_questions,
        )

    @staticmethod
    def submit_quiz_attempt(db: Session, student: StudentProfile, req: SubmitQuizRequest) -> QuizAttemptResultResponse:
        attempt = db.query(QuizAttempt).filter(QuizAttempt.id == req.attempt_id).first()
        if not attempt:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Quiz attempt not found.")

        if attempt.student_id != student.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Unauthorized quiz attempt submission.")

        quiz = db.query(Quiz).filter(Quiz.id == attempt.quiz_id).first()
        questions = db.query(Question).filter(Question.quiz_id == quiz.id).order_by(Question.order_index).all()

        total_score = 0.0
        max_marks = 0.0
        correct_count = 0
        wrong_count = 0
        unanswered_count = 0
        breakdown: List[AnswerResultItem] = []

        # Delete any previous answers for this attempt (idempotent re-submit safeguard)
        db.query(QuizAnswer).filter(QuizAnswer.attempt_id == attempt.id).delete()

        for q in questions:
            max_marks += q.marks
            selected = req.answers.get(q.id)

            if selected is None:
                unanswered_count += 1
                is_correct = False
                marks_awarded = 0.0
            elif selected == q.correct_answer:
                correct_count += 1
                is_correct = True
                marks_awarded = q.marks
                total_score += marks_awarded
            else:
                wrong_count += 1
                is_correct = False
                marks_awarded = -abs(q.negative_marks)
                total_score += marks_awarded

            # Record answer
            answer_rec = QuizAnswer(
                attempt_id=attempt.id,
                question_id=q.id,
                selected_option=selected,
                is_correct=is_correct,
            )
            db.add(answer_rec)

            breakdown.append(
                AnswerResultItem(
                    question_id=q.id,
                    question_text=q.question_text,
                    options=q.options,
                    selected_option=selected,
                    correct_option=q.correct_answer,
                    is_correct=is_correct,
                    explanation=q.explanation,
                    marks_awarded=marks_awarded,
                )
            )

        final_score = max(0.0, total_score)
        total_answered = correct_count + wrong_count
        accuracy = round((correct_count / total_answered * 100.0), 2) if total_answered > 0 else 0.0

        # Update attempt
        attempt.score = final_score
        attempt.total_marks = max_marks
        attempt.accuracy_percentage = accuracy
        attempt.correct_count = correct_count
        attempt.wrong_count = wrong_count
        attempt.unanswered_count = unanswered_count
        attempt.time_taken_seconds = req.time_taken_seconds
        attempt.status = "COMPLETED"
        attempt.submitted_at = datetime.utcnow()

        # Update StudentProgress for this topic
        progress = (
            db.query(StudentProgress)
            .filter(
                StudentProgress.student_id == student.id,
                StudentProgress.subject == quiz.subject,
                StudentProgress.topic == quiz.topic,
            )
            .first()
        )
        if not progress:
            progress = StudentProgress(
                student_id=student.id,
                section=quiz.section,
                subject=quiz.subject,
                topic=quiz.topic,
                quizzes_completed=1,
                quiz_accuracy=accuracy,
                mastery_percentage=min(100.0, accuracy * 0.9),
                last_activity_at=datetime.utcnow(),
            )
            db.add(progress)
        else:
            progress.quizzes_completed += 1
            progress.quiz_accuracy = round((progress.quiz_accuracy + accuracy) / 2.0, 2)
            progress.mastery_percentage = min(100.0, max(progress.mastery_percentage, accuracy * 0.9))
            progress.last_activity_at = datetime.utcnow()

        db.commit()

        return QuizAttemptResultResponse(
            attempt_id=attempt.id,
            quiz_id=quiz.id,
            quiz_title=quiz.title,
            score=final_score,
            total_marks=max_marks,
            accuracy_percentage=accuracy,
            correct_count=correct_count,
            wrong_count=wrong_count,
            unanswered_count=unanswered_count,
            time_taken_seconds=req.time_taken_seconds,
            submitted_at=attempt.submitted_at,
            breakdown=breakdown,
        )

    @staticmethod
    def get_quizzes_for_student(db: Session, student: StudentProfile, subject: Optional[str] = None, topic: Optional[str] = None) -> List[Quiz]:
        query = db.query(Quiz).filter(Quiz.published == True)

        if subject:
            query = query.filter(Quiz.subject.ilike(f"%{subject}%"))
        if topic:
            query = query.filter(Quiz.topic.ilike(f"%{topic}%"))

        all_quizzes = query.order_by(Quiz.created_at.desc()).all()
        accessible = []

        for q in all_quizzes:
            if q.visibility == VisibilityEnum.COMMUNITY:
                accessible.append(q)
            elif student.college_id and q.college_id == student.college_id:
                if CollegeService.matches_student_targeting(
                    q.college_id,
                    q.target_departments,
                    q.target_years,
                    q.target_sections,
                    q.target_student_ids,
                    student,
                ):
                    accessible.append(q)

        return accessible
