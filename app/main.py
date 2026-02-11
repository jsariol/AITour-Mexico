import os

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .azure_openai_client import AzureOpenAIChatClient
from .config import Settings
from .schemas import ChatRequest, ChatResponse

app = FastAPI()


def get_settings() -> Settings:
    return Settings()


def get_chat_client(settings: Settings = Depends(get_settings)) -> AzureOpenAIChatClient:
    return AzureOpenAIChatClient(settings)


allowed_origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin.strip() for origin in allowed_origins.split(",") if origin.strip()],
    allow_credentials=False,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)


@app.get("/")
def index() -> dict[str, str]:
    return {"status": "ok", "message": "API is running."}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
def chat(
    request: ChatRequest,
    client: AzureOpenAIChatClient = Depends(get_chat_client),
) -> ChatResponse:
    try:
        reply = client.complete(request.message)
    except Exception as exc:
        raise HTTPException(status_code=500, detail="Azure OpenAI request failed.") from exc

    return ChatResponse(reply=reply, model=client.deployment_name)
