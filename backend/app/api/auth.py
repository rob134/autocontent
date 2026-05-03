"""
Authentication API endpoints
"""
import logging
import os
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services.oauth import OAuthService
from app.services.channel import ChannelService
from app.models.models import OAuthState, ContentModeEnum
from app.schemas.base import OAuthInitRequest, OAuthCallbackRequest, OAuthTokenResponse
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/youtube/init")
async def init_youtube_oauth(
    request: OAuthInitRequest,
    db: Session = Depends(get_db)
):
    """Initialize YouTube OAuth flow"""
    
    if request.platform != "youtube":
        raise HTTPException(status_code=400, detail="Unsupported platform")
    
    # Generate state
    state = OAuthService.generate_state()
    
    # Store state in database
    oauth_state = OAuthState(
        state=state,
        platform="youtube",
        expires_at=datetime.utcnow() + timedelta(minutes=10)
    )
    db.add(oauth_state)
    db.commit()
    
    # Get authorization URL
    client_id = os.getenv("YOUTUBE_CLIENT_ID", "mock_client_id")
    auth_url = OAuthService.get_youtube_auth_url(state, client_id)
    
    return {
        "auth_url": auth_url,
        "state": state
    }


@router.post("/youtube/callback")
async def youtube_oauth_callback(
    code: str = Query(...),
    state: str = Query(...),
    db: Session = Depends(get_db)
):
    """Handle YouTube OAuth callback"""
    
    # Verify state
    oauth_state = db.query(OAuthState).filter(
        OAuthState.state == state,
        OAuthState.expires_at > datetime.utcnow()
    ).first()
    
    if not oauth_state:
        raise HTTPException(status_code=400, detail="Invalid or expired state")
    
    # Exchange code for token
    token_data = await OAuthService.exchange_code_for_token(code, "youtube")
    
    if not token_data:
        raise HTTPException(status_code=400, detail="Failed to exchange code for token")
    
    # In Phase 1, create a channel with the token
    # In production, prompt user to name the channel
    channel_service = ChannelService(db)
    channel = channel_service.create_channel(
        name=f"YouTube Channel {state[:8]}",
        platform="youtube",
        platform_channel_id="UCxxx",  # Mock - should come from API
        oauth_token=token_data["access_token"],
        mode=ContentModeEnum.CURATED
    )
    
    # Clean up state
    db.delete(oauth_state)
    db.commit()
    
    return {
        "message": "OAuth successful",
        "channel_id": channel.id,
        "channel_name": channel.name
    }


@router.get("/youtube/callback", response_model=dict)
async def youtube_callback_redirect(
    code: str = Query(...),
    state: str = Query(...),
    db: Session = Depends(get_db)
):
    """Handle OAuth callback (GET for browser redirects)"""
    return await youtube_oauth_callback(code=code, state=state, db=db)
