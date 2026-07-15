from abc import ABC, abstractmethod

from app.schemas.ai_request import AIRequest
from app.schemas.ai_response import AIResponse


class LLMProvider(ABC):

    @abstractmethod
    def execute(self, request: AIRequest) -> AIResponse:
        pass

    @abstractmethod
    def stream(self, request: AIRequest):
        pass