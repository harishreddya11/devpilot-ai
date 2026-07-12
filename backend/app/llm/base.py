from abc import ABC, abstractmethod

from app.schemas.ai_request import AIRequest
from app.schemas.ai_response import AIResponse


class LLMProvider(ABC):
    """
    Base interface for all LLM providers.
    """

    @abstractmethod
    def execute(self, request: AIRequest) -> AIResponse:
        """
        Execute an AI task.
        """
        raise NotImplementedError