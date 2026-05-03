"""
Channel management service
"""
import logging
from typing import List, Optional
from sqlalchemy.orm import Session

from app.models.models import Channel, ContentModeEnum
from app.schemas.base import ChannelCreate, ChannelUpdate
from app.services.oauth import TokenService

logger = logging.getLogger(__name__)


class ChannelService:
    """Manage channel CRUD and OAuth setup"""
    
    def __init__(self, db: Session):
        self.db = db
    
    def create_channel(
        self,
        name: str,
        platform: str,
        platform_channel_id: str,
        oauth_token: str,
        mode: ContentModeEnum = ContentModeEnum.CURATED
    ) -> Channel:
        """Create new channel with OAuth token"""
        
        # Encrypt token before storing
        encrypted_token = TokenService.encrypt_token(oauth_token)
        
        channel = Channel(
            name=name,
            platform=platform,
            platform_channel_id=platform_channel_id,
            oauth_token=encrypted_token,
            mode=mode,
        )
        
        self.db.add(channel)
        self.db.commit()
        self.db.refresh(channel)
        logger.info(f"Created channel: {name} ({platform})")
        return channel
    
    def get_channel(self, channel_id: int) -> Optional[Channel]:
        """Get channel by ID"""
        return self.db.query(Channel).filter(Channel.id == channel_id).first()
    
    def get_channel_by_name(self, name: str) -> Optional[Channel]:
        """Get channel by name"""
        return self.db.query(Channel).filter(Channel.name == name).first()
    
    def list_channels(self) -> List[Channel]:
        """List all active channels"""
        return self.db.query(Channel).filter(Channel.is_active == True).all()
    
    def update_channel(self, channel_id: int, update_data: ChannelUpdate) -> Optional[Channel]:
        """Update channel settings"""
        channel = self.get_channel(channel_id)
        if not channel:
            return None
        
        update_dict = update_data.dict(exclude_unset=True)
        for key, value in update_dict.items():
            setattr(channel, key, value)
        
        self.db.commit()
        self.db.refresh(channel)
        logger.info(f"Updated channel: {channel.name}")
        return channel
    
    def delete_channel(self, channel_id: int) -> bool:
        """Soft delete channel"""
        channel = self.get_channel(channel_id)
        if not channel:
            return False
        
        channel.is_active = False
        self.db.commit()
        logger.info(f"Deleted channel: {channel.name}")
        return True
    
    def get_token(self, channel_id: int) -> Optional[str]:
        """Get decrypted OAuth token for a channel"""
        channel = self.get_channel(channel_id)
        if not channel or not channel.oauth_token:
            return None
        
        try:
            return TokenService.decrypt_token(channel.oauth_token)
        except Exception as e:
            logger.error(f"Failed to decrypt token for channel {channel_id}: {str(e)}")
            return None
