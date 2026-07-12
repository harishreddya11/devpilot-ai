from abc import ABC, abstractmethod
from app.schemas.review_response import ReviewResponse


class LLMProvider(ABC):

    @abstractmethod
    def review_code(
        self,
        language: str,
        code: str
    ) -> ReviewResponse:
        pass