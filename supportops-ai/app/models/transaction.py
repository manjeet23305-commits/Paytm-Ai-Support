from datetime import datetime

from pydantic import BaseModel


class Transaction(BaseModel):
    transaction_id: str
    merchant_id: str
    amount: float
    status: str
    transaction_date: datetime
    settlement_date: datetime | None = None