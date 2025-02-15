from abc import ABC, abstractmethod

from datetime import date

from infrastructure.database.models.models import OilTradeResultModel


class ITradingRepository(ABC):
    @abstractmethod
    async def get_last_dates(self, limit: int) -> list[date]:
        """
        Выгрузка дат последних торговых дней.

        :param limit: Кол-во торговых дней.
        :return: Список дат последних торговых дней.
        """

    @abstractmethod
    async def get_list_for_period(
        self,
        start_date: date,
        end_date: date,
        **filter_by
    ) -> list[OilTradeResultModel]:
        """
        Получение списка результатов торгов за период.

        :param start_date: Начало периода.
        :param end_date: Конец периода.
        :param filter_by: Параметры для фильтрации запроса:
          oil_id, delivery_type_id, delivery_basis_id.
        :return: Список торгов.
        """

    @abstractmethod
    async def get_list(
        self,
        **filter_by,
    ) -> list[OilTradeResultModel]:
        """
        Список результатов последних торгов.

        :param filter_by: Параметры для фильтрации запроса:
          oil_id, delivery_type_id, delivery_basis_id.
        :return: Список торгов.
        """
