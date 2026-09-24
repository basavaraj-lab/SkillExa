from typing import Generic, List, Optional, TypeVar
from pydantic import BaseModel, Field

T = TypeVar("T")


class ApiResponse(BaseModel, Generic[T]):
    success: bool = True
    message: str = "Operation successful"
    data: Optional[T] = None
    code: Optional[str] = None


class PaginatedResponse(BaseModel, Generic[T]):
    items: List[T]
    page: int = Field(1, ge=1)
    limit: int = Field(20, ge=1)
    total: int = Field(0, ge=0)
    total_pages: int = Field(0, ge=0)


class PaginationParams(BaseModel):
    page: int = Field(1, ge=1, description="Page number starting at 1")
    limit: int = Field(20, ge=1, le=100, description="Items per page (max 100)")
    search: Optional[str] = Field(None, description="Optional search term")
