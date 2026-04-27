import os
import google.generativeai as genai
from dotenv import load_dotenv

# Загружаем ключи
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

def test():
    if not api_key:
        print("Ошибка: Ключ GEMINI_API_KEY не найден в .env")
        return

    # Настраиваем конфигурацию
    genai.configure(api_key=api_key)
    
    # В 2026 году используем либо стабильный alias, либо 2.0
    # Попробуем сначала gemini-1.5-flash-latest
    try:
        print("--- Пробуем подключиться к Gemini ---")
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        response = model.generate_content("Напиши: Двигатель запущен!")
        print(f"УСПЕХ: {response.text}")
    except Exception as e:
        print(f"Ошибка 1.5-flash: {e}")
        
        # Если не вышло, пробуем версию 2.0
        print("--- Пробуем версию 2.0 ---")
        try:
            model = genai.GenerativeModel('gemini-2.0-flash')
            response = model.generate_content("Напиши: Двигатель 2.0 запущен!")
            print(f"УСПЕХ 2.0: {response.text}")
        except Exception as e2:
            print(f"Финальная ошибка: {e2}")

if __name__ == "__main__":
    test()
