from pydantic import BaseModel


class AIResponse(BaseModel):
    """
    Generic response returned by the AI provider.
    """

    task: str

    result: str