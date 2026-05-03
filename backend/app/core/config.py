"""
Application settings and configuration
"""
import os
from typing import Optional
from pydantic import BaseSettings


class Settings(BaseSettings):
    """Application configuration from environment variables"""
    
    # Database
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "sqlite:///./autocontent.db"
    )
    
    # API Configuration
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "AutoContent"
    
    # Security
    SECRET_KEY: str = os.getenv(
        "SECRET_KEY",
        "dev-secret-key-change-in-production"
    )
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # OAuth - YouTube
    YOUTUBE_CLIENT_ID: Optional[str] = os.getenv("YOUTUBE_CLIENT_ID")
    YOUTUBE_CLIENT_SECRET: Optional[str] = os.getenv("YOUTUBE_CLIENT_SECRET")
    YOUTUBE_REDIRECT_URI: str = "http://localhost:8000/api/v1/auth/youtube/callback"
    
    # Storage
    STORAGE_PATH: str = os.getenv("STORAGE_PATH", "./storage")
    TEMP_PATH: str = os.getenv("TEMP_PATH", "./temp")
    
    # Processing
    FFMPEG_PATH: str = os.getenv("FFMPEG_PATH", "ffmpeg")
    WHISPER_MODEL: str = os.getenv("WHISPER_MODEL", "base")
    TTS_ENGINE: str = os.getenv("TTS_ENGINE", "coqui")  # coqui, gtts, or api
    
    # Features (for phase roadmap)
    ENABLE_SCHEDULER: bool = False  # Phase 2
    ENABLE_ADS_MODE: bool = False  # Phase 2
    ENABLE_AVATAR_MODE: bool = False  # Phase 3
    ENABLE_CREATOR_PROFILES: bool = False  # Phase 4
    
    # Logging
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
