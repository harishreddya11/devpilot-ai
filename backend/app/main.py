from fastapi import FastAPI

from app.api.v1.review import router as review_router
from app.core.config import get_settings

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

app.include_router(
    review_router,
    prefix="/api/v1",
)


@app.get("/")
def home():
    return {
        "message": f"Welcome to {settings.app_name}",
        "version": settings.app_version,
    }