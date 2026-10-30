import os
import uuid
from typing import List, Optional
from fastapi import APIRouter, Depends, File, Form, HTTPException, Query, UploadFile, status
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from backend.app.dependencies.auth import get_optional_faculty, require_approved_faculty
from backend.app.dependencies.db import get_db
from backend.app.models.note import FacultyNote, PDFNote, VisibilityEnum
from backend.app.models.notification import Notification
from backend.app.models.user import FacultyProfile, User
from backend.app.schemas.common import ApiResponse
from backend.app.schemas.note import CreateNoteRequest, NoteResponse, UpdateNoteRequest
from backend.app.services.note_service import NoteService
from backend.app.services.notification_service import NotificationService
from backend.app.utils.file_storage import save_uploaded_note_file

router = APIRouter(tags=["Faculty Notes"])


def sync_note_to_competitive_json(note: FacultyNote, file_path: Optional[str] = None):
    """Sync published competitive note into the competitive portal database (skillexa.json)"""
    try:
        import json
        import shutil
        json_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../../../competative-skillexa/server/data/skillexa.json")
        )
        if not os.path.exists(json_path):
            return

        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if "notes" not in data or not isinstance(data["notes"], list):
            data["notes"] = []

        existing = next((n for n in data["notes"] if n.get("title") == note.title or str(n.get("id")) == str(note.id)), None)
        target_file_url = ""
        target_file_name = note.file_name or f"{note.title}.pdf"
        if file_path and os.path.exists(file_path):
            dest_dir = os.path.abspath(
                os.path.join(os.path.dirname(__file__), "../../../competative-skillexa/server/uploads/notes")
            )
            os.makedirs(dest_dir, exist_ok=True)
            dest_filename = f"{note.id}_{os.path.basename(file_path)}"
            dest_full_path = os.path.join(dest_dir, dest_filename)
            try:
                shutil.copyfile(file_path, dest_full_path)
                target_file_url = f"/uploads/notes/{dest_filename}"
            except Exception:
                pass
        elif note.download_url:
            target_file_url = f"http://localhost:8000{note.download_url}"

        file_size_str = "1.2 MB"
        if note.file_size_bytes:
            kb = note.file_size_bytes / 1024
            if kb < 1024:
                file_size_str = f"{kb:.1f} KB"
            else:
                file_size_str = f"{kb/1024:.1f} MB"

        max_id = max([int(n.get("id", 0)) for n in data["notes"] if str(n.get("id", "")).isdigit()] or [0])
        now_iso = note.created_at.isoformat() if hasattr(note.created_at, "isoformat") else str(note.created_at)

        note_entry = {
            "id": existing["id"] if existing else max_id + 1,
            "title": note.title,
            "file_name": target_file_name,
            "file_url": target_file_url or (existing.get("file_url") if existing else ""),
            "file_path": "",
            "subject_name": note.subject,
            "topic_name": note.topic or note.title,
            "subtopic_name": note.subtopic or "",
            "description": note.description or "",
            "source": "KVG Faculty Study Material",
            "file_size": file_size_str,
            "file_bytes": note.file_size_bytes or 1200000,
            "page_count": None,
            "status": "PUBLISHED",
            "uploaded_by": "Dr. Ramesh Kumar",
            "created_at": now_iso,
            "updated_at": now_iso,
        }

        if existing:
            existing.update(note_entry)
        else:
            data["notes"].insert(0, note_entry)

        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Notice: sync_note_to_competitive_json failed: {e}")


def remove_note_from_competitive_json(note_id: str, title: Optional[str] = None):
    try:
        import json
        json_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../../../competative-skillexa/server/data/skillexa.json")
        )
        if not os.path.exists(json_path):
            return

        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if "notes" in data and isinstance(data["notes"], list):
            data["notes"] = [
                n for n in data["notes"]
                if str(n.get("id")) != str(note_id) and (not title or n.get("title") != title)
            ]
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Notice: remove_note_from_competitive_json failed: {e}")


@router.post("/faculty/notes/upload", response_model=ApiResponse[NoteResponse], status_code=status.HTTP_201_CREATED)
@router.post("/notes/upload", response_model=ApiResponse[NoteResponse], status_code=status.HTTP_201_CREATED)
async def upload_faculty_note(
    title: str = Form(...),
    description: Optional[str] = Form(""),
    subject: str = Form("General Engineering"),
    topic: Optional[str] = Form(None),
    subtopic: Optional[str] = Form(None),
    section: str = Form("engineering"),
    visibility: VisibilityEnum = Form(VisibilityEnum.COLLEGE),
    file: Optional[UploadFile] = File(None),
    faculty: Optional[FacultyProfile] = Depends(get_optional_faculty),
    db: Session = Depends(get_db),
):
    """
    Simplified Faculty Notes Upload:
    Accepts Notes Name (title), Description, Subject, and an uploaded file (PDF, Docx, etc.),
    and persists it in SQLite DB and disk storage for KVG College of Engineering students.
    """
    effective_faculty = faculty or db.query(FacultyProfile).first()
    note_id = str(uuid.uuid4())
    file_path = None
    file_name = None
    file_size_bytes = None
    mime_type = "application/pdf"

    if file and file.filename:
        file_path, file_name, file_size_bytes, mime_type = await save_uploaded_note_file(file)

    download_url = f"/api/notes/{note_id}/download" if file_path else None
    topic_val = (topic or title).strip()

    note = FacultyNote(
        id=note_id,
        faculty_id=effective_faculty.id if effective_faculty else "fac-101",
        college_id=effective_faculty.college_id if effective_faculty else "clg-kvg",
        title=title.strip(),
        description=description.strip() if description else "",
        content=description.strip() if description else f"Notes on {title}",
        section=section,
        subject=subject.strip(),
        topic=topic_val,
        subtopic=subtopic.strip() if subtopic else "",
        file_path=file_path,
        file_name=file_name,
        file_size_bytes=file_size_bytes,
        download_url=download_url,
        visibility=visibility,
        published=True,
        target_departments=[effective_faculty.department] if effective_faculty else ["ECE"],
    )
    db.add(note)
    db.commit()
    db.refresh(note)

    # If physical file was attached, also insert into PDFNote for backward compatibility
    if file_path and file_name:
        try:
            pdf_note = PDFNote(
                id=str(uuid.uuid4()),
                note_id=note.id,
                faculty_id=effective_faculty.id if effective_faculty else "fac-101",
                college_id=effective_faculty.college_id if effective_faculty else "clg-kvg",
                title=title.strip(),
                subject=subject.strip(),
                topic=topic_val,
                subtopic=subtopic.strip() if subtopic else "",
                file_path=file_path,
                file_name=file_name,
                file_size_bytes=file_size_bytes or 0,
                mime_type=mime_type,
                visibility=visibility,
                published=True,
            )
            db.add(pdf_note)
            db.commit()
        except Exception:
            pass

    # Notify students
    try:
        NotificationService.notify_targeted_students(
            db=db,
            college_id=note.college_id,
            target_departments=note.target_departments,
            target_years=[],
            target_sections=[],
            target_student_ids=[],
            notification_type="NEW_NOTE",
            title="📚 New Faculty Notes Published",
            message=f"New notes '{note.title}' uploaded for {note.subject}.",
            reference_id=note.id,
            action_route="/my-college",
            action_params={"note_id": note.id},
        )
    except Exception:
        pass

    # Seamlessly mirror to Competitive Exams platform database
    if section.lower() in ["competitive", "competitive exams"]:
        sync_note_to_competitive_json(note, file_path)

    return ApiResponse(
        success=True,
        message="Faculty notes uploaded and published successfully!",
        data=note,
    )


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
    faculty: Optional[FacultyProfile] = Depends(get_optional_faculty),
    db: Session = Depends(get_db),
):
    query = db.query(FacultyNote)
    if faculty:
        query = query.filter(FacultyNote.faculty_id == faculty.id)
    notes = query.order_by(FacultyNote.created_at.desc()).all()
    for n in notes:
        if n.file_path and not n.download_url:
            n.download_url = f"/api/notes/{n.id}/download"
    return ApiResponse(
        success=True,
        message="Faculty notes retrieved.",
        data=notes,
    )


@router.get("/notes/{id}/download")
def download_note_file(
    id: str,
    db: Session = Depends(get_db),
):
    note = db.query(FacultyNote).filter(FacultyNote.id == id).first()
    if note and note.file_path and os.path.exists(note.file_path):
        return FileResponse(
            path=note.file_path,
            filename=note.file_name or f"{note.title}.pdf",
            media_type="application/octet-stream",
        )

    # Check PDFNote table fallback
    pdf = db.query(PDFNote).filter((PDFNote.id == id) | (PDFNote.note_id == id)).first()
    if pdf and pdf.file_path and os.path.exists(pdf.file_path):
        return FileResponse(
            path=pdf.file_path,
            filename=pdf.file_name,
            media_type=pdf.mime_type or "application/pdf",
        )

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Physical note file missing from storage.")


@router.get("/faculty/notes/{id}", response_model=ApiResponse[NoteResponse])
def get_faculty_note_by_id(
    id: str,
    faculty: Optional[FacultyProfile] = Depends(get_optional_faculty),
    db: Session = Depends(get_db),
):
    note = db.query(FacultyNote).filter(FacultyNote.id == id).first()
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found.")
    if note.file_path and not note.download_url:
        note.download_url = f"/api/notes/{note.id}/download"
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
@router.delete("/notes/{id}", response_model=ApiResponse[dict])
def delete_faculty_note(
    id: str,
    faculty: Optional[FacultyProfile] = Depends(get_optional_faculty),
    db: Session = Depends(get_db),
):
    deleted_count = 0
    # 1. Check and delete FacultyNote
    note = db.query(FacultyNote).filter(FacultyNote.id == id).first()
    if note:
        # Remove physical file on disk if exists
        if note.file_path and os.path.exists(note.file_path):
            try:
                os.remove(note.file_path)
            except Exception as e:
                logger.warning(f"Could not remove note file {note.file_path}: {e}")

        # Delete any associated PDFNote records
        pdf_notes = db.query(PDFNote).filter((PDFNote.note_id == id) | (PDFNote.id == id)).all()
        for p in pdf_notes:
            if p.file_path and os.path.exists(p.file_path) and p.file_path != note.file_path:
                try:
                    os.remove(p.file_path)
                except Exception:
                    pass
            db.delete(p)

        db.delete(note)
        deleted_count += 1
    else:
        # Check PDFNote standalone record
        pdf = db.query(PDFNote).filter((PDFNote.id == id) | (PDFNote.note_id == id)).first()
        if pdf:
            if pdf.file_path and os.path.exists(pdf.file_path):
                try:
                    os.remove(pdf.file_path)
                except Exception:
                    pass
            db.delete(pdf)
            deleted_count += 1

    # Cascade delete any notifications referencing this note
    db.query(Notification).filter(Notification.reference_id == id).delete(synchronize_session=False)

    db.commit()

    # Mirror deletion to competitive exams platform
    try:
        remove_note_from_competitive_json(id, note.title if note else None)
    except Exception:
        pass

    return ApiResponse(
        success=True,
        message="Note and physical files permanently deleted from database.",
        data={"id": id, "deleted": True, "count": deleted_count},
    )


@router.post("/faculty/notes/{id}/publish", response_model=ApiResponse[NoteResponse])
def publish_note(
    id: str,
    faculty: Optional[FacultyProfile] = Depends(get_optional_faculty),
    db: Session = Depends(get_db),
):
    note = db.query(FacultyNote).filter(FacultyNote.id == id).first()
    if note:
        note.published = True
        db.commit()
        db.refresh(note)
    return ApiResponse(
        success=True,
        message="Note published successfully.",
        data=note,
    )


@router.post("/faculty/notes/{id}/unpublish", response_model=ApiResponse[NoteResponse])
def unpublish_note(
    id: str,
    faculty: Optional[FacultyProfile] = Depends(get_optional_faculty),
    db: Session = Depends(get_db),
):
    note = db.query(FacultyNote).filter(FacultyNote.id == id).first()
    if note:
        note.published = False
        db.commit()
        db.refresh(note)
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
    """Retrieve all published faculty notes."""
    query = db.query(FacultyNote).filter(FacultyNote.published == True)
    if subject:
        query = query.filter(FacultyNote.subject.ilike(f"%{subject}%"))
    if topic:
        query = query.filter(FacultyNote.topic.ilike(f"%{topic}%"))
    notes = query.order_by(FacultyNote.created_at.desc()).all()
    for n in notes:
        if n.file_path and not n.download_url:
            n.download_url = f"/api/notes/{n.id}/download"
    return ApiResponse(
        success=True,
        message="Topic notes retrieved.",
        data=notes,
    )
