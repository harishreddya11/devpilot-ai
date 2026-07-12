from pydantic import BaseModel, Field

from app.schemas.task import TaskType


class AIRequest(BaseModel):
    """
    Generic request for all AI tasks.
    """

    task: TaskType

    language: str = Field(
        ...,
        min_length=2,
        max_length=30,
    )

    prompt: str | None = None

    code: str | None = None