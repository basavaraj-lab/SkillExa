from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.app.dependencies.auth import get_current_student
from backend.app.dependencies.db import get_db
from backend.app.models.assignment import Assignment
from backend.app.models.interview import Interview
from backend.app.models.user import FacultyFollow, FacultyProfile, StudentProfile, User
from backend.app.schemas.common import ApiResponse
from backend.app.schemas.progress import StudentStatsResponse
from backend.app.services.college_service import CollegeService
from backend.app.services.note_service import NoteService
from backend.app.services.pdf_service import PDFService
from backend.app.services.progress_service import ProgressService
from backend.app.services.quiz_service import QuizService

router = APIRouter(prefix="/student", tags=["Student"])


@router.get("/my-college", response_model=ApiResponse[dict])
def get_my_college_workspace(
    student: StudentProfile = Depends(get_current_student),
    db: Session = Depends(get_db),
):
    """
    Return all college-targeted educational content for the current enrolled student:
    - Announcements
    - Faculty Notes
    - PDF Notes
    - Active Quizzes
    - Assignments
    - Viva / Placement Interviews
    - Department Faculty Directory
    """
    college = student.college
    announcements = CollegeService.get_announcements_for_student(db, student)
    notes = NoteService.get_notes_for_student(db, student)
    pdfs = PDFService.get_pdfs_for_student(db, student)
    quizzes = QuizService.get_quizzes_for_student(db, student)

    # Assignments
    all_assignments = db.query(Assignment).filter(Assignment.published == True).all()
    filtered_assignments = [
        a for a in all_assignments
        if CollegeService.matches_student_targeting(
            a.college_id, a.target_departments, a.target_years, a.target_sections, a.target_student_ids, student
        )
    ]

    # Interviews
    interviews = (
        db.query(Interview)
        .filter(Interview.student_id == student.id)
        .order_by(Interview.scheduled_at.desc())
        .all()
    )

    # Department Faculty Directory
    faculty_list = (
        db.query(FacultyProfile)
        .filter(FacultyProfile.college_id == student.college_id, FacultyProfile.department == student.branch)
        .all()
    )

    return ApiResponse(
        success=True,
        message="My College workspace content retrieved successfully.",
        data={
            "college": {
                "id": college.id if college else None,
                "name": college.name if college else "Enrolled College",
                "code": college.code if college else "",
                "branch": student.branch,
                "academic_year": student.academic_year,
                "section": student.section,
            },
            "announcements": [
                {
                    "id": a.id,
                    "title": a.title,
                    "content": a.content,
                    "priority": a.priority,
                    "is_pinned": a.is_pinned,
                    "faculty_name": a.faculty_name,
                    "faculty_dept": a.faculty_dept,
                    "created_at": a.created_at.isoformat(),
                }
                for a in announcements
            ],
            "notes": [
                {
                    "id": n.id,
                    "title": n.title,
                    "subject": n.subject,
                    "topic": n.topic,
                    "content": n.content,
                    "important_concepts": n.important_concepts,
                    "quick_revision": n.quick_revision,
                    "faculty_name": n.faculty.user.name if n.faculty and n.faculty.user else "Faculty",
                    "created_at": n.created_at.isoformat(),
                }
                for n in notes
            ],
            "pdfs": [
                {
                    "id": p.id,
                    "title": p.title,
                    "subject": p.subject,
                    "topic": p.topic,
                    "file_name": p.file_name,
                    "file_size_bytes": p.file_size_bytes,
                    "version": p.version,
                    "faculty_name": p.faculty.user.name if p.faculty and p.faculty.user else "Faculty",
                    "download_url": f"/api/faculty/pdf-notes/{p.id}/download",
                }
                for p in pdfs
            ],
            "quizzes": [
                {
                    "id": q.id,
                    "title": q.title,
                    "description": q.description,
                    "subject": q.subject,
                    "topic": q.topic,
                    "duration_minutes": q.duration_minutes,
                    "total_marks": q.total_marks,
                    "questions_count": len(q.questions),
                }
                for q in quizzes
            ],
            "assignments": [
                {
                    "id": a.id,
                    "title": a.title,
                    "description": a.description,
                    "subject": a.subject,
                    "topic": a.topic,
                    "max_marks": a.max_marks,
                    "due_date": a.due_date.isoformat(),
                }
                for a in filtered_assignments
            ],
            "interviews": [
                {
                    "id": i.id,
                    "title": i.title,
                    "interview_type": i.interview_type.value,
                    "subject_or_role": i.subject_or_role,
                    "scheduled_at": i.scheduled_at.isoformat(),
                    "status": i.status.value,
                    "faculty_name": i.faculty.user.name if i.faculty and i.faculty.user else "Examiner",
                    "room_id": i.video_session.room_id if i.video_session else None,
                }
                for i in interviews
            ],
            "faculty_directory": [
                {
                    "id": f.id,
                    "name": f.user.name if f.user else "Faculty",
                    "department": f.department,
                    "designation": f.designation,
                    "office_room": f.office_room,
                    "subjects_taught": f.subjects_taught,
                    "verification_status": f.verification_status.value,
                }
                for f in faculty_list
            ],
        },
    )


@router.post("/faculty/{faculty_id}/follow", response_model=ApiResponse[dict])
def follow_faculty(
    faculty_id: str,
    student: StudentProfile = Depends(get_current_student),
    db: Session = Depends(get_db),
):
    faculty = db.query(FacultyProfile).filter((FacultyProfile.id == faculty_id) | (FacultyProfile.user_id == faculty_id)).first()
    if not faculty:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Faculty profile not found.")

    existing = db.query(FacultyFollow).filter(FacultyFollow.student_id == student.user_id, FacultyFollow.faculty_id == faculty.user_id).first()
    if not existing:
        follow = FacultyFollow(student_id=student.user_id, faculty_id=faculty.user_id)
        db.add(follow)
        db.commit()

    return ApiResponse(
        success=True,
        message=f"You are now following {faculty.user.name if faculty.user else 'Faculty'}.",
        data={"faculty_id": faculty.id, "following": True},
    )


@router.delete("/faculty/{faculty_id}/follow", response_model=ApiResponse[dict])
def unfollow_faculty(
    faculty_id: str,
    student: StudentProfile = Depends(get_current_student),
    db: Session = Depends(get_db),
):
    faculty = db.query(FacultyProfile).filter((FacultyProfile.id == faculty_id) | (FacultyProfile.user_id == faculty_id)).first()
    if faculty:
        db.query(FacultyFollow).filter(FacultyFollow.student_id == student.user_id, FacultyFollow.faculty_id == faculty.user_id).delete()
        db.commit()

    return ApiResponse(
        success=True,
        message="Unfollowed faculty member.",
        data={"following": False},
    )


@router.get("/following", response_model=ApiResponse[List[dict]])
def get_following_faculty(
    student: StudentProfile = Depends(get_current_student),
    db: Session = Depends(get_db),
):
    follows = db.query(FacultyFollow).filter(FacultyFollow.student_id == student.user_id).all()
    results = []
    for f in follows:
        user = f.faculty
        if user and user.faculty_profile:
            fp = user.faculty_profile
            results.append({
                "faculty_id": fp.id,
                "user_id": user.id,
                "name": user.name,
                "department": fp.department,
                "designation": fp.designation,
                "college_name": fp.college.name if fp.college else "Partner College",
                "is_verified": fp.verification_status.value == "APPROVED",
            })
    return ApiResponse(
        success=True,
        message="Followed faculty list retrieved.",
        data=results,
    )


@router.get("/stats", response_model=ApiResponse[StudentStatsResponse])
def get_my_stats(
    student: StudentProfile = Depends(get_current_student),
    db: Session = Depends(get_db),
):
    stats = ProgressService.get_student_stats(db, student)
    return ApiResponse(
        success=True,
        message="Student performance stats retrieved.",
        data=stats,
    )
