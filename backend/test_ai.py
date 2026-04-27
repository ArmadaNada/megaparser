import asyncio
from ai_rewriter import rewrite_post
import os
from dotenv import load_dotenv

# Загружаем ключи из .env
load_dotenv()

async def test():
    test_text = "Виноделие в Абрау-Дюрсо выходит на новый уровень. Эксперты отмечают рост качества игристых вин."
    print("--- Отправляем текст на рерайт в Gemini ---")
    result = await rewrite_post(test_text)
    print(f"Результат:\n{result}")

if __name__ == "__main__":
    asyncio.run(test())
