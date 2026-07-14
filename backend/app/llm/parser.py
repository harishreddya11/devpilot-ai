import json

from app.schemas.ai_request import AIRequest
from app.schemas.ai_response import AIResponse


def parse_response(
    request: AIRequest,
    response_text: str,
    model: str,
) -> AIResponse:

    try:
        data = json.loads(response_text)

        return AIResponse(
            task=request.task.value,
            language=request.language,
            code=data["code"],
            explanation=data["explanation"],
            complexity=data["complexity"],
            suggestions=data["suggestions"],
            model=model,
        )

    except Exception:

        return AIResponse(
            task=request.task.value,
            language=request.language,
            code=response_text,
            explanation="Unable to parse AI response.",
            complexity="Unknown",
            suggestions=[],
            model=model,
        )