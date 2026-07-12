from app.llm.provider_factory import ProviderFactory
from app.schemas.ai_request import AIRequest


class AIService:

    def __init__(self):
        self.provider = ProviderFactory.get_provider()

    def execute(self, request: AIRequest):

        return self.provider.execute(request)
    