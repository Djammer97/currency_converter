from datetime import datetime, timedelta, timezone

import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

from app.core.config import settings

OAuth2 = OAuth2PasswordBearer(tokenUrl="auth/login")

crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_token(user: str) -> str:
    data = {"sub": user}

    expire_time = datetime.now(timezone.utc) + timedelta(minutes=settings.access_token_expire_minutes)

    data["exp"] = expire_time

    return jwt.encode(payload=data, key=settings.secret_key, algorithm=settings.algorithm)


async def get_user_from_token(token: str = Depends(OAuth2)):
    try:
        user = jwt.decode(token, key=settings.secret_key, algorithms=[settings.algorithm])
        return user["sub"]
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=403, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=403, detail="Invalid token")
