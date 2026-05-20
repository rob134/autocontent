"""Simple scheduling and retry policy for upload-only and downstream publish."""
from __future__ import annotations

from datetime import datetime, timedelta
from typing import Dict, List


class PublishScheduler:
    def build_schedule(self, platforms: List[str], cadence_minutes: int = 120) -> List[Dict]:
        now = datetime.utcnow()
        out = []
        for idx, platform in enumerate(platforms):
            out.append({
                "platform": platform,
                "scheduled_at": (now + timedelta(minutes=idx * cadence_minutes)).isoformat() + "Z",
                "retry_policy": {"max_retries": 5, "backoff_seconds": [30, 120, 300, 900, 1800]},
            })
        return out
