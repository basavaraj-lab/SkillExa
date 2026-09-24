from backend.app.dependencies.db import get_db
from backend.app.dependencies.auth import (
    get_current_user,
    get_current_student,
    require_role,
    require_approved_faculty,
)
from backend.app.dependencies.pagination import get_pagination

__all__ = [
    "get_db",
    "get_current_user",
    "get_current_student",
    "require_role",
    "require_approved_faculty",
    "get_pagination",
]
