from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from backend.app.dependencies.auth import require_approved_faculty
from backend.app.dependencies.db import get_db
from backend.app.models.video import FacultyVideo
from backend.app.models.user import FacultyProfile
from backend.app.schemas.common import ApiResponse
from backend.app.schemas.video import (
    CreateVideoRequest,
    UpdateVideoRequest,
    VideoResponse,
)
from backend.app.services.notification_service import NotificationService

router = APIRouter(tags=["Faculty Videos"])


@router.post("/faculty/videos", response_model=ApiResponse[VideoResponse], status_code=status.HTTP_201_CREATED)
def create_faculty_video(
    req: CreateVideoRequest,
    faculty: FacultyProfile = Depends(require_approved_faculty),
    db: Session = Depends(get_db),
):
    video = FacultyVideo(
        faculty_id=faculty.id,
        college_id=faculty.college_id,
        title=req.title.strip(),
        description=req.description.strip() if req.description else None,
        video_url=req.video_url.strip(),
        thumbnail_url=req.thumbnail_url,
        duration=req.duration or "20 mins",
        section=req.section,
        subject=req.subject,
        topic=req.topic,
        subtopic=req.subtopic,
        language=req.language,
        visibility=req.visibility,
        published=req.published,
        target_departments=req.target_departments or [faculty.department],
        target_years=req.target_years or [],
        target_sections=req.target_sections or [],
        target_student_ids=req.target_student_ids or [],
    )
    db.add(video)
    db.commit()
    db.refresh(video)

    # Notify students if college targeted
    if req.visibility.value != "community" and req.published:
        NotificationService.notify_targeted_students(
            db=db,
            college_id=faculty.college_id,
            target_departments=[faculty.department],
            target_years=[],
            target_sections=[],
            target_student_ids=[],
            notification_type="NEW_VIDEO",
            title="🎥 New Video Lecture",
            message=f"{faculty.user.name if faculty.user else 'Faculty'} attached lecture '{video.title}' for {video.topic}.",
            reference_id=video.id,
            action_route="/topic-learning",
            action_params={"topic": video.topic, "subject": video.subject},
        )

    return ApiResponse(
        success=True,
        message="Video lecture published successfully!",
        data=video,
    )


@router.get("/faculty/videos", response_model=ApiResponse[List[VideoResponse]])
def get_my_videos(
    faculty: FacultyProfile = Depends(require_approved_faculty),
    db: Session = Depends(get_db),
):
    videos = db.query(FacultyVideo).filter(FacultyVideo.faculty_id == faculty.id).order_by(FacultyVideo.created_at.desc()).all()
    return ApiResponse(
        success=True,
        message="Faculty videos retrieved.",
        data=videos,
    )


@router.put("/faculty/videos/{id}", response_model=ApiResponse[VideoResponse])
def update_faculty_video(
    id: str,
    req: UpdateVideoRequest,
    faculty: FacultyProfile = Depends(require_approved_faculty),
    db: Session = Depends(get_db),
):
    video = db.query(FacultyVideo).filter(FacultyVideo.id == id).first()
    if not video:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Video not found.")
    if video.faculty_id != faculty.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You can only edit your own videos.")

    update_data = req.model_dump(exclude_unset=True)
    for key, val in update_data.items():
        setattr(video, key, val)

    db.commit()
    db.refresh(video)
    return ApiResponse(
        success=True,
        message="Video updated successfully.",
        data=video,
    )


@router.delete("/faculty/videos/{id}", response_model=ApiResponse[dict])
def delete_faculty_video(
    id: str,
    faculty: FacultyProfile = Depends(require_approved_faculty),
    db: Session = Depends(get_db),
):
    video = db.query(FacultyVideo).filter(FacultyVideo.id == id).first()
    if not video:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Video not found.")
    if video.faculty_id != faculty.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You can only delete your own videos.")

    db.delete(video)
    db.commit()
    return ApiResponse(
        success=True,
        message="Video deleted.",
        data={"id": id, "deleted": True},
    )


@router.get("/videos", response_model=ApiResponse[List[VideoResponse]])
def get_topic_videos(
    subject: Optional[str] = Query(None),
    topic: Optional[str] = Query(None),
    db: Session = Depends(get_db),
):
    query = db.query(FacultyVideo).filter(FacultyVideo.published == True)
    if subject:
        query = query.filter(FacultyVideo.subject.ilike(f"%{subject}%"))
    if topic:
        query = query.filter(FacultyVideo.topic.ilike(f"%{topic}%"))
    videos = query.order_by(FacultyVideo.created_at.desc()).all()
    return ApiResponse(
        success=True,
        message="Topic videos retrieved.",
        data=videos,
    )
