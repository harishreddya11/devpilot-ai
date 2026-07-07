from pydantic import BaseModel, Field


class ReviewRequest(BaseModel):
    language: str = Field(
        ...,
        min_length=2,
        max_length=30,
        description="Programming language",
    )

    code: str = Field(
        ...,
        min_length=10,
        description="Source code to review",
    )