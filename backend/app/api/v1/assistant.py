from fastapi import APIRouter

from app.schemas.ai_request import AIRequest
from app.schemas.ai_response import AIResponse
from app.services.ai_service import AIService

router = APIRouter(
    prefix="/assistant",
    tags=["AI Assistant"],
)

service = AIService()


@router.post(
    "/",
    response_model=AIResponse,
)
def execute(request: AIRequest):
    return service.execute(request)