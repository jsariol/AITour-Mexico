# FastAPI Azure OpenAI Chat

A full-stack FastAPI app with a `/chat` API that calls Azure OpenAI, plus a PHP frontend.

## Requirements

- Python 3.11+
- PHP 8.2+

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

## Frontend Setup (PHP)

1. Start a local PHP server:

```bash
cd frontend
php -S localhost:8080
```

Open `http://localhost:8080`.

## Environment Variables

- `AZURE_OPENAI_ENDPOINT`
- `AZURE_OPENAI_AUTH_MODE` (aad|key)
- `AZURE_OPENAI_API_KEY`
- `AZURE_OPENAI_API_VERSION`
- `AZURE_OPENAI_DEPLOYMENT`
- `AZURE_OPENAI_TEMPERATURE`
- `AZURE_OPENAI_MAX_TOKENS`
- `ALLOWED_ORIGINS`
- `API_BASE_URL`

## Tests

```bash
pytest
```

## GitHub Copilot GPT-5.1-Codex in VS Code

- Install the GitHub Copilot and GitHub Copilot Chat extensions.
- In the Copilot Chat model picker, select `GPT-5.1-Codex` for this workspace.

## Deployment (Azure App Service)

Backend: the workflow in .github/workflows/deploy.yml deploys the API on pushes to `main`.

Frontend: the workflow in .github/workflows/deploy-php-frontend.yml deploys the PHP frontend to a separate App Service.

Add the following GitHub Actions secrets:

- `AZURE_WEBAPP_NAME`
- `AZURE_WEBAPP_PUBLISH_PROFILE`
- `AZURE_PHP_WEBAPP_NAME`
- `AZURE_PHP_WEBAPP_PUBLISH_PROFILE`

Set these application settings in Azure App Service:

- `AZURE_OPENAI_ENDPOINT`
- `AZURE_OPENAI_AUTH_MODE`
- `AZURE_OPENAI_API_KEY`
- `AZURE_OPENAI_API_VERSION`
- `AZURE_OPENAI_DEPLOYMENT`
- `AZURE_OPENAI_TEMPERATURE`
- `AZURE_OPENAI_MAX_TOKENS`
- `ALLOWED_ORIGINS`
- `API_BASE_URL`

Recommended startup command:

```bash
gunicorn -k uvicorn.workers.UvicornWorker app.main:app
```
