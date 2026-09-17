from fastapi import APIRouter

from app.models.requests import SupportQueryRequest
from app.models.responses import SupportQueryResponse


router = APIRouter(
    prefix="/api/v1/support",
    tags=["Support"],
)


@router.post("/query", response_model=SupportQueryResponse)
def support_query(request: SupportQueryRequest):
    return SupportQueryResponse(
        success=True,
        merchant_id=request.merchant_id,
        intent="unknown",
        requires_human=False,
        response="Your support query has been received successfully.",
    )