from app.api.models.user import User
from app.core.exceptions import *
from app.core.security import create_token, crypt_context
from app.repositories.base_repository import AbstractRepo


class UserService:
    def __init__(self, repo: AbstractRepo):
        self.repo = repo

    async def add_user(self, user: User):
        result = await self.repo.get_data_by_key("username", user.username)

        if result:
            raise UserIsExistException

        user_load = user.model_dump(mode="json")

        user_load["password"] = crypt_context.hash(user.password)

        await self.repo.add_data(user_load)

    async def get_user(self, username: str):
        result = await self.repo.get_data_by_key("username", username)

        if not result:
            raise UserNotFoundException
        return result

    async def create_token(self, user: User):
        user_from_db = await self.get_user(user.username)

        if not user_from_db:
            raise UserNotFoundException

        if not crypt_context.verify(user.password, user_from_db["password"]):
            raise PasswordIncorrectException

        return create_token(user.username)
