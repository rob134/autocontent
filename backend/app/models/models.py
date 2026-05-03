"""
SQLAlchemy models for Phase 1
"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean, ForeignKey, Enum
from sqlalchemy.orm import relationship
import enum

from app.core.database import Base


class ContentModeEnum(str, enum.Enum):
    """Content generation modes"""
    CURATED = "curated"
    AVATAR = "avatar"
    ADS = "ads"


class Channel(Base):
    """Social media channel model"""
    __tablename__ = "channels"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True)
    platform = Column(String(50))  # youtube, tiktok, instagram, etc.
    platform_channel_id = Column(String(255), unique=True)
    oauth_token = Column(Text)  # Encrypted token
    oauth_refresh_token = Column(Text)  # Encrypted refresh token
    mode = Column(Enum(ContentModeEnum), default=ContentModeEnum.CURATED)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    pipelines = relationship("Pipeline", back_populates="channel", cascade="all, delete-orphan")
    oauth_state = relationship("OAuthState", back_populates="channel", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Channel {self.name} ({self.platform})>"


class OAuthState(Base):
    """OAuth authorization state tracking"""
    __tablename__ = "oauth_states"

    id = Column(Integer, primary_key=True, index=True)
    state = Column(String(255), unique=True, index=True)
    channel_id = Column(Integer, ForeignKey("channels.id"))
    platform = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)
    expires_at = Column(DateTime)

    channel = relationship("Channel", back_populates="oauth_state")

    def __repr__(self):
        return f"<OAuthState {self.state} ({self.platform})>"


class Pipeline(Base):
    """Content pipeline execution record"""
    __tablename__ = "pipelines"

    id = Column(Integer, primary_key=True, index=True)
    channel_id = Column(Integer, ForeignKey("channels.id"))
    status = Column(String(50), default="pending")  # pending, running, completed, failed
    mode = Column(Enum(ContentModeEnum), default=ContentModeEnum.CURATED)
    
    # Pipeline configuration
    content_keyword = Column(String(255))  # For curated mode
    source_url = Column(String(500))  # Source video URL
    
    # Execution tracking
    started_at = Column(DateTime)
    completed_at = Column(DateTime)
    error_message = Column(Text)
    
    # Output
    output_video_path = Column(String(500))
    generated_title = Column(String(500))
    generated_description = Column(Text)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    channel = relationship("Channel", back_populates="pipelines")
    logs = relationship("PipelineLog", back_populates="pipeline", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Pipeline {self.id} ({self.status})>"


class PipelineLog(Base):
    """Execution logs for debugging and monitoring"""
    __tablename__ = "pipeline_logs"

    id = Column(Integer, primary_key=True, index=True)
    pipeline_id = Column(Integer, ForeignKey("pipelines.id"))
    level = Column(String(20))  # INFO, WARNING, ERROR, DEBUG
    message = Column(Text)
    step = Column(String(100))  # Step in pipeline (download, clip, compose, etc.)
    created_at = Column(DateTime, default=datetime.utcnow)

    pipeline = relationship("Pipeline", back_populates="logs")

    def __repr__(self):
        return f"<PipelineLog {self.step} ({self.level})>"
