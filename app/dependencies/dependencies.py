from fastapi import Depends

from app.core.security import get_user_from_token
from app.repositories.base_repository import AbstractRepo
from app.repositories.users_repository import UserRepo
from app.service.currency import CurrencyService
from app.service.users import UserService
from app.uow.uow import UnitOfWork


def get_user_service(repo: AbstractRepo = Depends(UserRepo)):
    return UserService(repo)


async def get_currency_service(
    username: str = Depends(get_user_from_token), user_service: UserService = Depends(get_user_service)
):
    user = await user_service.get_user(username)
    return CurrencyService(UnitOfWork())
