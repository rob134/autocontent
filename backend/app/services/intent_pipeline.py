"""Core orchestration intents and MVP algorithms."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from math import exp
from typing import Dict, List


@dataclass
class CandidateVideo:
    video_id: str
    title: str
    niche: str
    published_at: datetime
    semantic_relevance: float
    views_per_hour: float
    like_ratio: float
    comment_ratio: float
    estimated_retention: float


class RankingEngine:
    """MVP ranker for Search & Edit flow using weighted score."""

    WEIGHTS = {
        "semantic": 0.35,
        "engagement": 0.25,
        "retention": 0.20,
        "recency": 0.10,
        "niche_fit": 0.10,
    }

    @staticmethod
    def _clip01(v: float) -> float:
        return max(0.0, min(1.0, v))

    def _engagement(self, c: CandidateVideo) -> float:
        norm_views = self._clip01(c.views_per_hour / 100000)
        return self._clip01((norm_views + c.like_ratio + c.comment_ratio) / 3)

    def _recency(self, published_at: datetime) -> float:
        age_hours = max(0.0, (datetime.now(timezone.utc) - published_at).total_seconds() / 3600)
        half_life_hours = 24 * 14
        return self._clip01(exp(-age_hours / half_life_hours))

    def _niche_fit(self, niche: str, target_niche: str) -> float:
        return 1.0 if niche.lower() == target_niche.lower() else 0.55

    def score(self, c: CandidateVideo, target_niche: str) -> float:
        engagement = self._engagement(c)
        recency = self._recency(c.published_at)
        niche_fit = self._niche_fit(c.niche, target_niche)
        return (
            self.WEIGHTS["semantic"] * self._clip01(c.semantic_relevance)
            + self.WEIGHTS["engagement"] * engagement
            + self.WEIGHTS["retention"] * self._clip01(c.estimated_retention)
            + self.WEIGHTS["recency"] * recency
            + self.WEIGHTS["niche_fit"] * niche_fit
        )

    def rank(self, candidates: List[CandidateVideo], target_niche: str) -> List[Dict]:
        scored = [
            {
                "video_id": c.video_id,
                "title": c.title,
                "niche": c.niche,
                "score": round(self.score(c, target_niche), 4),
            }
            for c in candidates
        ]
        return sorted(scored, key=lambda x: x["score"], reverse=True)
