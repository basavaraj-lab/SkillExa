from typing import List, Optional
from fastapi import HTTPException, UploadFile, status
from sqlalchemy.orm import Session
from backend.app.models.note import PDFNote, VisibilityEnum
from backend.app.models.user import FacultyProfile, StudentProfile
from backend.app.services.college_service import CollegeService
from backend.app.utils.file_storage import delete_stored_file, save_uploaded_pdf


class PDFService:
    @staticmethod
    async def upload_pdf(
        db: Session,
        faculty: FacultyProfile,
        file: UploadFile,
        title: str,
        subject: str,
        topic: str,
        subtopic: Optional[str] = None,
        visibility: VisibilityEnum = VisibilityEnum.COLLEGE,
        target_departments: Optional[List[str]] = None,
        target_years: Optional[List[str]] = None,
        target_sections: Optional[List[str]] = None,
        note_id: Optional[str] = None,
    ) -> PDFNote:
        file_path, file_name, file_size_bytes = await save_uploaded_pdf(file)

        pdf_note = PDFNote(
            faculty_id=faculty.id,
            college_id=faculty.college_id,
            note_id=note_id,
            title=title.strip(),
            subject=subject.strip(),
            topic=topic.strip(),
            subtopic=subtopic.strip() if subtopic else None,
            file_path=file_path,
            file_name=file_name,
            file_size_bytes=file_size_bytes,
            mime_type="application/pdf",
            version=1,
            visibility=visibility,
            published=True,
            target_departments=target_departments or [faculty.department],
            target_years=target_years or [],
            target_sections=target_sections or [],
        )
        db.add(pdf_note)
        db.commit()
        db.refresh(pdf_note)
        return pdf_note

    @staticmethod
    async def replace_pdf(
        db: Session,
        pdf_id: str,
        faculty: FacultyProfile,
        file: UploadFile,
    ) -> PDFNote:
        pdf_note = db.query(PDFNote).filter(PDFNote.id == pdf_id).first()
        if not pdf_note:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="PDF Note not found.")

        if pdf_note.faculty_id != faculty.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You can only replace your own PDF notes.")

        # Save new file
        new_path, new_name, new_size = await save_uploaded_pdf(file)

        # Remove old physical file if exists
        delete_stored_file(pdf_note.file_path)

        # Update metadata and increment version
        pdf_note.file_path = new_path
        pdf_note.file_name = new_name
        pdf_note.file_size_bytes = new_size
        pdf_note.version += 1

        db.commit()
        db.refresh(pdf_note)
        return pdf_note

    @staticmethod
    def set_published_status(db: Session, pdf_id: str, faculty: FacultyProfile, published: bool) -> PDFNote:
        pdf_note = db.query(PDFNote).filter(PDFNote.id == pdf_id).first()
        if not pdf_note:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="PDF Note not found.")

        if pdf_note.faculty_id != faculty.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You can only modify your own PDF notes.")

        pdf_note.published = published
        db.commit()
        db.refresh(pdf_note)
        return pdf_note

    @staticmethod
    def delete_pdf(db: Session, pdf_id: str, faculty: FacultyProfile) -> bool:
        pdf_note = db.query(PDFNote).filter(PDFNote.id == pdf_id).first()
        if not pdf_note:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="PDF Note not found.")

        if pdf_note.faculty_id != faculty.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You can only delete your own PDF notes.")

        delete_stored_file(pdf_note.file_path)
        db.delete(pdf_note)
        db.commit()
        return True

    @staticmethod
    def get_pdfs_for_student(db: Session, student: StudentProfile, subject: Optional[str] = None, topic: Optional[str] = None) -> List[PDFNote]:
        query = db.query(PDFNote).filter(PDFNote.published == True)

        if subject:
            query = query.filter(PDFNote.subject.ilike(f"%{subject}%"))
        if topic:
            query = query.filter(PDFNote.topic.ilike(f"%{topic}%"))

        all_pdfs = query.order_by(PDFNote.created_at.desc()).all()
        accessible = []

        for p in all_pdfs:
            if p.visibility == VisibilityEnum.COMMUNITY:
                accessible.append(p)
            elif student.college_id and p.college_id == student.college_id:
                if CollegeService.matches_student_targeting(
                    p.college_id,
                    p.target_departments,
                    p.target_years,
                    p.target_sections,
                    p.target_student_ids,
                    student,
                ):
                    accessible.append(p)

        return accessible
