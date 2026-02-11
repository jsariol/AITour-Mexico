from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import AzureOpenAI

from .config import Settings


class AzureOpenAIChatClient:
    def __init__(self, settings: Settings) -> None:
        self._settings = settings
        auth_mode = settings.azure_openai_auth_mode.lower()
        if auth_mode == "aad":
            token_provider = get_bearer_token_provider(
                DefaultAzureCredential(),
                "https://cognitiveservices.azure.com/.default",
            )
            self._client = AzureOpenAI(
                api_version=settings.azure_openai_api_version,
                azure_endpoint=settings.azure_openai_endpoint,
                azure_ad_token_provider=token_provider,
            )
        else:
            if not settings.azure_openai_api_key:
                raise ValueError("AZURE_OPENAI_API_KEY is required when using key auth.")
            self._client = AzureOpenAI(
                api_key=settings.azure_openai_api_key,
                api_version=settings.azure_openai_api_version,
                azure_endpoint=settings.azure_openai_endpoint,
            )

    @property
    def deployment_name(self) -> str:
        return self._settings.azure_openai_deployment

    def complete(self, message: str) -> str:
        response = self._client.chat.completions.create(
            model=self._settings.azure_openai_deployment,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message},
            ],
            temperature=self._settings.azure_openai_temperature,
            max_tokens=self._settings.azure_openai_max_tokens,
        )
        choice = response.choices[0].message
        return choice.content or ""
