from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from app.api.models.user import User
from app.dependencies.dependencies import get_user_service
from app.service.users import UserService

user_router = APIRouter(prefix="/auth", tags=["users"])


@user_router.post("/register")
async def post_register(user: User, service: UserService = Depends(get_user_service)) -> JSONResponse:
    await service.add_user(user)

    return JSONResponse(content={"messege": f"{user.username} is created"}, status_code=200)


@user_router.post("/login")
async def post_login(user: User, service: UserService = Depends(get_user_service)) -> JSONResponse:
    return JSONResponse(content={"token": await service.create_token(user)}, status_code=200)
