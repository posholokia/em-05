from starlette import status

from fastapi import APIRouter, Query, Depends

from api.schema import (
    TradeDateSchema,
    TradeFilterSchema,
    TradePeriodFilterSchema,
    TradeResultSchema,
)
from config.container import container
from interfaces.repository.trading import ITradingRepository


router = APIRouter()


@router.get(
    "/get_last_trading_dates",
    status_code=status.HTTP_200_OK,
    description="Получение списка дат последних торгов.",
)
async def get_last_trading_dates(
    limit: int = Query(default=100, ge=1)
) -> TradeDateSchema:
    repository = container.resolve(ITradingRepository)
    date_list = await repository.get_last_dates(limit)
    return TradeDateSchema(dates=date_list)



@router.get(
    "/get_dynamics",
    status_code=status.HTTP_200_OK,
    description="Получение результатов торгов за период.",
)
async def get_dynamics(
    filter_: TradePeriodFilterSchema = Depends(),
) -> list[TradeResultSchema]:
    repository = container.resolve(ITradingRepository)
    trade_results = await repository.get_list_for_period(
        **filter_.model_dump(exclude_defaults=True)
    )
    return [TradeResultSchema.model_validate(res) for res in trade_results]


@router.get(
    "/get_trading_results",
    status_code=status.HTTP_200_OK,
    description="Получение результатов торгов за период.",
)
async def get_trading_results(
    filter_: TradeFilterSchema = Depends(),
) -> list[TradeResultSchema]:
    repository = container.resolve(ITradingRepository)
    trade_results = await repository.get_list(
        **filter_.model_dump(exclude_defaults=True)
    )
    return [TradeResultSchema.model_validate(res) for res in trade_results]
