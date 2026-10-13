"""Tests for learner-agent behavior rules."""

import unittest

from learner_agent.agent import LearnerAgent, export_for_recommender
from learner_agent.generate_profiles import generate_static_profiles


class TestLearnerAgent(unittest.TestCase):
    def test_generated_queries_are_non_empty(self) -> None:
        profiles = generate_static_profiles()

        for profile in profiles:
            query = LearnerAgent(profile).generate_query()
            self.assertIsInstance(query, str)
            self.assertTrue(query.strip())

    def test_weak_medium_strong_profiles_have_different_query_styles(self) -> None:
        profiles = generate_static_profiles()
        topic = "Solving linear equations"
        misconception = profiles[0].misconception
        comparison_profiles = {
            profile.topic_level_proficiency: profile
            for profile in profiles
            if profile.topic == topic and profile.misconception == misconception
        }

        weak_query = LearnerAgent(comparison_profiles["weak"]).generate_query()
        medium_query = LearnerAgent(comparison_profiles["medium"]).generate_query()
        strong_query = LearnerAgent(comparison_profiles["strong"]).generate_query()

        self.assertIn("lost on the basics", weak_query)
        self.assertIn("stuck when applying", medium_query)
        self.assertIn("refine my reasoning", strong_query)
        self.assertEqual(3, len({weak_query, medium_query, strong_query}))

    def test_export_for_recommender_is_json_ready(self) -> None:
        profile = generate_static_profiles()[0]
        export = LearnerAgent(profile).export_for_recommender()

        self.assertEqual(profile.agent_id, export["agent_id"])
        self.assertEqual(profile.topic, export["topic"])
        self.assertEqual(profile.prerequisite_knowledge, export["prerequisite_knowledge"])
        self.assertIn("generated_query", export)
        self.assertTrue(export["generated_query"])

    def test_module_level_export_function_matches_agent_method(self) -> None:
        profile = generate_static_profiles()[0]

        self.assertEqual(
            LearnerAgent(profile).export_for_recommender(),
            export_for_recommender(profile),
        )


if __name__ == "__main__":
    unittest.main()
