# 🌍 Autonomous Financial Event Market Impact Graph

## From Financial News to Explainable Market Impact

An explainable financial intelligence project intended to show how financial news and geopolitical events may affect countries, commodities, industries, companies, and financial markets.

Instead of only predicting prices, the project focuses on explaining what happened, how possible effects may spread, and what evidence supports each relationship.

**Current implementation status:** The backend currently matches submitted text to three predefined illustrative scenarios using keyword matching. Live-news retrieval, LLM-based event extraction, evidence verification, Neo4j integration, historical market analysis, and the full interactive graph workflow are planned capabilities—not implemented features yet.

## About the Project

Financial events can affect multiple connected parts of the economy. For example, an oil supply disruption may increase crude oil prices, raise transportation costs, contribute to inflationary pressure, and affect oil-importing and oil-producing countries differently.

The project aims to make these potential transmission paths explorable through an interactive knowledge graph, with explanations, evidence, limitations, and uncertainty made visible.

## Current Backend MVP

The current backend provides:

- A FastAPI application with health, scenario-listing, and news-analysis endpoints.
- Pydantic schemas for events, graph nodes, graph edges, and evidence.
- Three predefined illustrative scenarios:
  - Crude oil supply disruption.
  - Reserve Bank of India interest rates.
  - US Federal Reserve interest rates.
- Keyword-based matching of submitted text to a predefined scenario.
- Graph validation, including unique node/edge IDs and valid edge references.
- CORS support for the local Vite frontend origins.
- Automated API tests.

The current output is illustrative, not verified live-news analysis or investment advice.

## Technology Stack

| Component | Current / planned technology |
|---|---|
| Backend API | Python, FastAPI, Uvicorn |
| Data validation | Pydantic |
| Scenario data | JSON |
| Tests | pytest, FastAPI TestClient, httpx |
| Frontend | React and Vite (planned/integration target) |
| Interactive graph | Cytoscape.js (planned) |
| Knowledge graph database | Neo4j (planned) |
| Data analysis | pandas and NumPy (planned) |
| AI and NLP | LLM API with structured outputs (planned) |
| Country map | Leaflet or MapLibre GL (planned) |

Exact dependencies and versions for future components will be decided during implementation.

## Project Structure

```text
FinancialEvent/
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
├── CONTRACT.md
├── SCORING.md
├── models/
│   └── schemas.py
├── services/
│   └── scenario_service.py
├── data/
│   └── scenarios.json
└── tests/
    ├── mock_graph.json
    └── test_api.py
```

## Setup and Run the Backend

Use Python installed on your machine. From the project root, create and activate a virtual environment if you do not already have one.

### PowerShell (Windows)

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn app:app --reload --port 8000
```

The API runs at:

- **Base URL:** http://127.0.0.1:8000
- **Interactive API documentation:** http://127.0.0.1:8000/docs

## API Endpoints

### `GET /health`

Checks whether the API is running.

Example response:

```json
{
  "status": "healthy"
}
```

### `GET /events`

Returns the predefined illustrative event graphs. These are demo scenarios, not verified live-news events.

The current scenarios cover oil supply disruption, RBI interest rates, and US Federal Reserve interest rates.

### `POST /news/analyze`

Matches submitted text against the predefined scenario keywords.

Example request:

```json
{
  "text": "OPEC announces crude oil supply disruption, pushing oil prices higher."
}
```

A successful response contains:

- `matched`: whether a predefined scenario matched.
- `event`: the matched event graph, or `null` if there was no match.
- `message`: an explanation of the result.

An unmatched request returns `matched: false`, `event: null`, and a message explaining that no predefined scenario matched. Requests outside the accepted text length are rejected by request validation.

See `CONTRACT.md` for the API response contract.

## Frontend Integration

The backend CORS configuration allows these local Vite origins:

- `http://localhost:5173`
- `http://127.0.0.1:5173`

Use `http://localhost:8000` as the frontend API base URL.

For news analysis, send a `POST` request to `/news/analyze` with `Content-Type: application/json` and a JSON body containing `text`.

Use `matched` to decide whether to render the returned graph, render the `nodes` and `edges` from `event`, and display `message` to the user.

The fixture at `tests/mock_graph.json` provides an example graph response for development.

## Graph Structure and Scoring

An event graph contains:

- `nodes`: entities affected by or associated with the event.
- `edges`: directed relationships between nodes.
- `strength`: a provisional value from `0.0` to `1.0`.
- `direction`: `POSITIVE`, `NEGATIVE`, `MIXED`, or `UNKNOWN`.
- `evidence_type`: the relationship's evidence classification.
- `limitations`: caveats and uncertainty.

A strength score is not a probability of a future market movement and is not a calibrated prediction. Current scenario strengths are demonstration values. See `SCORING.md` for the current scoring notes.

The intended system should distinguish between:

- **Observed facts:** Claims supported by sources or recorded data.
- **Established relationships:** Economic mechanisms supported by credible evidence.
- **Inferred hypotheses:** Possible connections requiring further verification.
- **Insufficient verified evidence:** Used when reliable support is unavailable.

The application must not invent statistics, historical events, or citations when evidence is unavailable.

## Example Impact Path: Oil Supply Disruption

Possible pathways to investigate include:

- **Transportation:** Oil supply disruption → crude oil prices rise → fuel costs may increase → transportation operating costs may rise.
- **Inflation and monetary policy:** Crude oil prices rise → energy costs may increase → inflationary pressure may rise → interest-rate expectations may change.
- **Country exposure:** Changes in oil availability and prices may affect oil-importing and oil-producing countries differently.

These pathways are hypotheses, not guaranteed outcomes. Historical correlation alone does not establish causation.

## Current Limitations

- Matching is keyword-based.
- Only predefined scenarios are supported.
- No live news retrieval is implemented.
- No LLM-based extraction is implemented.
- Evidence is not verified against live sources.
- Demonstration strength values are not calibrated probabilities.
- Neo4j, impact-path ranking, country-wise analysis, and historical market-data analysis are not yet implemented.

## Roadmap

The broader project roadmap is to:

1. Agree on shared schemas and relationship vocabulary.
2. Build and review a small knowledge graph.
3. Connect the React graph interface to the API.
4. Add event and entity extraction.
5. Integrate Neo4j and graph queries.
6. Implement documented relationship scoring and impact-path traversal.
7. Add source-backed evidence and an evidence panel.
8. Add verified historical examples and market charts.
9. Develop country-wise exposure analysis and a map.
10. Test the complete workflow and document limitations.

Roadmap items should be marked complete only after implementation and testing.

## Team Responsibilities

### Member 1 — Backend, AI, and Knowledge Graph

- Maintain the API and shared schemas.
- Implement event/entity extraction as a future capability.
- Validate and retrieve graph entities and relationships.
- Develop and evaluate relationship scoring.
- Implement impact-path traversal.
- Connect evidence and historical references to relationships.
- Return structured JSON responses to the frontend.

**Deliverable:** A backend that accepts an event and returns validated entities, scored relationships, impact paths, and available supporting evidence as those capabilities are implemented.

### Member 2 — Frontend, Visualization, and Integration

- Build the React dashboard and event input.
- Render the graph and implement graph interactions.
- Build impact-path and evidence panels.
- Develop country-map and comparison interfaces.
- Add historical charts when validated data is available.
- Integrate the frontend with the backend and test the end-to-end workflow.

**Deliverable:** An interactive dashboard where users can submit an event, explore its graph, inspect relationships, and compare possible impacts.

Both members should agree on the shared API contract. The frontend can use mock data while backend capabilities are being developed.

## Testing

Run the backend tests from the project root:

```powershell
python -m pytest -v
```

The current test suite covers the health endpoint, scenario listing, a successful oil-scenario match, unmatched text, and short-text validation.

Future evaluation should assess entity and relationship extraction, evidence validity, impact-path relevance, country/asset mapping, historical-data correctness, and predictive performance if a separate prediction model is developed.

Do not claim an accuracy percentage before evaluation.

## Responsible Use

This prototype is for demonstration and educational purposes. Its output is not investment advice and should not be treated as a verified prediction of market movements.

---

**Trace the shock. Test the chain. Check reality.**