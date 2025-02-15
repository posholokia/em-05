from contextlib import asynccontextmanager
from dataclasses import dataclass
from typing import AsyncIterator

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    AsyncSession,
    create_async_engine,
)


class DatabaseConnection:
    """
    Объект подключения к базе данных.
    """
    def __init__(self, url: str):
        """
        :param url: Uri для подключения к БД.
        """
        db_engine = create_async_engine(
            url,
            pool_size=20,
            max_overflow=10,
            pool_pre_ping=False,
            isolation_level="AUTOCOMMIT",
        )

        self.__session = async_sessionmaker(
            bind=db_engine,
            expire_on_commit=False,
            class_=AsyncSession,
        )

    def get_session(self):
        return self.__session


@dataclass
class Database:
    """
    Абстракция над подключением базы данных,
    управляет сессиями и транзакциями.
    """
    __connection: DatabaseConnection

    @asynccontextmanager
    async def get_session(self) -> AsyncIterator[AsyncSession]:
        session = self.__connection.get_session()()
        try:
            yield session
        except SQLAlchemyError as e:
            await session.rollback()
            raise e
        finally:
            await session.commit()
            await session.close()
