"""Print example learner-agent outputs as JSON."""

from __future__ import annotations

import json

from learner_agent import LearnerAgent, generate_static_profiles


def main() -> None:
    profiles = generate_static_profiles()
    sample_profiles = [profiles[0], profiles[13], profiles[-1]]
    outputs = [
        LearnerAgent(profile).export_for_recommender()
        for profile in sample_profiles
    ]

    print(json.dumps(outputs, indent=2))


if __name__ == "__main__":
    main()
