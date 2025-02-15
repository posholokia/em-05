from datetime import date

from pydantic import BaseModel, ConfigDict, Field


class TradeDateSchema(BaseModel):
    dates: list[date]


class TradeResultSchema(BaseModel):
    id: int
    exchange_product_id: str
    exchange_product_name: str
    oil_id: str
    delivery_basis_id: str
    delivery_basis_name: str
    delivery_type_id: str
    volume: int
    total: int
    count: int
    date: date

    model_config = ConfigDict(from_attributes=True)


class TradeFilterSchema(BaseModel):
    oil_id: str | None = Field(default=None, max_length=4, min_length=4)
    delivery_type_id: str | None = Field(default=None, max_length=1, min_length=1)
    delivery_basis_id: str | None = Field(default=None, max_length=3, min_length=3)


class TradePeriodFilterSchema(TradeFilterSchema):
    start_date: date = Field(description="2025-01-01")
    end_date: date = Field(examples=["2025-01-31"])
