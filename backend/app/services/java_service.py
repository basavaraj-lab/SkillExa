"""Service layer for Java Enterprise learning flow, sequence enforcement, and database progress management."""
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.java_progress import JavaStudentProgress
from app.models.java_topic_catalog import JAVA_TOPICS

SECTION_ORDER = ["information", "examples", "programming", "fill-blanks", "test"]


def get_or_create_java_progress(db: Session, student_id: str, topic_id: int) -> JavaStudentProgress:
    """Retrieve existing Java progress or initialize standard progress state based on prerequisites."""
    progress = (
        db.query(JavaStudentProgress)
        .filter(JavaStudentProgress.student_id == str(student_id), JavaStudentProgress.topic_id == topic_id)
        .first()
    )

    if progress:
        return progress

    # Determine initial status: topic 1 is unlocked by default, otherwise dependent on previous topic completion
    if topic_id == 1:
        initial_status = "IN_PROGRESS"
    else:
        prev_progress = (
            db.query(JavaStudentProgress)
            .filter(JavaStudentProgress.student_id == str(student_id), JavaStudentProgress.topic_id == topic_id - 1)
            .first()
        )
        if prev_progress and prev_progress.topic_completed:
            initial_status = "IN_PROGRESS"
        else:
            initial_status = "LOCKED"

    progress = JavaStudentProgress(
        student_id=str(student_id),
        topic_id=topic_id,
        status=initial_status,
        current_section="information",
        information_completed=False,
        examples_completed=False,
        programming_completed=False,
        fill_blanks_completed=False,
        test_completed=False,
        test_score=0.0,
        topic_completed=False,
    )
    db.add(progress)
    db.commit()
    db.refresh(progress)
    return progress


def validate_java_topic_unlocked(progress: JavaStudentProgress):
    """Ensure the Java topic is not locked."""
    if progress.status == "LOCKED":
        raise HTTPException(
            status_code=403,
            detail="This Java topic is locked. Complete the previous topic first!",
        )


def validate_java_section_access(progress: JavaStudentProgress, target_section: str):
    """
    Enforce backend Java learning sequence:
    Information -> Examples -> Programming -> Fill in Blanks -> SkillExa Test
    """
    validate_java_topic_unlocked(progress)

    if progress.topic_completed:
        return  # Completed topics allow reviewing any section

    if target_section == "information":
        return

    if target_section == "examples":
        if not progress.information_completed:
            raise HTTPException(
                status_code=403,
                detail="Access denied: You must complete the Information section first.",
            )
        return

    if target_section == "programming":
        if not progress.examples_completed:
            raise HTTPException(
                status_code=403,
                detail="Access denied: You must complete the Examples section first.",
            )
        return

    if target_section == "fill-blanks":
        if not progress.programming_completed:
            raise HTTPException(
                status_code=403,
                detail="Access denied: You must complete the Programming section first.",
            )
        return

    if target_section == "test":
        if not progress.fill_blanks_completed:
            raise HTTPException(
                status_code=403,
                detail="Access denied: You must complete the Fill in the Blanks section first.",
            )
        return

    raise HTTPException(status_code=400, detail=f"Invalid section: {target_section}")


def complete_java_information_section(db: Session, progress: JavaStudentProgress) -> JavaStudentProgress:
    validate_java_topic_unlocked(progress)
    progress.information_completed = True
    if progress.current_section in ["information"]:
        progress.current_section = "examples"
    db.commit()
    db.refresh(progress)
    return progress


def complete_java_examples_section(db: Session, progress: JavaStudentProgress) -> JavaStudentProgress:
    validate_java_section_access(progress, "examples")
    progress.examples_completed = True
    if progress.current_section in ["information", "examples"]:
        progress.current_section = "programming"
    db.commit()
    db.refresh(progress)
    return progress


def complete_java_programming_section(db: Session, progress: JavaStudentProgress) -> JavaStudentProgress:
    validate_java_section_access(progress, "programming")
    progress.programming_completed = True
    if progress.current_section in ["information", "examples", "programming"]:
        progress.current_section = "fill-blanks"
    db.commit()
    db.refresh(progress)
    return progress


def complete_java_fill_blanks_section(db: Session, progress: JavaStudentProgress) -> JavaStudentProgress:
    validate_java_section_access(progress, "fill-blanks")
    progress.fill_blanks_completed = True
    if progress.current_section in ["information", "examples", "programming", "fill-blanks"]:
        progress.current_section = "test"
    db.commit()
    db.refresh(progress)
    return progress


def submit_java_skill_exa_test(
    db: Session,
    progress: JavaStudentProgress,
    user_answers: dict[str, str] | list[str] | None,
) -> tuple[JavaStudentProgress, float, dict | None]:
    """
    Validate Java SkillExa Test completion, compute test score, mark topic COMPLETED,
    unlock next topic in database, and return next topic info.
    """
    validate_java_section_access(progress, "test")

    topic = JAVA_TOPICS.get(progress.topic_id)
    if not topic:
        raise HTTPException(status_code=404, detail="Java Topic content not found.")

    questions = topic.get("skill_exa_test", [])
    total_questions = len(questions)
    correct_count = 0

    if total_questions > 0 and user_answers:
        if isinstance(user_answers, list):
            for i, q in enumerate(questions):
                if i < len(user_answers) and str(user_answers[i]).strip().lower() == str(q["answer"]).strip().lower():
                    correct_count += 1
        elif isinstance(user_answers, dict):
            for i, q in enumerate(questions):
                ans = user_answers.get(str(i)) or user_answers.get(q["question"])
                if ans and str(ans).strip().lower() == str(q["answer"]).strip().lower():
                    correct_count += 1
        score_percent = round((correct_count / total_questions) * 100, 1)
    else:
        score_percent = 100.0

    progress.test_completed = True
    progress.test_score = score_percent
    progress.topic_completed = True
    progress.status = "COMPLETED"
    progress.current_section = "completed"
    db.commit()

    # Unlock next topic
    next_topic_id = progress.topic_id + 1
    next_topic_info = None

    if next_topic_id in JAVA_TOPICS:
        next_progress = get_or_create_java_progress(db, progress.student_id, next_topic_id)
        if next_progress.status == "LOCKED":
            next_progress.status = "IN_PROGRESS"
            next_progress.current_section = "information"
            db.commit()
            db.refresh(next_progress)

        next_topic_raw = JAVA_TOPICS[next_topic_id]
        next_topic_info = {
            "id": next_topic_id,
            "title": next_topic_raw["title"],
            "difficulty": next_topic_raw["difficulty"],
            "duration": next_topic_raw["duration"],
            "status": next_progress.status,
            "current_section": next_progress.current_section,
        }

    db.refresh(progress)
    return progress, score_percent, next_topic_info
