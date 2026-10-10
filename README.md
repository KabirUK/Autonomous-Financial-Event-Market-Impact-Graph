# FinFlow AI — Financial Event Market Impact Graph

## Overview

FinFlow AI is a backend API prototype that maps financial news text to predefined event graphs. Each graph represents a financial event and its possible relationships with affected commodities, indicators, countries, sectors, companies, or assets.

The API currently uses keyword matching and predefined scenarios. It does not perform live AI analysis or verify current news.

## Technology Stack

- Python
- FastAPI
- Pydantic
- Uvicorn
- JSON scenario data

## Project Structure

```text
FinancialEvent/
├── app.py
├── models/
│   └── schemas.py
├── services/
│   └── scenario_service.py
├── data/
│   └── scenarios.json
├── tests/
│   └── mock_graph.json
├── CONTRACT.md
├── SCORING.md
└── README.md
```

## Setup

Activate the project's virtual environment in PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies if needed:

```powershell
python -m pip install fastapi "uvicorn[standard]"
```

Start the backend:

```powershell
python -m uvicorn app:app --reload --port 8000
```

The API runs at:

`http://127.0.0.1:8000`

Interactive API documentation:

`http://127.0.0.1:8000/docs`

## API Endpoints

### GET `/health`

Checks whether the API is running.

Example response:

```json
{
  "status": "healthy"
}
```

### GET `/events`

Returns all predefined event graphs.

The current demonstration scenarios cover:
- Crude oil supply disruption.
- Reserve Bank of India interest rates.
- US Federal Reserve interest rates.

### POST `/news/analyze`

Matches submitted text against the predefined scenario keywords.

Example request:

```json
{
  "text": "OPEC announces crude oil supply disruption, pushing oil prices higher."
}
```

A successful match returns:

- `matched`: whether a scenario matched.
- `event`: the matched event graph, or `null` if no scenario matched.
- `message`: an explanation of the matching result.

An unmatched request returns `matched: false` and `event: null`.

## Graph Structure

An event graph contains:
- `nodes`: entities affected by or associated with the event.
- `edges`: directed relationships between nodes.
- `strength`: a provisional value from `0.0` to `1.0`.
- `direction`: `POSITIVE`, `NEGATIVE`, `MIXED`, or `UNKNOWN`.
- `evidence_type`: indicates the evidence classification.
- `limitations`: known caveats and uncertainty.

## Frontend Integration

The frontend development server may call the backend from:

- `http://localhost:5173`
- `http://127.0.0.1:5173`

These origins are configured in the API's CORS settings.

The fixture at `tests/mock_graph.json` provides an example response for frontend development.

## Current Limitations

- Scenario matching is keyword-based.
- Only predefined scenarios are supported.
- No live news retrieval is implemented.
- No LLM-based extraction is implemented.
- Demonstration strength values are not calibrated probabilities.
- Evidence and limitations must be reviewed before treating a relationship as verified.

## Future Work

- Integrate a reliable news source.
- Extract events and entities using an LLM with structured output.
- Add source-backed evidence and timestamps.
- Develop and validate a documented scoring methodology.
- Add automated API tests.
- Consider historical market data and graph database integration.

## Responsible Use

This prototype is for demonstration and educational purposes. Its output is not investment advice and should not be treated as a verified prediction of market movements.
## Frontend Integration Guide

### Backend Base URL

```text
http://localhost:8000
```

Start the backend from the project root:

```powershell
python -m uvicorn app:app --reload --port 8000
```

### API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/health` | Check backend status |
| GET | `/events` | Fetch predefined scenario graphs |
| POST | `/news/analyze` | Match news text to a scenario |

### Analyze News

**Request:**

```json
{
  "text": "OPEC announces crude oil supply disruption, pushing oil prices higher."
}
```

**Successful response fields:**

- `matched`: whether a predefined scenario matched
- `event`: the matched event graph, or `null`
- `message`: explanation of the result

The event graph contains `nodes` and `edges`, which the frontend can use to render the financial impact graph.

### Frontend Requirements

- Send requests to `http://localhost:8000`.
- Send `POST /news/analyze` with `Content-Type: application/json`.
- Use `matched` to distinguish a match from an unmatched result.
- Render the returned graph using its `nodes` and `edges`.
- Display the returned `message`.
- Treat scenario results as illustrative, not verified live-news analysis.
- The Vite development server is allowed by CORS at `http://localhost:5173` and `http://127.0.0.1:5173`.

### API Documentation

Open `http://localhost:8000/docs` to test endpoints interactively.