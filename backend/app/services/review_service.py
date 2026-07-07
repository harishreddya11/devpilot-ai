from app.schemas.review import ReviewRequest


class ReviewService:
    """
    Handles all code review business logic.
    """

    def review_code(self, request: ReviewRequest) -> dict:
        return {
            "score": 8,
            "summary": "Good code. Minor improvements suggested.",
            "bugs": [
                "No input validation."
            ],
            "performance": [
                "Performance is acceptable."
            ],
            "security": [
                "No obvious security issues."
            ],
            "refactored_code": request.code
        }