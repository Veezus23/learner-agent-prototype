# Learner Agent Prototype

Minimal Version 1 prototype for simulated learner agents in an AI-in-education research project.

This version intentionally avoids a full agent SDK. A learner agent is modeled as:

```text
structured learner profile + deterministic behavior rules
```

The prototype uses static profiles so behavior is reproducible and easy to evaluate.

## Structure

```text
learner_agent_prototype/
  README.md
  learner_agent/
    __init__.py
    profile.py
    agent.py
    generate_profiles.py
  tests/
    test_profiles.py
    test_agent.py
  main.py
```

## Run Examples

From this directory:

```bash
python main.py
```

On Windows, if `python` is not available but the Python launcher is installed:

```bash
py main.py
```

## Run Tests

```bash
python -m unittest discover tests
```

or:

```bash
py -m unittest discover tests
```

## Notes

- Uses only standard Python libraries.
- Generates 27 profiles from 3 topics, 3 proficiency levels, and 3 misconception types per topic.
- Query generation is deterministic, based on topic, proficiency, confidence, and misconception.
- `export_for_recommender()` returns JSON-serializable learner context suitable for downstream recommendation experiments.
