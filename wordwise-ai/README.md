# WordWise AI

A full-stack writing assistant with **live inline AI suggestions**, spelling correction chips, next-word completion, saved writing history, SQLite, and Docker deployment.

## Run with Docker (recommended)
Install Docker Desktop / Docker Engine with Compose, then from this directory run:

```bash
docker compose up --build
```
Open **http://localhost:8080**. API health is at `/api/health`. Stop with `docker compose down`. Saved writing history persists in the `wordwise_sqlite_data` volume. To delete that data too, use `docker compose down -v`.

## Run without Docker
Requires Node.js 20+, Python 3.11+, and pip.

1. ML service: `cd ml-service`, create/activate a venv, `pip install -r requirements.txt`, then `uvicorn main:app --reload --host 127.0.0.1 --port 8000`.
2. API in another terminal: `cd backend`, `npm install`, copy `.env.example` to `.env`, then `npm run dev`.
3. Frontend in another terminal: `cd frontend`, `npm install`, then `npm run dev`. Open `http://localhost:5173`.

## API
- `GET /api/health` — API, SQLite and ML service status
- `POST /api/writing/analyze` — `{ "text": "I want to lern" }`
- `POST /api/history` — analyze and save writing
- `GET /api/history?limit=20` — recent saved sessions
- `GET /api/history/:id` — one saved session
- `DELETE /api/history/:id` — delete a saved session

## Important limitations
The included Python engine is a small n-gram demonstration model and dictionary spell checker, not a trained high-accuracy language model. Review corrections before applying them. This starter has no user accounts; history is shared by anyone with access to this deployment. Do not save sensitive text in a public demo.

## Deployment notes
Docker Compose is a reproducible single-host deployment path, not a guarantee that every cloud provider supports this exact configuration. Use a Docker-capable host with persistent volumes, HTTPS via a reverse proxy, backups for the SQLite volume, and appropriate access controls. SQLite is suitable for a single-instance app; consider PostgreSQL for multiple API replicas or heavy concurrent writes.

## Inline AI writing behavior
- Suggestions run automatically after a short pause while typing; no “Improve my writing” button or separate review panel is needed.
- Spelling corrections appear directly below the editor as clickable chips. Click a correction to replace that word in place.
- When a next-word prediction is available, it appears in the editor area. Press **Tab** or **Enter**, or click the suggestion, to accept it. Press **Esc** to dismiss it.
- The editor continues to use the existing `/api/writing/analyze` API, so Node.js forwards analysis to the Python ML service.
- The bundled model is still a small demonstration corpus plus a dictionary spell checker. Suggestions may be inaccurate; click a correction only when it looks right.
