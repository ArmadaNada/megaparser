import google.generativeai as genai
from config import settings
import logging

logger = logging.getLogger(__name__)

# Инициализация Gemini
genai.configure(api_key=settings.gemini_api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

async def rewrite_post(text: str) -> str:
    if not text:
        return ""
    
    # Промпт можно будет подстроить под ваш стиль позже
    prompt = (
        "Ты профессиональный редактор. Перепиши этот текст для Telegram-канала используя черный юмор и шутки на грани фола, "
        "сделав его более интересным и сохранив все важные детали и эмодзи:\n\n"
        f"{text}"
    )
    
    try:
        response = await model.generate_content_async(prompt)
        return response.text
    except Exception as e:
        logger.error(f"Ошибка Gemini: {e}")
        return f"Ошибка рерайта: {str(e)}"
