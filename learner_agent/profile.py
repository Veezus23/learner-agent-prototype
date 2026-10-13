"""Learner profile data model."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Dict, List, Literal


ProficiencyLevel = Literal["weak", "medium", "strong"]
ConfidenceLevel = Literal["low", "medium", "high"]


@dataclass(frozen=True)
class LearnerProfile:
    """Structured, static learner profile used by the learner agent."""

    agent_id: str
    course: str
    topic: str
    topic_level_proficiency: ProficiencyLevel
    prerequisite_knowledge: List[str]
    confidence_level: ConfidenceLevel
    misconception: str
    preferred_explanation_depth: str
    recent_performance: Dict[str, Any]

    def to_dict(self) -> Dict[str, Any]:
        """Return a JSON-serializable dictionary representation."""
        return asdict(self)
