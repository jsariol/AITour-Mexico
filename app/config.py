from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    azure_openai_endpoint: str = Field(..., alias="AZURE_OPENAI_ENDPOINT")
    azure_openai_auth_mode: str = Field("aad", alias="AZURE_OPENAI_AUTH_MODE")
    azure_openai_api_key: str | None = Field(None, alias="AZURE_OPENAI_API_KEY")
    azure_openai_api_version: str = Field("2024-06-01", alias="AZURE_OPENAI_API_VERSION")
    azure_openai_deployment: str = Field(..., alias="AZURE_OPENAI_DEPLOYMENT")
    azure_openai_temperature: float = Field(0.2, alias="AZURE_OPENAI_TEMPERATURE")
    azure_openai_max_tokens: int = Field(512, alias="AZURE_OPENAI_MAX_TOKENS")
    allowed_origins: str = Field("http://localhost:8000", alias="ALLOWED_ORIGINS")

    def allowed_origin_list(self) -> list[str]:
        return [origin.strip() for origin in self.allowed_origins.split(",") if origin.strip()]
