import json
from datetime import datetime, UTC, timedelta, time
from fastapi.requests import Request
from fastapi.responses import Response

from config.container import get_container
from interfaces.cache.storage import ICacheStorage


async def cache_response_middleware(request: Request, call_next):
    container = get_container()
    cache: ICacheStorage = container.resolve(ICacheStorage)
    cache_key = str(request.url)
    cached_response = await cache.get_value(cache_key)

    if cached_response:
        response_dict = json.loads(cached_response)
    else:
        response = await call_next(request)
        body = b"".join([part async for part in response.body_iterator]).decode()
        headers = dict(response.headers)
        response_dict = {
            "body": body,
            "status": response.status_code,
            "headers": headers,
        }

        dumped_response = json.dumps(response_dict)
        timestamp_ex = _calculate_timestamp(time(hour=14, minute=11, tzinfo=UTC))
        await cache.set_exp_value(cache_key, dumped_response, timestamp_ex)

    return Response(
            content=response_dict["body"],
            status_code=response_dict["status"],
            headers=response_dict["headers"]
        )


def _calculate_timestamp(time_point) -> int:
    now_datetime = datetime.now(UTC)
    if now_datetime.timetz() > time_point:
        timestamp_date = now_datetime.date() + timedelta(days=1)
    else:
        timestamp_date=now_datetime.date()

    cache_clear_datetime = datetime(
        year=timestamp_date.year,
        month=timestamp_date.month,
        day=timestamp_date.day,
        hour=time_point.hour,
        minute=time_point.minute,
        tzinfo=UTC,
    )
    cache_clear_timestamp = cache_clear_datetime.timestamp()
    return round(cache_clear_timestamp)
