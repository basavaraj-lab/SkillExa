from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import or_
from sqlalchemy.orm import Session

from backend.app.dependencies.db import get_db
from backend.app.models.govt_job import GovtJobNotification
from backend.app.schemas.common import ApiResponse
from backend.app.schemas.govt_job import (
    GovtJobResponse,
    GovtJobScrapeResult,
    GovtJobSummary,
    GovtOrgInfo,
)
from backend.app.services.govt_job_scraper import (
    OFFICIAL_ORGANIZATIONS,
    GovtJobScraperService,
)

router = APIRouter(prefix="/govt-jobs", tags=["Government Jobs & Exam Notifications"])


@router.get("", response_model=ApiResponse[List[GovtJobResponse]])
def get_govt_jobs(
    organization: Optional[str] = Query(None, description="Filter by Organization code (e.g. SSC, UPSC, IBPS, KPSC, BSF, SSB, RRB_BENGALURU, KARNATAKA_POLICE)"),
    category: Optional[str] = Query(None, description="Filter by Category (e.g. Central Govt, Banking, Police, Railways)"),
    update_type: Optional[str] = Query(None, description="Filter by update type (RECRUITMENT, EXAM_DATE, ADMIT_CARD, RESULT)"),
    status: Optional[str] = Query(None, description="Filter by status (ACTIVE, DEADLINE_CLOSE, etc.)"),
    search: Optional[str] = Query(None, description="Keyword search in title, advt number, qualifications, description"),
    limit: int = Query(50, ge=1, le=100),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
):
    """
    List verified government recruitment notifications and exam updates.
    """
    # Auto-seed baseline on first query if table is empty
    count = db.query(GovtJobNotification).count()
    if count == 0:
        import asyncio
        try:
            loop = asyncio.get_event_loop()
            if loop.is_running():
                asyncio.ensure_future(GovtJobScraperService.run_scraper(db))
            else:
                loop.run_until_complete(GovtJobScraperService.run_scraper(db))
        except Exception:
            pass

    query = db.query(GovtJobNotification).filter(GovtJobNotification.is_active == True)

    if organization and organization != "All":
        query = query.filter(GovtJobNotification.organization == organization)

    if category and category != "All":
        query = query.filter(GovtJobNotification.category == category)

    if update_type and update_type != "All":
        query = query.filter(GovtJobNotification.update_type == update_type)

    if status and status != "All":
        query = query.filter(GovtJobNotification.status == status)

    if search and search.strip():
        q = f"%{search.strip()}%"
        query = query.filter(
            or_(
                GovtJobNotification.title.ilike(q),
                GovtJobNotification.advertisement_number.ilike(q),
                GovtJobNotification.qualification.ilike(q),
                GovtJobNotification.organization_name.ilike(q),
                GovtJobNotification.description.ilike(q),
            )
        )

    # Sort newest first
    query = query.order_by(GovtJobNotification.created_at.desc())
    items = query.offset(offset).limit(limit).all()

    return ApiResponse(
        success=True,
        message=f"Found {len(items)} government job and exam notifications.",
        data=items,
    )


@router.get("/summary", response_model=ApiResponse[GovtJobSummary])
def get_govt_jobs_summary(db: Session = Depends(get_db)):
    """
    Get aggregated recruitment and examination metrics across all official agencies.
    """
    all_notifs = db.query(GovtJobNotification).filter(GovtJobNotification.is_active == True).all()

    total_vacancies = sum([n.vacancies for n in all_notifs if n.vacancies])
    open_apps = len([n for n in all_notifs if n.update_type == "RECRUITMENT" and n.status == "ACTIVE"])
    upcoming_exams = len([n for n in all_notifs if n.exam_date])
    admit_cards = len([n for n in all_notifs if n.update_type == "ADMIT_CARD" or n.admit_card_date])
    results = len([n for n in all_notifs if n.update_type == "RESULT" or n.result_date])

    # Deadlines closing within 14 days
    today_str = datetime.utcnow().strftime("%Y-%m-%d")
    deadlines = 0
    for n in all_notifs:
        if n.application_end_date and n.application_end_date >= today_str:
            deadlines += 1

    last_scraped = None
    if all_notifs:
        dates = [n.scraped_at for n in all_notifs if n.scraped_at]
        if dates:
            last_scraped = max(dates).strftime("%Y-%m-%d %H:%M:%S UTC")

    summary = GovtJobSummary(
        total_notifications=len(all_notifs),
        active_vacancies=total_vacancies,
        open_applications=open_apps,
        upcoming_exams=upcoming_exams,
        admit_cards_live=admit_cards,
        results_announced=results,
        deadlines_this_week=deadlines,
        last_scraped_at=last_scraped or datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),
    )

    return ApiResponse(success=True, data=summary)


@router.get("/organizations", response_model=ApiResponse[List[GovtOrgInfo]])
def get_official_organizations(db: Session = Depends(get_db)):
    """
    Get the directory of 8 official government recruitment bodies with live notification counts.
    """
    orgs_info: List[GovtOrgInfo] = []

    for code, meta in OFFICIAL_ORGANIZATIONS.items():
        count = db.query(GovtJobNotification).filter(
            GovtJobNotification.organization == code,
            GovtJobNotification.is_active == True,
        ).count()

        orgs_info.append(
            GovtOrgInfo(
                code=code,
                name=meta["name"],
                official_website=meta["official_website"],
                category=meta["category"],
                badge_color=meta["badge_color"],
                active_notices_count=count,
                exam_types=meta["exam_types"],
            )
        )

    return ApiResponse(success=True, data=orgs_info)


@router.get("/latest", response_model=ApiResponse[List[GovtJobResponse]])
def get_latest_notifications(
    limit: int = Query(6, ge=1, le=20),
    db: Session = Depends(get_db),
):
    """Get the latest published government notifications."""
    items = (
        db.query(GovtJobNotification)
        .filter(GovtJobNotification.is_active == True)
        .order_by(GovtJobNotification.created_at.desc())
        .limit(limit)
        .all()
    )
    return ApiResponse(success=True, data=items)


@router.get("/upcoming-exams", response_model=ApiResponse[List[GovtJobResponse]])
def get_upcoming_exams(db: Session = Depends(get_db)):
    """Get notifications with upcoming examination dates."""
    items = (
        db.query(GovtJobNotification)
        .filter(
            GovtJobNotification.is_active == True,
            GovtJobNotification.exam_date.isnot(None),
        )
        .order_by(GovtJobNotification.created_at.desc())
        .all()
    )
    return ApiResponse(success=True, data=items)


@router.get("/admit-cards", response_model=ApiResponse[List[GovtJobResponse]])
def get_admit_cards(db: Session = Depends(get_db)):
    """Get admit cards and hall ticket releases."""
    items = (
        db.query(GovtJobNotification)
        .filter(
            GovtJobNotification.is_active == True,
            or_(
                GovtJobNotification.update_type == "ADMIT_CARD",
                GovtJobNotification.admit_card_date.isnot(None),
            ),
        )
        .order_by(GovtJobNotification.created_at.desc())
        .all()
    )
    return ApiResponse(success=True, data=items)


@router.get("/results", response_model=ApiResponse[List[GovtJobResponse]])
def get_results(db: Session = Depends(get_db)):
    """Get announced exam results and merit lists."""
    items = (
        db.query(GovtJobNotification)
        .filter(
            GovtJobNotification.is_active == True,
            or_(
                GovtJobNotification.update_type == "RESULT",
                GovtJobNotification.result_date.isnot(None),
            ),
        )
        .order_by(GovtJobNotification.created_at.desc())
        .all()
    )
    return ApiResponse(success=True, data=items)


@router.get("/deadlines", response_model=ApiResponse[List[GovtJobResponse]])
def get_closing_deadlines(db: Session = Depends(get_db)):
    """Get notifications where application deadlines are closing soon."""
    today = datetime.utcnow().strftime("%Y-%m-%d")
    items = (
        db.query(GovtJobNotification)
        .filter(
            GovtJobNotification.is_active == True,
            GovtJobNotification.application_end_date >= today,
        )
        .order_by(GovtJobNotification.application_end_date.asc())
        .limit(10)
        .all()
    )
    return ApiResponse(success=True, data=items)


@router.get("/{id}", response_model=ApiResponse[GovtJobResponse])
def get_govt_job_detail(id: str, db: Session = Depends(get_db)):
    """Get complete details for a single verified government job notification."""
    item = db.query(GovtJobNotification).filter(GovtJobNotification.id == id).first()
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Government Job notification not found.",
        )
    return ApiResponse(success=True, data=item)


@router.post("/scrape", response_model=ApiResponse[GovtJobScrapeResult])
async def trigger_live_scrape(
    organization: Optional[str] = Query(None, description="Optional target organization code"),
    db: Session = Depends(get_db),
):
    """
    On-demand live scraping trigger.
    Fetches real-time updates from official government recruitment websites,
    extracts official PDF details, removes duplicates, and updates database records.
    """
    result = await GovtJobScraperService.run_scraper(db, target_org=organization)
    return ApiResponse(
        success=True,
        message=result["message"],
        data=GovtJobScrapeResult(**result),
    )

