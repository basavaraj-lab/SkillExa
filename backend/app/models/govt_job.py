import enum
import uuid
from datetime import datetime
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Enum,
    Integer,
    JSON,
    String,
    Text,
)
from backend.app.database import Base


def generate_uuid() -> str:
    return str(uuid.uuid4())


class GovtOrgEnum(str, enum.Enum):
    SSC = "SSC"
    UPSC = "UPSC"
    IBPS = "IBPS"
    KPSC = "KPSC"
    BSF = "BSF"
    SSB = "SSB"
    RRB_BENGALURU = "RRB_BENGALURU"
    KARNATAKA_POLICE = "KARNATAKA_POLICE"


class UpdateTypeEnum(str, enum.Enum):
    RECRUITMENT = "RECRUITMENT"
    NOTIFICATION = "NOTIFICATION"
    EXAM_DATE = "EXAM_DATE"
    ADMIT_CARD = "ADMIT_CARD"
    RESULT = "RESULT"
    CORRIGENDUM = "CORRIGENDUM"


class GovtJobNotification(Base):
    __tablename__ = "govt_job_notifications"

    id = Column(String(36), primary_key=True, default=generate_uuid, index=True)
    organization = Column(String(50), nullable=False, index=True)  # SSC, UPSC, IBPS, KPSC, BSF, SSB, RRB_BENGALURU, KARNATAKA_POLICE
    organization_name = Column(String(200), nullable=False)
    category = Column(String(100), nullable=False, index=True)  # Central Govt, State Govt, Banking, Defense, Police, Railways

    title = Column(String(300), nullable=False, index=True)
    advertisement_number = Column(String(120), nullable=True, index=True)
    update_type = Column(String(50), default="RECRUITMENT", nullable=False, index=True)  # RECRUITMENT, EXAM_DATE, ADMIT_CARD, RESULT

    vacancies = Column(Integer, nullable=True)  # Exact vacancy count from official PDF/notice
    qualification = Column(String(255), nullable=True)  # 10th Pass, 12th Pass, Degree, etc.
    age_limit = Column(String(100), nullable=True)
    eligibility = Column(Text, nullable=True)

    application_start_date = Column(String(50), nullable=True)
    application_end_date = Column(String(50), nullable=True, index=True)  # Deadline
    exam_date = Column(String(100), nullable=True)
    admit_card_date = Column(String(100), nullable=True)
    result_date = Column(String(100), nullable=True)

    official_pdf_url = Column(String(500), nullable=True)
    apply_url = Column(String(500), nullable=True)
    source_url = Column(String(500), nullable=False)  # Verified official announcement URL
    source_hash = Column(String(64), unique=True, index=True, nullable=False)  # Deduplication hash

    status = Column(String(50), default="ACTIVE", index=True)  # ACTIVE, UPCOMING, DEADLINE_CLOSE, EXAM_SCHEDULED, ADMIT_CARD_LIVE, RESULT_OUT, ARCHIVED
    description = Column(Text, nullable=True)
    selection_process = Column(Text, nullable=True)
    application_fee = Column(String(150), nullable=True)
    raw_details = Column(JSON, default=dict)

    is_active = Column(Boolean, default=True, index=True)
    verification_status = Column(String(50), default="VERIFIED", index=True)

    scraped_at = Column(DateTime, default=datetime.utcnow)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

