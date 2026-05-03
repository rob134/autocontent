"""
Pipeline execution API endpoints
"""
import logging
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services.pipeline import PipelineService
from app.services.channel import ChannelService
from app.schemas.base import PipelineRunRequest, PipelineResponse, PipelineDetailResponse

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/run", response_model=PipelineResponse)
async def run_pipeline(
    request: PipelineRunRequest,
    db: Session = Depends(get_db)
):
    """Run content creation pipeline for a channel"""
    
    # Verify channel exists
    channel_service = ChannelService(db)
    channel = channel_service.get_channel(request.channel_id)
    
    if not channel:
        raise HTTPException(status_code=404, detail="Channel not found")
    
    if not channel.is_active:
        raise HTTPException(status_code=400, detail="Channel is inactive")
    
    # Execute pipeline
    pipeline_service = PipelineService(db)
    try:
        pipeline = await pipeline_service.run_pipeline(request.channel_id, request)
        return pipeline
    except Exception as e:
        logger.error(f"Pipeline execution failed: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Pipeline failed: {str(e)}")


@router.get("/{pipeline_id}", response_model=PipelineDetailResponse)
async def get_pipeline(
    pipeline_id: int,
    db: Session = Depends(get_db)
):
    """Get pipeline details with logs"""
    pipeline = db.query(__import__('app.models.models', fromlist=['Pipeline']).Pipeline).filter_by(id=pipeline_id).first()
    
    if not pipeline:
        raise HTTPException(status_code=404, detail="Pipeline not found")
    
    pipeline_service = PipelineService(db)
    logs = pipeline_service.get_pipeline_logs(pipeline_id)
    
    # Manually construct response with logs
    response_data = {
        "id": pipeline.id,
        "channel_id": pipeline.channel_id,
        "status": pipeline.status,
        "mode": pipeline.mode,
        "content_keyword": pipeline.content_keyword,
        "source_url": pipeline.source_url,
        "generated_title": pipeline.generated_title,
        "generated_description": pipeline.generated_description,
        "output_video_path": pipeline.output_video_path,
        "error_message": pipeline.error_message,
        "started_at": pipeline.started_at,
        "completed_at": pipeline.completed_at,
        "created_at": pipeline.created_at,
        "updated_at": pipeline.updated_at,
        "logs": logs,
    }
    
    return response_data
