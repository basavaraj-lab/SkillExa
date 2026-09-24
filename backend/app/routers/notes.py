from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from backend.app.dependencies.auth import get_current_user, require_approved_faculty
from backend.app.dependencies.db import get_db
from backend.app.models.note import FacultyNote
from backend.app.models.user import FacultyProfile, User
from backend.app.schemas.common import ApiResponse
from backend.app.schemas.note import CreateNoteRequest, NoteResponse, UpdateNoteRequest
from backend.app.services.note_service import NoteService
from backend.app.services.notification_service import NotificationService

router = APIRouter(tags=["Faculty Notes"])


@router.post("/faculty/notes", response_model=ApiResponse[NoteResponse], status_code=status.HTTP_201_CREATED)
def create_faculty_note(
    req: CreateNoteRequest,
    faculty: FacultyProfile = Depends(require_approved_faculty),
    db: Session = Depends(get_db),
):
    note = NoteService.create_note(db, faculty, req)

    # If college targeted, dispatch in-app notification to college students
    if note.visibility.value != "community" and note.published:
        NotificationService.notify_targeted_students(
            db=db,
            college_id=note.college_id,
            target_departments=note.target_departments,
            target_years=note.target_years,
            target_sections=note.target_sections,
            target_student_ids=note.target_student_ids,
            notification_type="NEW_NOTE",
            title="📚 New Faculty Note Published",
            message=f"{faculty.user.name if faculty.user else 'Faculty'} published '{note.title}' for {note.topic}.",
            reference_id=note.id,
            action_route="/topic-learning",
            action_params={"topic": note.topic, "subject": note.subject, "section": note.section},
        )
    elif note.visibility.value == "community" and note.published:
        # Notify faculty followers
        NotificationService.notify_faculty_followers(
            db=db,
            faculty_user_id=faculty.user_id,
            title="🌍 New Community Note",
            message=f"{faculty.user.name if faculty.user else 'Faculty'} shared '{note.title}' in the SkillExa Community.",
            reference_id=note.id,
            action_route="/topic-learning",
            action_params={"topic": note.topic, "subject": note.subject, "section": note.section},
        )

    return ApiResponse(
        success=True,
        message="Faculty note created successfully.",
        data=note,
    )


@router.get("/faculty/notes", response_model=ApiResponse[List[NoteResponse]])
def get_my_faculty_notes(
    faculty: FacultyProfile = Depends(require_approved_faculty),
    db: Session = Depends(get_db),
):
    notes = db.query(FacultyNote).filter(FacultyNote.faculty_id == faculty.id).order_by(FacultyNote.created_at.desc()).all()
    return ApiResponse(
        success=True,
        message="Faculty notes retrieved.",
        data=notes,
    )


@router.get("/faculty/notes/{id}", response_model=ApiResponse[NoteResponse])
def get_faculty_note_by_id(
    id: str,
    faculty: FacultyProfile = Depends(require_approved_faculty),
    db: Session = Depends(get_db),
):
    note = db.query(FacultyNote).filter(FacultyNote.id == id).first()
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found.")
    return ApiResponse(
        success=True,
        message="Note details retrieved.",
        data=note,
    )


@router.put("/faculty/notes/{id}", response_model=ApiResponse[NoteResponse])
def update_faculty_note(
    id: str,
    req: UpdateNoteRequest,
    faculty: FacultyProfile = Depends(require_approved_faculty),
    db: Session = Depends(get_db),
):
    note = NoteService.update_note(db, id, faculty, req)
    return ApiResponse(
        success=True,
        message="Note updated successfully.",
        data=note,
    )


@router.delete("/faculty/notes/{id}", response_model=ApiResponse[dict])
def delete_faculty_note(
    id: str,
    faculty: FacultyProfile = Depends(require_approved_faculty),
    db: Session = Depends(get_db),
):
    NoteService.delete_note(db, id, faculty)
    return ApiResponse(
        success=True,
        message="Note deleted successfully.",
        data={"id": id, "deleted": True},
    )


@router.post("/faculty/notes/{id}/publish", response_model=ApiResponse[NoteResponse])
def publish_note(
    id: str,
    faculty: FacultyProfile = Depends(require_approved_faculty),
    db: Session = Depends(get_db),
):
    note = NoteService.set_published_status(db, id, faculty, published=True)
    return ApiResponse(
        success=True,
        message="Note published successfully.",
        data=note,
    )


@router.post("/faculty/notes/{id}/unpublish", response_model=ApiResponse[NoteResponse])
def unpublish_note(
    id: str,
    faculty: FacultyProfile = Depends(require_approved_faculty),
    db: Session = Depends(get_db),
):
    note = NoteService.set_published_status(db, id, faculty, published=False)
    return ApiResponse(
        success=True,
        message="Note unpublished.",
        data=note,
    )


@router.get("/notes", response_model=ApiResponse[List[NoteResponse]])
def get_public_or_topic_notes(
    subject: Optional[str] = Query(None),
    topic: Optional[str] = Query(None),
    db: Session = Depends(get_db),
):
    """Retrieve notes for specific topic."""
    query = db.query(FacultyNote).filter(FacultyNote.published == True)
    if subject:
        query = query.filter(FacultyNote.subject.ilike(f"%{subject}%"))
    if topic:
        query = query.filter(FacultyNote.topic.ilike(f"%{topic}%"))
    notes = query.order_by(FacultyNote.created_at.desc()).all()
    return ApiResponse(
        success=True,
        message="Topic notes retrieved.",
        data=notes,
    )
