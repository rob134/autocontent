"""Pluggable connectors for search/upload/generation providers."""
from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Dict, List

from app.services.intent_pipeline import CandidateVideo


class DiscoveryConnector:
    def search_rank_candidates(self, query: str, niche: str) -> List[CandidateVideo]:
        now = datetime.now(timezone.utc)
        # MVP mock candidates; replace with YouTube/TikTok search APIs in production workers.
        return [
            CandidateVideo("yt001", f"{query} podcast highlights", niche, now - timedelta(hours=8), 0.92, 52000, 0.81, 0.42, 0.74),
            CandidateVideo("yt002", f"{query} deep dive", "business", now - timedelta(days=3), 0.83, 23000, 0.75, 0.35, 0.62),
            CandidateVideo("tk003", f"{query} shorts compilation", niche, now - timedelta(hours=40), 0.88, 95000, 0.69, 0.20, 0.58),
        ]


class UploadConnector:
    def queue_upload(self, platform: str, asset_path: str, metadata: Dict) -> Dict:
        return {"platform": platform, "asset_path": asset_path, "status": "queued", "metadata": metadata}


class GenerativeConnector:
    def generate_video(self, provider: str, prompt: str) -> Dict:
        return {
            "provider": provider,
            "status": "generated",
            "asset_path": f"./storage/videos/generated_{provider.lower()}.mp4",
            "prompt": prompt,
        }
