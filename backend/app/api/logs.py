"""
Pipeline logs API endpoints
"""
import logging
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.models import Pipeline, PipelineLog
from app.schemas.base import PipelineLogResponse

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/{pipeline_id}")
async def get_pipeline_logs(
    pipeline_id: int,
    db: Session = Depends(get_db)
):
    """Get all logs for a pipeline"""
    
    # Verify pipeline exists
    pipeline = db.query(Pipeline).filter(Pipeline.id == pipeline_id).first()
    if not pipeline:
        raise HTTPException(status_code=404, detail="Pipeline not found")
    
    # Get logs
    logs = db.query(PipelineLog).filter(
        PipelineLog.pipeline_id == pipeline_id
    ).order_by(PipelineLog.created_at).all()
    
    return {"pipeline_id": pipeline_id, "logs": logs}


@router.get("/{pipeline_id}/stream")
async def stream_pipeline_logs(
    pipeline_id: int,
    db: Session = Depends(get_db)
):
    """Stream pipeline logs (for real-time UI updates)
    
    In Phase 1, return all logs.
    In Phase 2+, implement WebSocket for real-time streaming.
    """
    return await get_pipeline_logs(pipeline_id, db)
