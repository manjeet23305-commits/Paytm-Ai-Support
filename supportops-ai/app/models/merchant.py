from pydantic import BaseModel


class Merchant(BaseModel):
    merchant_id: str
    merchant_name: str
    phone: str
    settlement_account: str
    status: str