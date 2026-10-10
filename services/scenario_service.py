
import json
from pathlib import Path

from models.schemas import EventGraph


DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "scenarios.json"


def load_scenarios() -> list[dict]:
    with DATA_FILE.open("r", encoding="utf-8") as file:
        raw_scenarios = json.load(file)

    validated_scenarios = []

    for raw in raw_scenarios:
        scenario = raw.copy()
        keywords = scenario.pop("keywords", [])

        # Validate the graph using our Pydantic schema.
        graph = EventGraph.model_validate(scenario)

        # Keep routing keywords separate from the public graph response.
        validated_scenarios.append({
            "graph": graph,
            "keywords": keywords
        })

    return validated_scenarios


def get_all_events() -> list[EventGraph]:
    return [item["graph"] for item in load_scenarios()]


def match_news(text: str) -> EventGraph | None:
    normalized_text = text.casefold()

    best_match = None
    best_score = 0

    for item in load_scenarios():
        score = sum(
            1 for keyword in item["keywords"]
            if keyword.casefold() in normalized_text
        )

        if score > best_score:
            best_score = score
            best_match = item["graph"]

    return best_match
