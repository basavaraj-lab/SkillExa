import json
import os
from typing import List, Union
from pydantic import field_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "SkillExa Backend API"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    API_V1_STR: str = "/api"

    # Database
    DATABASE_URL: str = "sqlite:///./skillexa.db"

    # Security & JWT
    JWT_SECRET: str = "skillexa_super_secret_jwt_key_development_2026_change_in_production"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440  # 24 hours
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # CORS
    CORS_ORIGINS: Union[List[str], str] = ["*"]

    @field_validator("CORS_ORIGINS", mode="before")
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> List[str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, str) and v.startswith("["):
            try:
                return json.loads(v)
            except Exception:
                return ["*"]
        elif isinstance(v, list):
            return v
        return ["*"]

    # File Storage
    STORAGE_LOCAL_DIR: str = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "uploads"))
    MAX_PDF_SIZE_MB: int = 25

    # Sandboxed Code Execution
    SANDBOX_EXECUTION_TIMEOUT_SECONDS: int = 5
    SANDBOX_MEMORY_LIMIT_MB: int = 256
    SANDBOX_MAX_PROCESSES: int = 10

    # Video Calling / WebRTC Signaling
    WEBRTC_SIGNALING_ENABLED: bool = True

    class Config:
        env_file = os.path.join(os.path.dirname(__file__), "..", ".env")
        env_file_encoding = "utf-8"
        case_sensitive = True
        extra = "ignore"


settings = Settings()

# Ensure uploads directory exists
os.makedirs(settings.STORAGE_LOCAL_DIR, exist_ok=True)
