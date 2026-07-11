from app.llm.provider_factory import ProviderFactory
from app.schemas.review import ReviewRequest
from app.schemas.review_response import ReviewResponse


class ReviewService:

    def review_code(
        self,
        request: ReviewRequest,
    ) -> ReviewResponse:

        provider = ProviderFactory.get_provider()

        return provider.review_code(
            request.language,
            request.code,
        )