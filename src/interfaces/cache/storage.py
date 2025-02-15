from abc import ABC, abstractmethod
from typing import Any


class ICacheStorage(ABC):
    @abstractmethod
    async def connect(self) -> Any:
        """
        Устанавливает соединение с кеш хранилищем
        и возвращает экземпляр соединения.
        """

    @abstractmethod
    async def set_exp_value(
        self,
        key: str,
        value: str | int | bytes,
        timestamp_ex: int,
    ) -> None:
        """
        Сохранить ключ - значение в кеш. Метод сохраняет данные только
        на фиксированный срок.

        :param key: Ключ.
        :param value: Значение ключа.
        :param timestamp_ex: Временная метка, в секундах, когда должен
          истечь срок хранения.
        """

    @abstractmethod
    async def get_value(self, key: str) -> str | None:
        """
        Получить значение из кеша.

        :param key: Ключ.
        :return: Значение ключа из кэша. Если ключ не был найден, то None.
        """
