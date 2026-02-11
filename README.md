# FastAPI Azure OpenAI Chat

A full-stack FastAPI app with a `/chat` API that calls Azure OpenAI, plus a Next.js frontend.

## Requirements

- Python 3.11+
- Node.js 18+

## Backend Setup

1. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

2. Copy `.env.example` to `.env` and fill in your Azure OpenAI values.

3. Run the API locally:

```bash
uvicorn app.main:app --reload
```

API runs at `http://localhost:8000`.

## Frontend Setup (Next.js)

1. Install dependencies:

```bash
cd frontend
npm install
```

2. Copy `frontend/.env.example` to `frontend/.env.local` and update the API base if needed.

3. Run the frontend:

```bash
npm run dev
```

Open `http://localhost:3000`.

## Environment Variables

- `AZURE_OPENAI_ENDPOINT`
- `AZURE_OPENAI_AUTH_MODE` (aad|key)
- `AZURE_OPENAI_API_KEY`
- `AZURE_OPENAI_API_VERSION`
- `AZURE_OPENAI_DEPLOYMENT`
- `AZURE_OPENAI_TEMPERATURE`
- `AZURE_OPENAI_MAX_TOKENS`
- `ALLOWED_ORIGINS`
- `NEXT_PUBLIC_API_BASE`

## Tests

```bash
pytest
```

## GitHub Copilot GPT-5.1-Codex in VS Code

- Install the GitHub Copilot and GitHub Copilot Chat extensions.
- In the Copilot Chat model picker, select `GPT-5.1-Codex` for this workspace.

## Deployment (Azure App Service + Static Web Apps)

Backend: the workflow in .github/workflows/deploy.yml deploys the API on pushes to `main`.

Frontend: the workflow in .github/workflows/deploy-frontend.yml deploys the Next.js static export to Azure Static Web Apps.

Add the following GitHub Actions secrets:

- `AZURE_WEBAPP_NAME`
- `AZURE_WEBAPP_PUBLISH_PROFILE`
- `AZURE_STATIC_WEB_APPS_API_TOKEN`

Set these application settings in Azure App Service:

- `AZURE_OPENAI_ENDPOINT`
- `AZURE_OPENAI_AUTH_MODE`
- `AZURE_OPENAI_API_KEY`
- `AZURE_OPENAI_API_VERSION`
- `AZURE_OPENAI_DEPLOYMENT`
- `AZURE_OPENAI_TEMPERATURE`
- `AZURE_OPENAI_MAX_TOKENS`
- `ALLOWED_ORIGINS`
- `NEXT_PUBLIC_API_BASE`

Set `NEXT_PUBLIC_API_BASE` as a build environment variable in Azure Static Web Apps to point to the App Service URL.

Recommended startup command:

```bash
gunicorn -k uvicorn.workers.UvicornWorker app.main:app
```
