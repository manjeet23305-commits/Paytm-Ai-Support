from fastapi import FastAPI

from app.routes.support import router as support_router


app = FastAPI(
    title="SupportOps AI",
    description="AI-powered support investigation agent for multilingual issue resolution",
    version="0.1.0",
)


app.include_router(support_router)


@app.get("/")
def root():
    return {
        "success": True,
        "message": "SupportOps AI API is running",
        "version": "0.1.0",
    }


@app.get("/health")
def health_check():
    return {
        "success": True,
        "status": "healthy",
    }