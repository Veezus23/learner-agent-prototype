"""Static learner profile generation for reproducible experiments."""

from __future__ import annotations

from typing import Dict, List

from learner_agent.profile import LearnerProfile, ProficiencyLevel


COURSE = "Introductory Algebra"

TOPIC_CONFIG: Dict[str, Dict[str, List[str]]] = {
    "Solving linear equations": {
        "prerequisites": [
            "integer arithmetic",
            "inverse operations",
            "order of operations",
        ],
        "misconceptions": [
            "moving a term across the equals sign changes the problem without needing the same operation on both sides",
            "subtracting a negative number always makes the result smaller",
            "the variable must always be isolated in one step",
        ],
    },
    "Graphing linear functions": {
        "prerequisites": [
            "coordinate plane",
            "ordered pairs",
            "slope as rate of change",
        ],
        "misconceptions": [
            "slope is the same thing as the y-intercept",
            "a negative slope means all y-values must be negative",
            "the graph of a linear function can curve if the points are far apart",
        ],
    },
    "Factoring quadratic expressions": {
        "prerequisites": [
            "multiplication facts",
            "distributive property",
            "combining like terms",
        ],
        "misconceptions": [
            "factoring means dividing every term by the largest visible number",
            "the two binomial constants should add to the constant term instead of multiply to it",
            "a quadratic with a negative middle term cannot have two positive factors",
        ],
    },
}

PROFICIENCY_SETTINGS: Dict[ProficiencyLevel, Dict[str, object]] = {
    "weak": {
        "confidence_level": "low",
        "preferred_explanation_depth": "step-by-step with prerequisite review",
        "recent_performance": {
            "last_quiz_score": 42,
            "practice_accuracy": 0.38,
            "attempts_last_week": 3,
        },
    },
    "medium": {
        "confidence_level": "medium",
        "preferred_explanation_depth": "worked example with concise reminders",
        "recent_performance": {
            "last_quiz_score": 71,
            "practice_accuracy": 0.68,
            "attempts_last_week": 5,
        },
    },
    "strong": {
        "confidence_level": "high",
        "preferred_explanation_depth": "concise explanation with edge cases",
        "recent_performance": {
            "last_quiz_score": 91,
            "practice_accuracy": 0.88,
            "attempts_last_week": 6,
        },
    },
}


def generate_static_profiles() -> List[LearnerProfile]:
    """Generate 27 deterministic learner profiles."""
    profiles: List[LearnerProfile] = []
    agent_number = 1

    for topic, topic_config in TOPIC_CONFIG.items():
        for proficiency, proficiency_config in PROFICIENCY_SETTINGS.items():
            for misconception in topic_config["misconceptions"]:
                profile = LearnerProfile(
                    agent_id=f"learner-{agent_number:03d}",
                    course=COURSE,
                    topic=topic,
                    topic_level_proficiency=proficiency,
                    prerequisite_knowledge=list(topic_config["prerequisites"]),
                    confidence_level=str(proficiency_config["confidence_level"]),
                    misconception=misconception,
                    preferred_explanation_depth=str(
                        proficiency_config["preferred_explanation_depth"]
                    ),
                    recent_performance=dict(proficiency_config["recent_performance"]),
                )
                profiles.append(profile)
                agent_number += 1

    return profiles
