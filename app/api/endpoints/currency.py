from fastapi import APIRouter, Depends, Query

from app.dependencies.dependencies import get_currency_service
from app.service.currency import CurrencyService

currency_router = APIRouter(prefix="/currency", tags=["currency"])


@currency_router.get("/list")
async def get_currency(service: CurrencyService = Depends(get_currency_service)):
    return await service.get_full_currency_data()


@currency_router.get("/exchange")
async def get_currency_exchange(
    from_code: str = Query(),
    to_code: str = Query(),
    value: float | int = Query(),
    service: CurrencyService = Depends(get_currency_service),
):
    return await service.currency_convert(from_code, to_code, value)
