"""
Конфигурация приложения.
"""
import os

# Токен бота (в реальном проекте должен быть в переменных окружения)
BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")

# URL API для получения новостей
# NewsAPI - бесплатный план доступен, требует API ключ (можно использовать мок для тестирования)
NEWS_API_URL = os.getenv("NEWS_API_URL", "https://newsapi.org/v2/top-headlines")
NEWS_API_KEY = os.getenv("NEWS_API_KEY", "your_api_key_here")

