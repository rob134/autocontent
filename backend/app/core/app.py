"""
FastAPI configuration and initialization
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
import logging

logger = logging.getLogger(__name__)


def create_app() -> FastAPI:
    """Create and configure FastAPI application"""
    app = FastAPI(
        title="AutoContent API",
        description="Modular content automation platform",
        version="0.1.0",
    )

    # Add middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:4200", "http://localhost:3000"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    app.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=["localhost", "127.0.0.1"],
    )

    # Include routers
    from app.api import channels, pipeline, auth, logs
    
    app.include_router(channels.router, prefix="/api/v1/channels", tags=["channels"])
    app.include_router(pipeline.router, prefix="/api/v1/pipeline", tags=["pipeline"])
    app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
    app.include_router(logs.router, prefix="/api/v1/logs", tags=["logs"])

    @app.get("/health")
    async def health_check():
        return {"status": "ok", "version": "0.1.0"}

    return app
