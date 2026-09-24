from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from backend.app.dependencies.db import get_db
from backend.app.models.note import FacultyNote, PDFNote, VisibilityEnum
from backend.app.models.quiz import Quiz
from backend.app.models.user import VerificationStatusEnum
from backend.app.models.video import FacultyVideo
from backend.app.schemas.common import ApiResponse, PaginatedResponse
from backend.app.schemas.community import CommunityContentItemResponse

router = APIRouter(prefix="/community", tags=["SkillExa Community"])


@router.get("/content", response_model=ApiResponse[PaginatedResponse[CommunityContentItemResponse]])
def get_community_content(
    search: Optional[str] = Query(None, description="Search query"),
    category: Optional[str] = Query("all", description="'all', 'engineering', 'competitive', 'programming', 'dsa'"),
    content_type: Optional[str] = Query("all", description="'all', 'notes', 'pdf', 'quiz', 'video'"),
    subject: Optional[str] = Query(None),
    topic: Optional[str] = Query(None),
    language: Optional[str] = Query(None),
    college_id: Optional[str] = Query(None),
    faculty_id: Optional[str] = Query(None),
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
):
    """
    Section 14: SkillExa Community Feed.
    Returns all public, approved faculty content (notes, pdfs, quizzes, videos) across all colleges.
    """
    items: List[CommunityContentItemResponse] = []

    # 1. Faculty Notes (published == True, visibility == COMMUNITY)
    if content_type in ["all", "notes", "note"]:
        notes = (
            db.query(FacultyNote)
            .filter(
                FacultyNote.published == True,
                FacultyNote.visibility == VisibilityEnum.COMMUNITY,
            )
            .all()
        )
        for n in notes:
            fac = n.faculty
            if fac and fac.verification_status == VerificationStatusEnum.APPROVED:
                user = fac.user
                college = fac.college
                items.append(
                    CommunityContentItemResponse(
                        id=f"comm-note-{n.id}",
                        type="note",
                        title=n.title,
                        subject=n.subject,
                        topic=n.topic,
                        subtopic=n.subtopic,
                        language=n.language,
                        faculty_id=fac.id,
                        faculty_name=user.name if user else "Faculty",
                        faculty_designation=fac.designation,
                        college_id=college.id if college else None,
                        college_name=college.name if college else "Partner College",
                        is_verified_faculty=True,
                        published_date=n.created_at.strftime("%b %d, %Y"),
                        summary=n.description or n.content[:150] + "...",
                        duration=None,
                        questions_count=None,
                        rating=4.9,
                        views_count=n.views_count,
                        target_params={
                            "section": n.section,
                            "subject": n.subject,
                            "topic": n.topic,
                            "subtopic": n.subtopic,
                            "noteId": n.id,
                        },
                    )
                )

    # 2. PDF Notes
    if content_type in ["all", "pdf", "pdfs"]:
        pdfs = (
            db.query(PDFNote)
            .filter(
                PDFNote.published == True,
                PDFNote.visibility == VisibilityEnum.COMMUNITY,
            )
            .all()
        )
        for p in pdfs:
            fac = p.faculty
            if fac and fac.verification_status == VerificationStatusEnum.APPROVED:
                user = fac.user
                college = fac.college
                items.append(
                    CommunityContentItemResponse(
                        id=f"comm-pdf-{p.id}",
                        type="pdf",
                        title=p.title,
                        subject=p.subject,
                        topic=p.topic,
                        subtopic=p.subtopic,
                        language=None,
                        faculty_id=fac.id,
                        faculty_name=user.name if user else "Faculty",
                        faculty_designation=fac.designation,
                        college_id=college.id if college else None,
                        college_name=college.name if college else "Partner College",
                        is_verified_faculty=True,
                        published_date=p.created_at.strftime("%b %d, %Y"),
                        summary=f"Curated PDF Guide ({round(p.file_size_bytes / (1024*1024), 2)} MB) • v{p.version}",
                        duration=None,
                        questions_count=None,
                        rating=4.9,
                        views_count=p.downloads_count,
                        target_params={
                            "section": "engineering",
                            "subject": p.subject,
                            "topic": p.topic,
                            "pdfId": p.id,
                        },
                    )
                )

    # 3. Quizzes
    if content_type in ["all", "quiz", "quizzes"]:
        quizzes = (
            db.query(Quiz)
            .filter(
                Quiz.published == True,
                Quiz.visibility == VisibilityEnum.COMMUNITY,
            )
            .all()
        )
        for q in quizzes:
            fac = q.faculty
            if fac and fac.verification_status == VerificationStatusEnum.APPROVED:
                user = fac.user
                college = fac.college
                items.append(
                    CommunityContentItemResponse(
                        id=f"comm-quiz-{q.id}",
                        type="quiz",
                        title=q.title,
                        subject=q.subject,
                        topic=q.topic,
                        subtopic=q.subtopic,
                        language=q.language,
                        faculty_id=fac.id,
                        faculty_name=user.name if user else "Faculty",
                        faculty_designation=fac.designation,
                        college_id=college.id if college else None,
                        college_name=college.name if college else "Partner College",
                        is_verified_faculty=True,
                        published_date=q.created_at.strftime("%b %d, %Y"),
                        summary=q.description or f"{len(q.questions)} Multi-Concept MCQs • {q.duration_minutes} Mins",
                        duration=f"{q.duration_minutes} mins",
                        questions_count=len(q.questions),
                        rating=4.95,
                        views_count=240,
                        target_params={
                            "section": q.section,
                            "subject": q.subject,
                            "topic": q.topic,
                            "quizId": q.id,
                        },
                    )
                )

    # 4. Videos
    if content_type in ["all", "video", "videos"]:
        videos = (
            db.query(FacultyVideo)
            .filter(
                FacultyVideo.published == True,
                FacultyVideo.visibility == VisibilityEnum.COMMUNITY,
            )
            .all()
        )
        for v in videos:
            fac = v.faculty
            if fac and fac.verification_status == VerificationStatusEnum.APPROVED:
                user = fac.user
                college = fac.college
                items.append(
                    CommunityContentItemResponse(
                        id=f"comm-video-{v.id}",
                        type="video",
                        title=v.title,
                        subject=v.subject,
                        topic=v.topic,
                        subtopic=v.subtopic,
                        language=v.language,
                        faculty_id=fac.id,
                        faculty_name=user.name if user else "Faculty",
                        faculty_designation=fac.designation,
                        college_id=college.id if college else None,
                        college_name=college.name if college else "Partner College",
                        is_verified_faculty=True,
                        published_date=v.created_at.strftime("%b %d, %Y"),
                        summary=v.description,
                        duration=v.duration,
                        questions_count=None,
                        rating=4.9,
                        views_count=v.views_count,
                        target_params={
                            "section": v.section,
                            "subject": v.subject,
                            "topic": v.topic,
                            "videoId": v.id,
                        },
                    )
                )

    # Apply Filter Criteria
    filtered = []
    for item in items:
        # Search query
        if search and search.strip():
            sq = search.lower().strip()
            match = (
                sq in item.title.lower()
                or sq in item.subject.lower()
                or sq in item.topic.lower()
                or sq in item.faculty_name.lower()
                or sq in item.college_name.lower()
            )
            if not match:
                continue

        # Category
        if category and category != "all":
            if category == "engineering" and "engineering" not in item.target_params.get("section", ""):
                continue
            if category == "competitive" and "competitive" not in item.target_params.get("section", ""):
                continue

        # Subject
        if subject and subject.strip():
            if subject.lower() not in item.subject.lower():
                continue

        # Topic
        if topic and topic.strip():
            if topic.lower() not in item.topic.lower():
                continue

        # Language
        if language and language.strip():
            if item.language != language:
                continue

        # College ID
        if college_id and item.college_id != college_id:
            continue

        # Faculty ID
        if faculty_id and item.faculty_id != faculty_id:
            continue

        filtered.append(item)

    # Sort & Paginate
    total = len(filtered)
    total_pages = (total + limit - 1) // limit if total > 0 else 0
    start_idx = (page - 1) * limit
    end_idx = start_idx + limit
    paginated_items = filtered[start_idx:end_idx]

    return ApiResponse(
        success=True,
        message=f"Retrieved {len(paginated_items)} community items.",
        data=PaginatedResponse(
            items=paginated_items,
            page=page,
            limit=limit,
            total=total,
            total_pages=total_pages,
        ),
    )
