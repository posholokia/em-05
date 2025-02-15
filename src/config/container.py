from functools import lru_cache
from punq import Container, Scope

from config import settings
from infrastructure.cache.redis_ import RedisStorage
from infrastructure.database.connection import DatabaseConnection, Database
from infrastructure.database.models.models import OilTradeResultModel
from infrastructure.repository.sqla import TradingRepository
from interfaces.cache.storage import ICacheStorage
from interfaces.repository.trading import ITradingRepository


@lru_cache(1)
def get_container() -> Container:
    return DiContainer().initialize_container()


class DiContainer:
    def __init__(self):
        self.container = Container()

    def initialize_container(self) -> Container:
        self.container.register(
            service=DatabaseConnection,
            factory=DatabaseConnection,
            scope=Scope.singleton,
            url=settings.DATABASE_URL,
        )
        self.container.register(
            service=Database,
            factory=Database,
            scope=Scope.transient
        )
        self.container.register(
            service=ITradingRepository,
            factory=TradingRepository,
            db=self.container.resolve(Database),
            model=OilTradeResultModel
        )
        self.container.register(
            ICacheStorage,
            RedisStorage,
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            db=settings.REDIS_DB,
            username=settings.REDIS_USER,
            password=settings.REDIS_PASS,
        )
        return self.container
