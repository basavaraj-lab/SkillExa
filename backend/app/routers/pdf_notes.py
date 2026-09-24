import os
from typing import List, Optional
from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile, status
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from backend.app.dependencies.auth import require_approved_faculty
from backend.app.dependencies.db import get_db
from backend.app.models.note import PDFNote, VisibilityEnum
from backend.app.models.user import FacultyProfile
from backend.app.schemas.common import ApiResponse
from backend.app.schemas.note import PDFNoteResponse
from backend.app.services.notification_service import NotificationService
from backend.app.services.pdf_service import PDFService

router = APIRouter(prefix="/faculty/pdf-notes", tags=["Faculty PDF Notes"])


@router.post("", response_model=ApiResponse[PDFNoteResponse], status_code=status.HTTP_201_CREATED)
async def upload_pdf_note(
    file: UploadFile = File(...),
    title: str = Form(...),
    subject: str = Form(...),
    topic: str = Form(...),
    subtopic: Optional[str] = Form(None),
    visibility: VisibilityEnum = Form(VisibilityEnum.COLLEGE),
    note_id: Optional[str] = Form(None),
    faculty: FacultyProfile = Depends(require_approved_faculty),
    db: Session = Depends(get_db),
):
    pdf = await PDFService.upload_pdf(
        db=db,
        faculty=faculty,
        file=file,
        title=title,
        subject=subject,
        topic=topic,
        subtopic=subtopic,
        visibility=visibility,
        note_id=note_id,
    )

    # Dispatch targeted notification
    if visibility.value != "community":
        NotificationService.notify_targeted_students(
            db=db,
            college_id=faculty.college_id,
            target_departments=[faculty.department],
            target_years=[],
            target_sections=[],
            target_student_ids=[],
            notification_type="NEW_PDF",
            title="📄 New PDF Guide Attached",
            message=f"{faculty.user.name if faculty.user else 'Faculty'} uploaded '{pdf.title}' ({pdf.file_name}) for {pdf.topic}.",
            reference_id=pdf.id,
            action_route="/topic-learning",
            action_params={"topic": pdf.topic, "subject": pdf.subject},
        )

    return ApiResponse(
        success=True,
        message="PDF note uploaded successfully!",
        data=PDFNoteResponse(
            id=pdf.id,
            note_id=pdf.note_id,
            faculty_id=pdf.faculty_id,
            faculty_name=faculty.user.name if faculty.user else "Faculty",
            college_id=pdf.college_id,
            college_name=faculty.college.name if faculty.college else "College",
            title=pdf.title,
            subject=pdf.subject,
            topic=pdf.topic,
            subtopic=pdf.subtopic,
            file_name=pdf.file_name,
            file_size_bytes=pdf.file_size_bytes,
            mime_type=pdf.mime_type,
            version=pdf.version,
            download_url=f"/api/faculty/pdf-notes/{pdf.id}/download",
            visibility=pdf.visibility,
            published=pdf.published,
            downloads_count=pdf.downloads_count,
            created_at=pdf.created_at,
            updated_at=pdf.updated_at,
        ),
    )


@router.get("", response_model=ApiResponse[List[PDFNoteResponse]])
def get_my_pdf_notes(
    faculty: FacultyProfile = Depends(require_approved_faculty),
    db: Session = Depends(get_db),
):
    pdfs = db.query(PDFNote).filter(PDFNote.faculty_id == faculty.id).order_by(PDFNote.created_at.desc()).all()
    results = [
        PDFNoteResponse(
            id=p.id,
            note_id=p.note_id,
            faculty_id=p.faculty_id,
            faculty_name=faculty.user.name if faculty.user else "Faculty",
            college_id=p.college_id,
            college_name=faculty.college.name if faculty.college else "College",
            title=p.title,
            subject=p.subject,
            topic=p.topic,
            subtopic=p.subtopic,
            file_name=p.file_name,
            file_size_bytes=p.file_size_bytes,
            mime_type=p.mime_type,
            version=p.version,
            download_url=f"/api/faculty/pdf-notes/{p.id}/download",
            visibility=p.visibility,
            published=p.published,
            downloads_count=p.downloads_count,
            created_at=p.created_at,
            updated_at=p.updated_at,
        )
        for p in pdfs
    ]
    return ApiResponse(
        success=True,
        message="Faculty PDF notes retrieved.",
        data=results,
    )


@router.get("/{id}/download")
def download_pdf_note(
    id: str,
    db: Session = Depends(get_db),
):
    pdf = db.query(PDFNote).filter(PDFNote.id == id).first()
    if not pdf:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="PDF document not found.")

    if not os.path.exists(pdf.file_path):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Physical PDF file missing from storage.")

    # Increment download counter
    pdf.downloads_count += 1
    db.commit()

    return FileResponse(
        path=pdf.file_path,
        filename=pdf.file_name,
        media_type=pdf.mime_type,
    )


@router.put("/{id}/replace", response_model=ApiResponse[PDFNoteResponse])
async def replace_pdf_note(
    id: str,
    file: UploadFile = File(...),
    faculty: FacultyProfile = Depends(require_approved_faculty),
    db: Session = Depends(get_db),
):
    """
    Section 7: Replace existing PDF file. Increments version number, updates updated_at, keeps same ID.
    """
    pdf = await PDFService.replace_pdf(db, id, faculty, file)
    return ApiResponse(
        success=True,
        message=f"PDF replaced successfully! Incremented to version v{pdf.version}.",
        data=PDFNoteResponse(
            id=pdf.id,
            note_id=pdf.note_id,
            faculty_id=pdf.faculty_id,
            faculty_name=faculty.user.name if faculty.user else "Faculty",
            college_id=pdf.college_id,
            college_name=faculty.college.name if faculty.college else "College",
            title=pdf.title,
            subject=pdf.subject,
            topic=pdf.topic,
            subtopic=pdf.subtopic,
            file_name=pdf.file_name,
            file_size_bytes=pdf.file_size_bytes,
            mime_type=pdf.mime_type,
            version=pdf.version,
            download_url=f"/api/faculty/pdf-notes/{pdf.id}/download",
            visibility=pdf.visibility,
            published=pdf.published,
            downloads_count=pdf.downloads_count,
            created_at=pdf.created_at,
            updated_at=pdf.updated_at,
        ),
    )


@router.delete("/{id}", response_model=ApiResponse[dict])
def delete_pdf_note(
    id: str,
    faculty: FacultyProfile = Depends(require_approved_faculty),
    db: Session = Depends(get_db),
):
    PDFService.delete_pdf(db, id, faculty)
    return ApiResponse(
        success=True,
        message="PDF note deleted successfully.",
        data={"id": id, "deleted": True},
    )


@router.post("/{id}/publish", response_model=ApiResponse[dict])
def publish_pdf_note(
    id: str,
    faculty: FacultyProfile = Depends(require_approved_faculty),
    db: Session = Depends(get_db),
):
    PDFService.set_published_status(db, id, faculty, published=True)
    return ApiResponse(
        success=True,
        message="PDF note published.",
        data={"id": id, "published": True},
    )


@router.post("/{id}/unpublish", response_model=ApiResponse[dict])
def unpublish_pdf_note(
    id: str,
    faculty: FacultyProfile = Depends(require_approved_faculty),
    db: Session = Depends(get_db),
):
    PDFService.set_published_status(db, id, faculty, published=False)
    return ApiResponse(
        success=True,
        message="PDF note unpublished.",
        data={"id": id, "published": False},
    )
