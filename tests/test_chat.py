from fastapi.testclient import TestClient

from app.main import app, get_chat_client


class StubChatClient:
    deployment_name = "stub-deployment"

    def complete(self, message: str) -> str:
        return f"Echo: {message}"


def setup_env(monkeypatch) -> None:
    monkeypatch.setenv("AZURE_OPENAI_ENDPOINT", "https://example.openai.azure.com/")
    monkeypatch.setenv("AZURE_OPENAI_AUTH_MODE", "key")
    monkeypatch.setenv("AZURE_OPENAI_API_KEY", "test-key")
    monkeypatch.setenv("AZURE_OPENAI_API_VERSION", "2024-06-01")
    monkeypatch.setenv("AZURE_OPENAI_DEPLOYMENT", "test-deployment")
    monkeypatch.setenv("AZURE_OPENAI_TEMPERATURE", "0.2")
    monkeypatch.setenv("AZURE_OPENAI_MAX_TOKENS", "32")
    monkeypatch.setenv("ALLOWED_ORIGINS", "http://localhost:8000")


def test_chat_returns_reply(monkeypatch):
    setup_env(monkeypatch)
    app.dependency_overrides[get_chat_client] = lambda: StubChatClient()

    with TestClient(app) as client:
        response = client.post("/chat", json={"message": "Hello"})

    app.dependency_overrides.clear()

    assert response.status_code == 200
    body = response.json()
    assert body["reply"] == "Echo: Hello"
    assert body["model"] == "stub-deployment"


def test_chat_validation(monkeypatch):
    setup_env(monkeypatch)

    with TestClient(app) as client:
        response = client.post("/chat", json={"message": ""})

    assert response.status_code == 422
