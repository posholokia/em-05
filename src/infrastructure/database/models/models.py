from sqlalchemy.orm import Mapped

from infrastructure.database.models.base import BaseModel
from infrastructure.database.models.mapped_values import (
    str11,
    str4,
    str3,
    str1,
    date,
    datetime_tz,
)


class OilTradeResultModel(BaseModel):
    __tablename__ = 'oil_trade_result'

    exchange_product_id: Mapped[str11]
    exchange_product_name: Mapped[str]
    oil_id: Mapped[str4]
    delivery_basis_id: Mapped[str3]
    delivery_basis_name: Mapped[str]
    delivery_type_id: Mapped[str1]
    volume: Mapped[int]
    total: Mapped[int]
    count: Mapped[int]
    date: Mapped[date]
    created_on: Mapped[datetime_tz]
    updated_on: Mapped[datetime_tz]
