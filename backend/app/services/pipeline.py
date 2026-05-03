"""
Pipeline execution service
"""
import logging
import asyncio
from datetime import datetime
from typing import Optional
from sqlalchemy.orm import Session

from app.models.models import Pipeline, PipelineLog, ContentModeEnum
from app.schemas.base import PipelineRunRequest

logger = logging.getLogger(__name__)


class PipelineService:
    """Orchestrate content creation pipeline execution"""
    
    def __init__(self, db: Session):
        self.db = db
    
    async def run_pipeline(self, channel_id: int, request: PipelineRunRequest) -> Pipeline:
        """Execute full content creation pipeline"""
        
        # Create pipeline record
        pipeline = Pipeline(
            channel_id=channel_id,
            status="running",
            mode=request.mode,
            content_keyword=request.content_keyword,
            source_url=request.source_url,
            started_at=datetime.utcnow(),
        )
        self.db.add(pipeline)
        self.db.commit()
        self.db.refresh(pipeline)
        
        try:
            # Log start
            self._log(pipeline.id, "PIPELINE", "INFO", f"Starting {request.mode} pipeline")
            
            # Phase 1: Simple workflow (mock)
            await self._execute_phase1_pipeline(pipeline, request)
            
            pipeline.status = "completed"
            pipeline.completed_at = datetime.utcnow()
            self._log(pipeline.id, "PIPELINE", "INFO", "Pipeline completed successfully")
            
        except Exception as e:
            logger.error(f"Pipeline failed: {str(e)}")
            pipeline.status = "failed"
            pipeline.error_message = str(e)
            pipeline.completed_at = datetime.utcnow()
            self._log(pipeline.id, "PIPELINE", "ERROR", f"Pipeline failed: {str(e)}")
        
        self.db.commit()
        return pipeline
    
    async def _execute_phase1_pipeline(self, pipeline: Pipeline, request: PipelineRunRequest):
        """Execute Phase 1 simple pipeline"""
        
        # Step 1: Content Discovery
        self._log(pipeline.id, "DISCOVERY", "INFO", f"Searching for content: {request.content_keyword}")
        await asyncio.sleep(1)  # Mock operation
        
        # Step 2: Download
        self._log(pipeline.id, "DOWNLOAD", "INFO", "Downloading source video")
        await asyncio.sleep(1)  # Mock download
        
        # Step 3: Clipping
        self._log(pipeline.id, "CLIPPING", "INFO", "Creating video clips")
        await asyncio.sleep(1)  # Mock clipping
        
        # Step 4: Script Generation
        self._log(pipeline.id, "SCRIPT", "INFO", "Generating title and description")
        pipeline.generated_title = "Auto-generated Title: " + (request.content_keyword or "Content")
        pipeline.generated_description = f"This is an auto-generated description for {request.mode} content."
        
        # Step 5: Composition
        self._log(pipeline.id, "COMPOSITION", "INFO", "Composing final video")
        await asyncio.sleep(1)  # Mock composition
        pipeline.output_video_path = f"./storage/videos/pipeline_{pipeline.id}.mp4"
        
        # Step 6: Ready for Upload
        self._log(pipeline.id, "READY", "INFO", "Video ready for upload")
    
    def _log(self, pipeline_id: int, step: str, level: str, message: str):
        """Create a pipeline log entry"""
        log = PipelineLog(
            pipeline_id=pipeline_id,
            step=step,
            level=level,
            message=message,
        )
        self.db.add(log)
        self.db.commit()
        logger.log(
            level=getattr(logging, level),
            msg=f"[Pipeline {pipeline_id}] {step}: {message}"
        )
    
    def get_pipeline_logs(self, pipeline_id: int) -> list:
        """Get all logs for a pipeline"""
        return self.db.query(PipelineLog).filter(
            PipelineLog.pipeline_id == pipeline_id
        ).order_by(PipelineLog.created_at).all()
