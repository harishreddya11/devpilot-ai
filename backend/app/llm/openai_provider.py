from app.core.config import get_settings
from app.llm.base import LLMProvider
from app.llm.client import get_client
from app.llm.prompts import SYSTEM_PROMPT, build_generate_prompt
from app.schemas.ai_request import AIRequest
from app.schemas.ai_response import AIResponse
from app.schemas.task import TaskType

settings = get_settings()


class OpenAIProvider(LLMProvider):

    def execute(self, request: AIRequest) -> AIResponse:

        client = get_client()

        if request.task != TaskType.GENERATE:
            return AIResponse(
                task=request.task.value,
                language=request.language,
                result="Task not implemented yet.",
                model=settings.openrouter_model,
            )

        response = client.chat.completions.create(
            model=settings.openrouter_model,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": build_generate_prompt(
                        request.language,
                        request.prompt or "",
                    ),
                },
            ],
        )

        generated_code = response.choices[0].message.content or ""

        return AIResponse(
            task=request.task.value,
            language=request.language,
            result=generated_code,
            model=settings.openrouter_model,
        )