from pydantic import BaseModel, Field, field_validator


class Transaction(BaseModel):
    transaction_id: str
    amount: float
    currency: str

    @field_validator("transaction_id")
    @classmethod
    def id_length(cls, v: str) -> str:
        if len(v) < 5:
            raise ValueError("transaction_id must be at least 5 characters")
        return v

    @field_validator("amount")
    @classmethod
    def amount_positive(cls, v: float) -> float:
        if v <= 0:
            raise ValueError("amount must be a positive number greater than zero")
        return v

    @field_validator("currency")
    @classmethod
    def validate_currency(cls, v: str) -> str:
        allowed = {"EUR", "USD", "CHF"}
        if v.upper() not in allowed:
            raise ValueError(f"Unsupported currency. Must be one of {allowed}")
        return v.upper()
