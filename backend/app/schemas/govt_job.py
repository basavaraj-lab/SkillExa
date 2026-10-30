from datetime import datetime
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field


class GovtJobBase(BaseModel):
    organization: str
    organization_name: str
    category: str
    title: str
    advertisement_number: Optional[str] = None
    update_type: str = "RECRUITMENT"
    vacancies: Optional[int] = None
    qualification: Optional[str] = None
    age_limit: Optional[str] = None
    eligibility: Optional[str] = None
    application_start_date: Optional[str] = None
    application_end_date: Optional[str] = None
    exam_date: Optional[str] = None
    admit_card_date: Optional[str] = None
    result_date: Optional[str] = None
    official_pdf_url: Optional[str] = None
    apply_url: Optional[str] = None
    source_url: str
    status: str = "ACTIVE"
    description: Optional[str] = None
    selection_process: Optional[str] = None
    application_fee: Optional[str] = None
    raw_details: Optional[Dict[str, Any]] = None
    is_active: bool = True
    verification_status: str = "VERIFIED"


class GovtJobResponse(GovtJobBase):
    id: str
    scraped_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class GovtJobSummary(BaseModel):
    total_notifications: int
    active_vacancies: int
    open_applications: int
    upcoming_exams: int
    admit_cards_live: int
    results_announced: int
    deadlines_this_week: int
    last_scraped_at: Optional[str] = None


class GovtOrgInfo(BaseModel):
    code: str
    name: str
    official_website: str
    category: str
    badge_color: str
    active_notices_count: int
    exam_types: List[str]


class GovtJobScrapeResult(BaseModel):
    success: bool
    message: str
    total_scraped: int
    new_inserted: int
    updated: int
    duplicates_skipped: int
    organizations_checked: List[str]
    scraped_at: str

