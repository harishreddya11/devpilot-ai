from abc import ABC, abstractmethod

from app.schemas.review_response import ReviewResponse


class LLMProvider(ABC):
    """
    Abstract base class for all LLM providers.
    """

    @abstractmethod
    def review_code(
        self,
        language: str,
        code: str,
    ) -> ReviewResponse:
        """
        Review the submitted code.
        """
        raise NotImplementedError