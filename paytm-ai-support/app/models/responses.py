from pydantic import BaseModel


class SupportQueryResponse(BaseModel):
    success: bool
    merchant_id: str
    intent: str
    requires_human: bool
    response: str