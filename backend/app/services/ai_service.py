from app.llm.provider_factory import ProviderFactory
from app.schemas.ai_request import AIRequest
from app.schemas.ai_response import AIResponse


class AIService:
    """
    Coordinates AI requests and delegates them to the configured provider.
    """

    def __init__(self) -> None:
        self.provider = ProviderFactory.get_provider()

    def execute(self, request: AIRequest) -> AIResponse:
        return self.provider.execute(request)