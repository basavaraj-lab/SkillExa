import os
import re
import uuid
from typing import Tuple
from fastapi import HTTPException, UploadFile, status
from backend.app.config import settings


def sanitize_filename(filename: str) -> str:
    """Sanitize original filename to prevent directory traversal."""
    cleaned = re.sub(r"[^a-zA-Z0-9_.-]", "_", filename)
    return cleaned[:100]


async def save_uploaded_pdf(file: UploadFile) -> Tuple[str, str, int]:
    """
    Validate, sanitize, and save an uploaded PDF file.
    Returns: (file_path, file_name, file_size_bytes)
    """
    # 1. Check content type
    if file.content_type not in ["application/pdf", "application/x-pdf", "application/acrobat"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid file type. Only PDF documents (.pdf) are allowed.",
        )

    # 2. Check filename extension
    if not file.filename or not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="File must have a .pdf extension.",
        )

    # 3. Read content and validate size
    content = await file.read()
    file_size_bytes = len(content)
    max_bytes = settings.MAX_PDF_SIZE_MB * 1024 * 1024

    if file_size_bytes > max_bytes:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"File exceeds maximum allowed size of {settings.MAX_PDF_SIZE_MB}MB.",
        )

    if file_size_bytes == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Uploaded file is empty.",
        )

    # 4. Save to storage directory
    os.makedirs(settings.STORAGE_LOCAL_DIR, exist_ok=True)
    clean_name = sanitize_filename(file.filename)
    unique_filename = f"{uuid.uuid4()}_{clean_name}"
    target_path = os.path.join(settings.STORAGE_LOCAL_DIR, unique_filename)

    with open(target_path, "wb") as f:
        f.write(content)

    return target_path, clean_name, file_size_bytes


def delete_stored_file(file_path: str) -> bool:
    """Safely delete stored file from disk."""
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            return True
    except Exception:
        pass
    return False
