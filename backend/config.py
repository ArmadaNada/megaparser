from functools import lru_cache
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    telegram_api_id: int
    telegram_api_hash: str
    telegram_bot_token: str
    gemini_api_key: str
    database_url: str
    allowed_user_id: int
    allowed_origins: str = "*"

    model_config = {"env_file": ".env"}

@lru_cache
def get_settings() -> Settings:
    return Settings()

settings = get_settings()
