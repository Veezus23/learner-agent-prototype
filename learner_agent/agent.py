"""Deterministic learner-agent behavior rules."""

from __future__ import annotations

from typing import Any, Dict

from learner_agent.profile import LearnerProfile


class LearnerAgent:
    """Learner agent composed of a static profile and behavior rules."""

    _PROFICIENCY_FRAMES = {
        "weak": "I'm lost on the basics of {topic}.",
        "medium": "I understand part of {topic}, but I get stuck when applying it.",
        "strong": "I can usually solve {topic} problems, but I want to refine my reasoning.",
    }

    _CONFIDENCE_FRAMES = {
        "low": "Can you explain it slowly and check my thinking?",
        "medium": "Can you show one example and point out where my reasoning goes wrong?",
        "high": "Can you challenge my understanding with a precise explanation?",
    }

    _MISCONCEPTION_FRAMES = {
        "weak": "I think {misconception}. Is that why I'm confused?",
        "medium": "I keep assuming that {misconception}. When does that break down?",
        "strong": "I suspect my edge-case mistake is that {misconception}. How should I correct it?",
    }

    def __init__(self, profile: LearnerProfile) -> None:
        self.profile = profile

    def generate_query(self) -> str:
        """Create a realistic, deterministic student question from the profile."""
        proficiency = self.profile.topic_level_proficiency
        confidence = self.profile.confidence_level

        topic_frame = self._PROFICIENCY_FRAMES[proficiency].format(
            topic=self.profile.topic
        )
        misconception_frame = self._MISCONCEPTION_FRAMES[proficiency].format(
            misconception=self.profile.misconception
        )
        confidence_frame = self._CONFIDENCE_FRAMES[confidence]

        return " ".join([topic_frame, misconception_frame, confidence_frame])

    def export_for_recommender(self) -> Dict[str, Any]:
        """Return clean JSON-like learner context for a recommender system."""
        return {
            "agent_id": self.profile.agent_id,
            "course": self.profile.course,
            "topic": self.profile.topic,
            "topic_level_proficiency": self.profile.topic_level_proficiency,
            "prerequisite_knowledge": self.profile.prerequisite_knowledge,
            "confidence_level": self.profile.confidence_level,
            "misconception": self.profile.misconception,
            "preferred_explanation_depth": self.profile.preferred_explanation_depth,
            "recent_performance": self.profile.recent_performance,
            "generated_query": self.generate_query(),
        }


def export_for_recommender(profile: LearnerProfile) -> Dict[str, Any]:
    """Return recommender-ready output for a learner profile."""
    return LearnerAgent(profile).export_for_recommender()
