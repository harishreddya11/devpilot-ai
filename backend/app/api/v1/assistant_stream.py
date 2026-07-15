from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.schemas.ai_request import AIRequest
from app.services.ai_service import AIService

router = APIRouter(
    prefix="/assistant",
    tags=["AI Assistant"],
)

service = AIService()


@router.post("/stream")
def stream(request: AIRequest):
    return StreamingResponse(
        service.stream(request),
        media_type="text/plain",
    )