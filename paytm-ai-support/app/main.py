from fastapi import FastAPI

from app.routes.support import router as support_router


app = FastAPI(
    title="Paytm AI Support Teammate",
    description="AI-powered multilingual support backend for Paytm merchants",
    version="0.1.0",
)


app.include_router(support_router)


@app.get("/")
def root():
    return {
        "success": True,
        "message": "Paytm AI Support Teammate API is running",
        "version": "0.1.0",
    }


@app.get("/health")
def health_check():
    return {
        "success": True,
        "status": "healthy",
    }