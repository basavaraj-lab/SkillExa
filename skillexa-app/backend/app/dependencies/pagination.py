from typing import Optional
from fastapi import Query
from backend.app.schemas.common import PaginationParams


def get_pagination(
    page: int = Query(1, ge=1, description="Page number"),
    limit: int = Query(20, ge=1, le=100, description="Items per page"),
    search: Optional[str] = Query(None, description="Search query"),
) -> PaginationParams:
    return PaginationParams(page=page, limit=limit, search=search)
