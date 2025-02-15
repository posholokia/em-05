from datetime import date
from typing import Type

from infrastructure.database.models.models import OilTradeResultModel
from interfaces.repository.trading import ITradingRepository
from infrastructure.database.connection import Database
from sqlalchemy import select
from sqlalchemy.sql.expression import between, desc


class TradingRepository(ITradingRepository):
    def __init__(self, db: Database, model: Type[OilTradeResultModel]):
        self.__db = db
        self.__model = model

    async def get_last_dates(self, limit: int) -> list[date]:
        async with self.__db.get_session() as session:
            smtp = (
                select(self.__model.date)
                .distinct()
                .order_by(desc(self.__model.date))
                .limit(limit)
            )
            result = await session.execute(smtp)
            return result.scalars().all()

    async def get_list_for_period(
        self,
        start_date: date,
        end_date: date,
        **filter_by
    ) -> list[OilTradeResultModel]:
        async with self.__db.get_session() as session:
            smtp = (
                select(self.__model)
                .where(
                    between(self.__model.date, start_date, end_date)
                )
                .filter_by(**filter_by)
            )
            result = await session.execute(smtp)
            return result.scalars().all()

    async def get_list(
        self,
        **filter_by,
    ) -> list[OilTradeResultModel]:
        async with self.__db.get_session() as session:
            smtp = (
                select(self.__model)
                .filter_by(**filter_by)
                .order_by(desc(self.__model.date))
            )
            result = await session.execute(smtp)
            return result.scalars().all()
