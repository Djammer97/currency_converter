from dataclasses import dataclass

from environs import Env


@dataclass
class Settings:
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    all_currency_http_address: str


env = Env()
env.read_env()

settings = Settings(
    secret_key=env("SECRET_KEY"),
    algorithm=env("ALGORITHM"),
    access_token_expire_minutes=env.int("access_token_expire_minutes"),
    all_currency_http_address=env("ALL_CURRENCY_HTTP_ADDRESS"),
)
