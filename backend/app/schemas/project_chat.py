from datetime import datetime
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field


class AIProjectCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=120)
    description: Optional[str] = None
    icon: Optional[str] = "folder"
    context_prompt: Optional[str] = None


class AIProjectUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=120)
    description: Optional[str] = None
    icon: Optional[str] = None
    context_prompt: Optional[str] = None
    is_pinned: Optional[bool] = None


class AIProjectResponse(BaseModel):
    id: str
    student_id: str
    name: str
    description: Optional[str]
    icon: str
    context_prompt: Optional[str]
    is_pinned: bool
    conversation_count: int = 0
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class AIConversationCreate(BaseModel):
    project_id: Optional[str] = None
    title: Optional[str] = "New Conversation"


class AIConversationUpdate(BaseModel):
    title: Optional[str] = None
    project_id: Optional[str] = None  # To move conversation to another project


class AIMessageResponse(BaseModel):
    id: str
    conversation_id: str
    sender_type: str
    message_text: str
    input_type: str
    search_sources: List[Dict[str, Any]] = []
    created_at: datetime

    class Config:
        from_attributes = True


class AIConversationDetailResponse(BaseModel):
    id: str
    project_id: str
    project_name: str
    student_id: str
    title: str
    messages: List[AIMessageResponse] = []
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class AIConversationListItem(BaseModel):
    id: str
    project_id: str
    project_name: str
    student_id: str
    title: str
    message_count: int = 0
    last_message_preview: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class AIChatRequest(BaseModel):
    message: str = Field(..., min_length=1)
    project_id: Optional[str] = None
    conversation_id: Optional[str] = None
    input_type: str = "text"  # 'text' | 'voice'
    search_enabled: bool = False
    spoken_acknowledgement_needed: bool = False
    file_data: Optional[str] = None  # Base64 encoded file or data URL
    file_name: Optional[str] = None
    file_mime_type: Optional[str] = None


class AIChatResponse(BaseModel):
    project_id: str
    project_name: str
    conversation_id: str
    conversation_title: str
    reply: str
    speech_text: str
    search_sources: List[Dict[str, Any]] = []
    memory_summary: Optional[str] = None
    acknowledgement: Optional[str] = None


class ProjectMemoryResponse(BaseModel):
    project_id: str
    project_name: str
    memory_summary: str
    key_entities: Dict[str, Any] = {}
    updated_at: datetime

