from pydantic import BaseModel, Field, field_validator


class SupportQueryRequest(BaseModel):
    merchant_id: str = Field(
        ...,
        min_length=1,
        description="Unique merchant identifier",
    )

    query: str = Field(
        ...,
        min_length=1,
        description="Merchant's support query",
    )

    @field_validator("merchant_id", "query")
    @classmethod
    def validate_not_blank(cls, value: str) -> str:
        value = value.strip()

        if not value:
            raise ValueError("Value cannot be blank")

        return value