from pydantic import BaseModel


class ReviewResponse(BaseModel):
    score: int
    summary: str
    bugs: list[str]
    performance: list[str]
    security: list[str]
    best_practices: list[str]
    complexity: str
    refactored_code: str
    unit_tests: str
    explanation: str