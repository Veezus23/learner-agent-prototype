"""Tests for static learner profile generation."""

import unittest
from dataclasses import fields

from learner_agent.generate_profiles import generate_static_profiles
from learner_agent.profile import LearnerProfile


class TestProfileGeneration(unittest.TestCase):
    def test_generates_27_profiles(self) -> None:
        profiles = generate_static_profiles()

        self.assertEqual(27, len(profiles))

    def test_each_profile_has_required_fields(self) -> None:
        profiles = generate_static_profiles()
        required_fields = {field.name for field in fields(LearnerProfile)}

        for profile in profiles:
            profile_data = profile.to_dict()
            self.assertEqual(required_fields, set(profile_data))
            for field_name in required_fields:
                self.assertIsNotNone(profile_data[field_name])

    def test_agent_ids_are_unique(self) -> None:
        profiles = generate_static_profiles()
        agent_ids = [profile.agent_id for profile in profiles]

        self.assertEqual(len(agent_ids), len(set(agent_ids)))


if __name__ == "__main__":
    unittest.main()
