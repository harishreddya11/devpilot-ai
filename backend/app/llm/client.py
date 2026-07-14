from openai import OpenAI

from app.core.config import get_settings


def get_client() -> OpenAI:
    settings = get_settings()

    return OpenAI(
        api_key=settings.openrouter_api_key,
        base_url="https://openrouter.ai/api/v1",
    )