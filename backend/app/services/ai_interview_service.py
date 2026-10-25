import logging
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from backend.app.models.ai_interview import (
    AIInterviewAnswer,
    AIInterviewQuestion,
    AIInterviewReport,
    AIInterviewSession,
    AIQuestionBank,
    EducationalKnowledgeSource,
    EvaluationStatusEnum,
    InterviewCategoryEnum,
    InterviewDifficultyEnum,
    InterviewModeEnum,
    SessionStatusEnum,
)
from backend.app.models.user import User
from backend.app.schemas.ai_interview import StartAIInterviewRequest, SubmitAnswerRequest
from backend.app.services.answer_evaluation_service import AnswerEvaluationService
from backend.app.services.question_generation_service import QuestionGenerationService

logger = logging.getLogger("skillexa.ai_interview_service")


class AIInterviewService:
    """
    Main Domain Orchestration Service for SkillExa AI Mock Interviews.
    Enforces student data access isolation, safe state transitions, and automatic reporting.
    """

    @classmethod
    def start_session(
        cls, db: Session, user: User, req: StartAIInterviewRequest
    ) -> AIInterviewSession:
        """
        Create a new AI Interview Session and prepare the first question snapshot.
        """
        session = AIInterviewSession(
            user_id=user.id,
            interview_category=req.interview_category,
            job_role=req.job_role,
            subject=req.subject,
            programming_language=req.programming_language,
            difficulty=req.difficulty,
            experience_level=req.experience_level,
            interview_mode=req.interview_mode,
            preferred_language=req.preferred_language,
            duration_minutes=req.duration_minutes,
            total_questions=req.total_questions,
            questions_answered=0,
            status=SessionStatusEnum.IN_PROGRESS,
            started_at=datetime.now(timezone.utc),
        )
        db.add(session)
        db.flush()

        # Generate and save first question snapshot
        first_q_data = QuestionGenerationService.get_or_generate_question(
            db=db,
            category=req.interview_category,
            subject=req.subject,
            difficulty=req.difficulty,
            job_role=req.job_role,
            experience_level=req.experience_level,
        )

        q1 = AIInterviewQuestion(
            interview_id=session.id,
            question_bank_id=first_q_data.get("question_bank_id"),
            question_number=1,
            question_text=first_q_data["question_text"],
            topic=first_q_data.get("topic", req.subject),
            difficulty=first_q_data.get("difficulty", req.difficulty),
            expected_concepts=first_q_data.get("expected_concepts", []),
            evaluation_criteria=first_q_data.get("evaluation_criteria", {}),
            question_source=first_q_data.get("question_source", "predefined"),
            source_reference=first_q_data.get("source_reference"),
            generated_follow_up=False,
            asked_at=datetime.now(timezone.utc),
        )
        db.add(q1)
        db.commit()
        db.refresh(session)
        return session

    @classmethod
    def get_session(cls, db: Session, interview_id: str, current_user: User) -> AIInterviewSession:
        """
        Retrieve interview session and enforce strict candidate access authorization.
        """
        session = db.query(AIInterviewSession).filter(AIInterviewSession.id == interview_id).first()
        if not session:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"AI Interview session '{interview_id}' not found.",
            )

        # Enforce student-level isolation
        if session.user_id != current_user.id and current_user.role.value != "faculty":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Access denied: You are not authorized to view this interview session.",
            )

        return session

    @classmethod
    def submit_answer(
        cls,
        db: Session,
        interview_id: str,
        current_user: User,
        req: SubmitAnswerRequest,
    ) -> Dict[str, Any]:
        """
        Process student's text or transcribed voice answer, execute AI evaluation,
        and generate next question or final report.
        """
        session = cls.get_session(db, interview_id, current_user)

        if session.status == SessionStatusEnum.COMPLETED:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="This interview session is already completed. Answers cannot be submitted.",
            )

        # Verify question belongs to this session
        question = (
            db.query(AIInterviewQuestion)
            .filter(
                AIInterviewQuestion.id == req.question_id,
                AIInterviewQuestion.interview_id == session.id,
            )
            .first()
        )
        if not question:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Question not found in this interview session.",
            )

        # Prevent duplicate submissions
        existing_answer = (
            db.query(AIInterviewAnswer)
            .filter(AIInterviewAnswer.interview_question_id == question.id)
            .first()
        )
        if existing_answer:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="An answer for this question has already been submitted and evaluated.",
            )

        # 1. Retrieve sample answer from Question Bank if available
        sample_answer = None
        if question.question_bank_id:
            bank_item = db.query(AIQuestionBank).filter(AIQuestionBank.id == question.question_bank_id).first()
            if bank_item and bank_item.sample_answer:
                sample_answer = bank_item.sample_answer

        # 2. Retrieve verified educational knowledge source if cached or grounded
        knowledge_summary = None
        wiki_reference = question.source_reference
        if question.source_reference or question.topic:
            k_item = (
                db.query(EducationalKnowledgeSource)
                .filter(
                    (EducationalKnowledgeSource.source_url == question.source_reference)
                    | (EducationalKnowledgeSource.article_title.ilike(f"%{question.topic}%"))
                )
                .order_by(EducationalKnowledgeSource.retrieved_at.desc())
                .first()
            )
            if k_item:
                knowledge_summary = k_item.content_summary
                wiki_reference = k_item.source_url

        # 3. IF NO BACKEND SAMPLE ANSWER OR KNOWLEDGE SUMMARY: USE WIKIPEDIA!
        if not sample_answer or not knowledge_summary:
            from backend.app.services.knowledge_retrieval_service import KnowledgeRetrievalService
            wiki_data = KnowledgeRetrievalService.get_or_fetch_topic_knowledge(
                db, question.topic or session.subject
            )
            if wiki_data:
                knowledge_summary = wiki_data.get("content_summary")
                wiki_reference = wiki_data.get("source_url")
                if not question.source_reference:
                    question.source_reference = wiki_reference
                if not sample_answer:
                    # Synthesize verified model answer grounded in Wikipedia
                    summary_clean = (wiki_data.get("content_summary") or "").strip()
                    sample_answer = f"According to verified documentation on {wiki_data.get('article_title')}: {summary_clean[:420]}..."
                if not question.expected_concepts:
                    wiki_words = [w.strip(".,;:()") for w in (wiki_data.get("content_summary") or "").split() if len(w) > 5]
                    question.expected_concepts = list(dict.fromkeys(wiki_words))[:6]

        # Run Multi-Criteria Answer Evaluation (supporting up to 1,000+ words)
        eval_result = AnswerEvaluationService.evaluate_answer(
            question_text=question.question_text,
            student_answer=req.answer_text,
            topic=question.topic,
            difficulty=question.difficulty,
            expected_concepts=question.expected_concepts,
            evaluation_criteria=question.evaluation_criteria,
            sample_answer=sample_answer,
            interview_category=session.interview_category.value if hasattr(session.interview_category, "value") else str(session.interview_category),
            speech_metrics=req.speech_metrics,
            theory_reference=wiki_reference,
            knowledge_summary=knowledge_summary,
        )

        # Persist Answer and Score
        answer_record = AIInterviewAnswer(
            interview_question_id=question.id,
            answer_text=req.answer_text,
            answer_mode=req.answer_mode,
            submitted_at=datetime.now(timezone.utc),
            technical_score=eval_result["technical_score"],
            completeness_score=eval_result["completeness_score"],
            clarity_score=eval_result["clarity_score"],
            communication_score=eval_result["communication_score"],
            feedback=eval_result["feedback"],
            strengths=eval_result["strengths"],
            improvement_areas=eval_result["improvement_areas"],
            missing_concepts=eval_result["missing_concepts"],
            model_answer=eval_result.get("model_answer"),
            speech_metrics=req.speech_metrics or {},
            evaluation_status=EvaluationStatusEnum.COMPLETED,
        )
        db.add(answer_record)

        session.questions_answered += 1

        is_complete = session.questions_answered >= session.total_questions

        if is_complete:
            # Finish interview and generate final report
            cls._finalize_interview(db, session)
            db.commit()
            db.refresh(answer_record)
            return {
                "answer_id": answer_record.id,
                "question_id": question.id,
                "technical_score": answer_record.technical_score,
                "completeness_score": answer_record.completeness_score,
                "clarity_score": answer_record.clarity_score,
                "communication_score": answer_record.communication_score,
                "overall_score": eval_result["overall_score"],
                "verdict": eval_result.get("verdict", "Evaluated"),
                "student_answer": req.answer_text,
                "feedback": answer_record.feedback,
                "strengths": answer_record.strengths,
                "improvement_areas": answer_record.improvement_areas,
                "missing_concepts": answer_record.missing_concepts,
                "model_answer": answer_record.model_answer,
                "wikipedia_reference": wiki_reference,
                "is_interview_complete": True,
                "next_question_number": None,
                "next_question": None,
                "cumulative_accuracy": session.total_score,
                "questions_answered": session.questions_answered,
                "total_questions": session.total_questions,
            }

        # Otherwise, prepare the next question automatically
        next_q_number = session.questions_answered + 1
        
        # Check if an adaptive follow-up question is suitable (e.g., question 2 or 4)
        use_follow_up = (next_q_number % 2 == 0) and (eval_result["technical_score"] >= 6.0)

        if use_follow_up:
            follow_up = QuestionGenerationService.generate_follow_up_question(
                db=db,
                question_text=question.question_text,
                student_answer=req.answer_text,
                subject=session.subject,
                difficulty=session.difficulty.value if hasattr(session.difficulty, "value") else str(session.difficulty),
            )
            next_q = AIInterviewQuestion(
                interview_id=session.id,
                question_bank_id=None,
                question_number=next_q_number,
                question_text=follow_up["question_text"],
                topic=follow_up["topic"],
                difficulty=follow_up["difficulty"],
                expected_concepts=follow_up["expected_concepts"],
                evaluation_criteria=follow_up["evaluation_criteria"],
                question_source="adaptive_follow_up",
                generated_follow_up=True,
                parent_question_id=question.id,
                asked_at=datetime.now(timezone.utc),
            )
        else:
            # Retrieve already asked question bank IDs to prevent duplicates
            asked_bank_ids = [
                q.question_bank_id
                for q in session.questions
                if q.question_bank_id is not None
            ]
            next_data = QuestionGenerationService.get_or_generate_question(
                db=db,
                category=session.interview_category.value if hasattr(session.interview_category, "value") else str(session.interview_category),
                subject=session.subject,
                difficulty=session.difficulty.value if hasattr(session.difficulty, "value") else str(session.difficulty),
                job_role=session.job_role,
                experience_level=session.experience_level.value if hasattr(session.experience_level, "value") else str(session.experience_level),
                excluded_question_ids=asked_bank_ids,
            )
            next_q = AIInterviewQuestion(
                interview_id=session.id,
                question_bank_id=next_data.get("question_bank_id"),
                question_number=next_q_number,
                question_text=next_data["question_text"],
                topic=next_data.get("topic", session.subject),
                difficulty=next_data.get("difficulty", "Intermediate"),
                expected_concepts=next_data.get("expected_concepts", []),
                evaluation_criteria=next_data.get("evaluation_criteria", {}),
                question_source=next_data.get("question_source", "predefined"),
                source_reference=next_data.get("source_reference"),
                generated_follow_up=False,
                asked_at=datetime.now(timezone.utc),
            )

        db.add(next_q)
        db.commit()
        db.refresh(answer_record)
        db.refresh(next_q)

        # Calculate running cumulative accuracy across answered questions
        running_scores = [
            q.answer.technical_score
            for q in session.questions
            if q.answer and q.answer.technical_score is not None
        ]
        cumulative_acc = (
            round((sum(running_scores) / len(running_scores)) * 10.0, 1)
            if running_scores
            else eval_result["overall_score"]
        )

        next_q_data = {
            "id": next_q.id,
            "interview_id": session.id,
            "question_number": next_q.question_number,
            "total_questions": session.total_questions,
            "question_text": next_q.question_text,
            "topic": next_q.topic,
            "difficulty": next_q.difficulty,
            "hints": [],
            "generated_follow_up": next_q.generated_follow_up,
            "question_source": next_q.question_source,
            "source_reference": next_q.source_reference,
            "asked_at": next_q.asked_at,
        }

        return {
            "answer_id": answer_record.id,
            "question_id": question.id,
            "technical_score": answer_record.technical_score,
            "completeness_score": answer_record.completeness_score,
            "clarity_score": answer_record.clarity_score,
            "communication_score": answer_record.communication_score,
            "overall_score": eval_result["overall_score"],
            "verdict": eval_result.get("verdict", "Evaluated"),
            "student_answer": req.answer_text,
            "feedback": answer_record.feedback,
            "strengths": answer_record.strengths,
            "improvement_areas": answer_record.improvement_areas,
            "missing_concepts": answer_record.missing_concepts,
            "model_answer": answer_record.model_answer,
            "wikipedia_reference": wiki_reference,
            "is_interview_complete": False,
            "next_question_number": next_q_number,
            "next_question": next_q_data,
            "cumulative_accuracy": cumulative_acc,
            "questions_answered": session.questions_answered,
            "total_questions": session.total_questions,
        }

    @classmethod
    def _finalize_interview(cls, db: Session, session: AIInterviewSession) -> AIInterviewReport:
        """
        Compile final report, compute cumulative scores, and record feedback.
        """
        session.status = SessionStatusEnum.COMPLETED
        session.completed_at = datetime.now(timezone.utc)

        # Calculate average scores across all answered questions
        tech_scores = []
        clarity_scores = []
        comm_scores = []
        all_strengths = []
        all_improvements = []
        all_missing = []

        for q in session.questions:
            if q.answer and q.answer.evaluation_status == EvaluationStatusEnum.COMPLETED:
                if q.answer.technical_score is not None:
                    tech_scores.append(q.answer.technical_score)
                if q.answer.clarity_score is not None:
                    clarity_scores.append(q.answer.clarity_score)
                if q.answer.communication_score is not None:
                    comm_scores.append(q.answer.communication_score)
                if q.answer.strengths:
                    all_strengths.extend(q.answer.strengths)
                if q.answer.improvement_areas:
                    all_improvements.extend(q.answer.improvement_areas)
                if q.answer.missing_concepts:
                    all_missing.extend(q.answer.missing_concepts)

        avg_tech = sum(tech_scores) / len(tech_scores) if tech_scores else 5.0
        avg_clarity = sum(clarity_scores) / len(clarity_scores) if clarity_scores else 5.0
        avg_comm = sum(comm_scores) / len(comm_scores) if comm_scores else 5.0

        overall_score = round(((avg_tech * 0.45) + (avg_clarity * 0.30) + (avg_comm * 0.25)) * 10.0, 1)
        session.total_score = overall_score

        # Distinct curated strengths and improvements
        curated_strengths = list(dict.fromkeys(all_strengths))[:4] or [
            "Good command of core terminology",
            "Clear logical progression during technical explanations",
        ]
        curated_improvements = list(dict.fromkeys(all_improvements))[:4] or [
            "Practice elaborating on high-concurrency and scale trade-offs",
            "Provide more concrete system architecture examples",
        ]

        # Recommended practice topics based on missing concepts or curriculum
        recommended_topics = list(dict.fromkeys(all_missing))[:4] or [
            f"{session.subject} Core Architecture",
            f"{session.subject} Optimization & Best Practices",
            "Data Structures & Algorithmic Complexity",
        ]

        technical_summary = (
            f"Achieved a technical proficiency score of {round(avg_tech, 1)}/10.0 across {len(tech_scores)} questions. "
            f"Demonstrated good theoretical grasp with opportunities to strengthen deep edge-case analysis."
        )

        communication_summary = (
            f"Communication rated at {round(avg_comm, 1)}/10.0. Logical organization was consistently "
            f"{'strong' if avg_clarity >= 7.0 else 'moderate'}. Effectively used technical vocabulary."
        )

        final_feedback = (
            f"Overall performance in this {session.interview_category.value if hasattr(session.interview_category, 'value') else session.interview_category} interview was "
            f"{'exemplary' if overall_score >= 80 else 'promising with focused areas for refinement'}. "
            f"Continue practicing structured explanations using the STAR framework and concrete code trade-offs."
        )

        report = AIInterviewReport(
            interview_id=session.id,
            overall_score=overall_score,
            technical_summary=technical_summary,
            communication_summary=communication_summary,
            strengths=curated_strengths,
            improvement_areas=curated_improvements,
            recommended_topics=recommended_topics,
            final_feedback=final_feedback,
            generated_at=datetime.now(timezone.utc),
        )
        db.add(report)
        return report

    @classmethod
    def get_report(cls, db: Session, interview_id: str, current_user: User) -> AIInterviewReport:
        """Retrieve interview report with authorization check."""
        session = cls.get_session(db, interview_id, current_user)
        report = db.query(AIInterviewReport).filter(AIInterviewReport.interview_id == session.id).first()
        if not report:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Interview report is not yet generated. Complete the interview session first.",
            )
        return report

    @classmethod
    def get_student_history(
        cls, db: Session, user: User, page: int = 1, limit: int = 20
    ) -> Dict[str, Any]:
        """Retrieve paginated student interview history."""
        offset = (page - 1) * limit
        query = db.query(AIInterviewSession).filter(AIInterviewSession.user_id == user.id)
        total = query.count()
        items = query.order_by(AIInterviewSession.started_at.desc()).offset(offset).limit(limit).all()

        return {
            "total": total,
            "page": page,
            "limit": limit,
            "items": items,
        }
