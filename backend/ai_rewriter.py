from google import genai
from config import settings
import logging

logger = logging.getLogger(__name__)

# Инициализация нового клиента
client = genai.Client(api_key=settings.gemini_api_key)

async def rewrite_post(text: str) -> str:
    if not text:
        return ""
    
    try:
        # Используем ту самую модель, которая дала "Победу"
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=f"Ты профессиональный редактор любитель не политкорректного юмора и шуток "на грани фола". Перепиши пост для Telegram: {text}"
        )
        return response.text
    except Exception as e:
        logger.error(f"Ошибка рерайта: {e}")
        return f"Ошибка: {str(e)}"
