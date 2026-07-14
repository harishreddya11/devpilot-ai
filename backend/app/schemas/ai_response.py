from pydantic import BaseModel


class AIResponse(BaseModel):
    task: str
    language: str
    code: str
    explanation: str
    model: str