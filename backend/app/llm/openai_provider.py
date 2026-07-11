from app.llm.base import LLMProvider
from app.schemas.review_response import ReviewResponse


class OpenAIProvider(LLMProvider):

    def review_code(
        self,
        language: str,
        code: str,
    ) -> ReviewResponse:

        print("✅ OpenAIProvider.review_code() called")

        return ReviewResponse(
    score=100,
    summary="THIS IS FROM OpenAIProvider",
    bugs=["Bug A"],
    performance=["Performance A"],
    security=["Security A"],
    best_practices=["Best Practice A"],
    complexity="Very Low",
    refactored_code="HELLO FROM PROVIDER",
    unit_tests="TESTS",
    explanation="Provider is working."
)