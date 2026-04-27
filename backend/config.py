from functools import lru_cache
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    telegram_api_id: int
    telegram_api_hash: str
    telegram_bot_token: str
    gemini_api_key: str  # Добавляем этот обязательный параметр
    openai_api_key: Optional[str] = None  # Теперь он не обязателен
    database_url: str
    allowed_user_id: int
    allowed_origins: str = "http://localhost:5173"

    model_config = {"env_file": ".env"}


@lru_cache
def get_settings() -> Settings:
    return Settings()

# Добавим эту строчку, чтобы в других файлах было проще обращаться к настройкам
settings = get_settings()
