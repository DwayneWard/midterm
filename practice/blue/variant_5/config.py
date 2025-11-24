"""
Конфигурация приложения.
"""
import os

# Токен бота (в реальном проекте должен быть в переменных окружения)
BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")

# URL API для получения цитат
# quotable.io - бесплатный, не требует API ключа
QUOTES_API_URL = os.getenv("QUOTES_API_URL", "https://api.quotable.io/quotes/random")

