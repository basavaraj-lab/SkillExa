from typing import List, Optional
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from backend.app.models.note import FacultyNote, VisibilityEnum
from backend.app.models.user import FacultyProfile, StudentProfile
from backend.app.schemas.note import CreateNoteRequest, UpdateNoteRequest
from backend.app.services.college_service import CollegeService


class NoteService:
    @staticmethod
    def create_note(db: Session, faculty: FacultyProfile, req: CreateNoteRequest) -> FacultyNote:
        note = FacultyNote(
            faculty_id=faculty.id,
            college_id=faculty.college_id,
            title=req.title.strip(),
            description=req.description.strip() if req.description else None,
            content=req.content.strip(),
            section=req.section.strip(),
            subject=req.subject.strip(),
            topic=req.topic.strip(),
            subtopic=req.subtopic.strip() if req.subtopic else None,
            language=req.language.strip() if req.language else None,
            important_concepts=req.important_concepts or [],
            quick_revision=req.quick_revision.strip() if req.quick_revision else None,
            visibility=req.visibility,
            published=req.published,
            target_departments=req.target_departments or [faculty.department],
            target_years=req.target_years or [],
            target_sections=req.target_sections or [],
            target_student_ids=req.target_student_ids or [],
        )
        db.add(note)
        db.commit()
        db.refresh(note)
        return note

    @staticmethod
    def update_note(db: Session, note_id: str, faculty: FacultyProfile, req: UpdateNoteRequest) -> FacultyNote:
        note = db.query(FacultyNote).filter(FacultyNote.id == note_id).first()
        if not note:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found.")

        if note.faculty_id != faculty.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You can only edit your own notes.")

        update_data = req.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(note, key, value)

        db.commit()
        db.refresh(note)
        return note

    @staticmethod
    def set_published_status(db: Session, note_id: str, faculty: FacultyProfile, published: bool) -> FacultyNote:
        note = db.query(FacultyNote).filter(FacultyNote.id == note_id).first()
        if not note:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found.")

        if note.faculty_id != faculty.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You can only modify your own notes.")

        note.published = published
        db.commit()
        db.refresh(note)
        return note

    @staticmethod
    def delete_note(db: Session, note_id: str, faculty: FacultyProfile) -> bool:
        note = db.query(FacultyNote).filter(FacultyNote.id == note_id).first()
        if not note:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found.")

        if note.faculty_id != faculty.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You can only delete your own notes.")

        db.delete(note)
        db.commit()
        return True

    @staticmethod
    def get_notes_for_student(db: Session, student: StudentProfile, subject: Optional[str] = None, topic: Optional[str] = None) -> List[FacultyNote]:
        query = db.query(FacultyNote).filter(FacultyNote.published == True)

        if subject:
            query = query.filter(FacultyNote.subject.ilike(f"%{subject}%"))
        if topic:
            query = query.filter(FacultyNote.topic.ilike(f"%{topic}%"))

        all_notes = query.order_by(FacultyNote.created_at.desc()).all()
        accessible = []

        for n in all_notes:
            if n.visibility == VisibilityEnum.COMMUNITY:
                accessible.append(n)
            elif student.college_id and n.college_id == student.college_id:
                if CollegeService.matches_student_targeting(
                    n.college_id,
                    n.target_departments,
                    n.target_years,
                    n.target_sections,
                    n.target_student_ids,
                    student,
                ):
                    accessible.append(n)

        return accessible
