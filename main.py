import uvicorn
from fastapi import FastAPI

from app.api.endpoints.currency import currency_router
from app.api.endpoints.users import user_router
from app.api.exceptions.exceptions import set_exception_handlers

app = FastAPI()
set_exception_handlers(app)
app.include_router(user_router)
app.include_router(currency_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
