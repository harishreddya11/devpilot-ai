from fastapi import APIRouter

from app.schemas.review import ReviewRequest
from app.services.review_service import ReviewService

router = APIRouter(
    prefix="/review",
    tags=["Code Review"],
)

review_service = ReviewService()


@router.post("/")
def review_code(request: ReviewRequest):
    return review_service.review_code(request)