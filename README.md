# ORBITAL SI — Space Fire Intelligence Platform

React + Vite frontend prototype for a space-habitat fire prediction and safety support dashboard.

## Run locally

```bash
npm install
npm run dev
```

## Current prototype pages

- **Home** — mission overview and platform status.
- **Agent 1** — fire prediction dashboard with six placeholder telemetry indicators: air flow velocity (m/s), ambient temperature (°C), CO₂ (%), cabin pressure (kPa), O₂ (%), and material flammability index.
- **Agent 2** — incident intake, technical-analysis preview, and placeholder safety action plan.
- **About** — platform overview and proposed agent integration flow.

All telemetry and model responses are sample placeholders. No real sensors, prediction model, or safety system is connected.

## Where to connect the agents

Use a backend orchestration/API layer between the frontend and the two agents. Suggested flow:

1. The frontend sends telemetry to `POST /api/telemetry`.
2. The backend validates and stores readings, then calls Agent 1 (fire prediction).
3. Agent 1 returns a structured prediction, e.g. `{ "risk_score": 0, "confidence": 0, "risk_factors": [], "summary": "" }`.
4. For an incident, the frontend sends the incident description plus relevant telemetry and Agent 1 output to `POST /api/incidents/analyze`.
5. The backend calls Agent 2 and returns structured fields such as `assessment`, `technical_findings`, `recommended_actions`, and `severity`.
6. The frontend renders those API responses in the Agent 1 and Agent 2 pages.

Keep API keys and model credentials on the backend, never in the React client. Treat Agent 2 output as decision support for qualified human review, not as a substitute for certified emergency procedures.

## Frontend integration points

- Replace the sample `metrics` array and placeholder risk summary in `src/components/PageView.jsx` with state populated from the telemetry/prediction API.
- Replace the `submitted` demo response in `AgentTwo` with a request to `POST /api/incidents/analyze` and render the returned result.
- Keep API request helpers in a dedicated module such as `src/services/agents.js` so the UI components do not contain endpoint or authentication logic.


## Agent 1 — n8n production webhook

Agent 1 now sends a `POST` request to the production webhook configured in `src/components/PageView.jsx` when **Run Fire Prediction** is clicked. The request includes a `sensor_data` object and an `environmental_data` object with oxygen concentration, cabin pressure, airflow velocity, ambient temperature, CO2 concentration, and material flammability index.

The UI accepts common n8n response shapes, including a direct JSON object, an array containing an item, and an `output` / `body` JSON string. For the best display, return fields such as `overall_fire_risk` (0–100), `prediction_probability` (0–100), `risk_category`, `model_confidence` (0–100), `agent_reasoning`, `predicted_scenarios` (critical/elevated/low percentages), and `risk_factor_breakdown` (oxygen/pressure/airflow/materials values from 0–100). Missing fields fall back to illustrative UI values and should be replaced by real model output.

**Important:** the browser calls the n8n webhook directly. The n8n workflow must be active and its response must allow the website origin through CORS. For production deployments where the webhook should not be publicly callable, proxy this request through a backend and keep any credentials server-side.
