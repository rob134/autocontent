"""
Pydantic schemas for request/response validation
"""
from pydantic import BaseModel, HttpUrl
from datetime import datetime
from typing import Optional, List
from enum import Enum


class ContentModeEnum(str, Enum):
    CURATED = "curated"
    AVATAR = "avatar"
    ADS = "ads"
    SEARCH_EDIT = "search_edit"
    UPLOAD_ONLY = "upload_only"
    GENERATIVE_CREATE = "generative_create"


class OrchestrationModeEnum(str, Enum):
    FASTAPI_SYNC = "fastapi_sync"
    C_MESSAGE_BUS_READY = "c_message_bus_ready"
    K8S_READY = "k8s_ready"


# Channel Schemas
class ChannelBase(BaseModel):
    name: str
    platform: str
    mode: ContentModeEnum = ContentModeEnum.CURATED
    is_active: bool = True


class ChannelCreate(ChannelBase):
    pass


class ChannelUpdate(BaseModel):
    mode: Optional[ContentModeEnum] = None
    is_active: Optional[bool] = None


class ChannelResponse(ChannelBase):
    id: int
    platform_channel_id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ChannelListResponse(BaseModel):
    channels: List[ChannelResponse]
    total: int


# Pipeline Schemas
class PipelineBase(BaseModel):
    mode: ContentModeEnum = ContentModeEnum.CURATED
    content_keyword: Optional[str] = None
    source_url: Optional[str] = None


class PipelineRunRequest(PipelineBase):
    channel_id: int


class AssistantMessageRequest(BaseModel):
    message: str
    channel_id: Optional[int] = None
    source_url: Optional[HttpUrl] = None
    orchestration_mode: OrchestrationModeEnum = OrchestrationModeEnum.C_MESSAGE_BUS_READY


class AssistantMessageResponse(BaseModel):
    intent: ContentModeEnum
    reasoning: str
    suggested_steps: List[str]
    pipeline_request: PipelineRunRequest


class SearchEditRunRequest(BaseModel):
    prompt: str
    niche: str = "general"


class UploadOnlyRunRequest(BaseModel):
    asset_path: str
    platforms: List[str]


class GenerativeRunRequest(BaseModel):
    prompt: str
    provider: str = "veo"
    platforms: List[str] = ["youtube", "tiktok", "instagram"]


class PipelineResponse(BaseModel):
    id: int
    channel_id: int
    status: str
    mode: ContentModeEnum
    content_keyword: Optional[str]
    source_url: Optional[str]
    generated_title: Optional[str]
    generated_description: Optional[str]
    output_video_path: Optional[str]
    error_message: Optional[str]
    started_at: Optional[datetime]
    completed_at: Optional[datetime]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class PipelineLogResponse(BaseModel):
    id: int
    step: str
    level: str
    message: str
    created_at: datetime

    class Config:
        from_attributes = True


class PipelineDetailResponse(PipelineResponse):
    logs: List[PipelineLogResponse]


# OAuth Schemas
class OAuthInitRequest(BaseModel):
    platform: str  # youtube, tiktok, instagram, etc.


class OAuthCallbackRequest(BaseModel):
    code: str
    state: str


class OAuthTokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


# Health Check
class HealthCheckResponse(BaseModel):
    status: str
    version: str


# Error Response
class ErrorResponse(BaseModel):
    detail: str
    status_code: int
    timestamp: datetime
