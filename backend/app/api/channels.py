"""
Channel API endpoints
"""
import logging
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services.channel import ChannelService
from app.schemas.base import ChannelCreate, ChannelUpdate, ChannelResponse, ChannelListResponse

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("", response_model=ChannelResponse)
async def create_channel(
    channel: ChannelCreate,
    db: Session = Depends(get_db)
):
    """Create a new channel"""
    service = ChannelService(db)
    
    # Check if channel already exists
    existing = service.get_channel_by_name(channel.name)
    if existing:
        raise HTTPException(
            status_code=400,
            detail=f"Channel '{channel.name}' already exists"
        )
    
    # In Phase 1, use mock OAuth token
    new_channel = service.create_channel(
        name=channel.name,
        platform=channel.platform,
        platform_channel_id=f"mock_id_{channel.name}",
        oauth_token="mock_token",
        mode=channel.mode
    )
    
    return new_channel


@router.get("", response_model=ChannelListResponse)
async def list_channels(db: Session = Depends(get_db)):
    """List all channels"""
    service = ChannelService(db)
    channels = service.list_channels()
    return ChannelListResponse(channels=channels, total=len(channels))


@router.get("/{channel_id}", response_model=ChannelResponse)
async def get_channel(
    channel_id: int,
    db: Session = Depends(get_db)
):
    """Get channel by ID"""
    service = ChannelService(db)
    channel = service.get_channel(channel_id)
    
    if not channel:
        raise HTTPException(status_code=404, detail="Channel not found")
    
    return channel


@router.patch("/{channel_id}", response_model=ChannelResponse)
async def update_channel(
    channel_id: int,
    update: ChannelUpdate,
    db: Session = Depends(get_db)
):
    """Update channel settings"""
    service = ChannelService(db)
    channel = service.update_channel(channel_id, update)
    
    if not channel:
        raise HTTPException(status_code=404, detail="Channel not found")
    
    return channel


@router.delete("/{channel_id}")
async def delete_channel(
    channel_id: int,
    db: Session = Depends(get_db)
):
    """Delete channel"""
    service = ChannelService(db)
    success = service.delete_channel(channel_id)
    
    if not success:
        raise HTTPException(status_code=404, detail="Channel not found")
    
    return {"message": "Channel deleted successfully"}
