from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from app.core.exceptions import *


def set_exception_handlers(app: FastAPI):
    @app.exception_handler(UserNotFoundException)
    async def user_not_found(request: Request, exc: Exception) -> JSONResponse:
        return JSONResponse(status_code=404, content={"messege": "User not found"})

    @app.exception_handler(UserIsExistException)
    async def user_found(request: Request, exc: Exception) -> JSONResponse:
        return JSONResponse(status_code=400, content={"messege": "User is exist"})

    @app.exception_handler(PasswordIncorrectException)
    async def invalid_password(request: Request, exc: Exception) -> JSONResponse:
        return JSONResponse(status_code=403, content={"messege": "Invalid password"})

    @app.exception_handler(InvalidCurrencyCode)
    async def invalid_code(request: Request, exc: Exception) -> JSONResponse:
        return JSONResponse(status_code=400, content={"messege": "Currency code not found"})
