from redis import asyncio as aioredis

from interfaces.cache.storage import ICacheStorage


class RedisStorage(ICacheStorage):
    def __init__(
        self,
        host: str,
        port: int,
        db: int,
        username: str,
        password: str,
    ) -> None:
        self._redis_instance = aioredis.Redis(
            host=host,
            port=port,
            db=db,
            password=password,
            username=username,
        )

    async def connect(self) -> aioredis.Redis:
        return self._redis_instance

    async def set_exp_value(
        self,
        key: str,
        value: str | int | bytes,
        timestamp_ex: int
    ) -> None:
        conn = await self.connect()
        await conn.set(
            name=key,
            value=value,
            exat=timestamp_ex,
        )

    async def get_value(self, key: str) -> str | None:
        redis = await self.connect()
        value: bytes = await redis.get(key)

        if value is None:
            return value

        return value.decode()