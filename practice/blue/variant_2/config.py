"""
Конфигурация приложения.
"""
import os

# Токен бота (в реальном проекте должен быть в переменных окружения)
BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")

# URL API для получения курсов валют
# exchangerate-api.io - бесплатный, не требует API ключа для базовых запросов
EXCHANGE_API_URL = os.getenv("EXCHANGE_API_URL", "https://api.exchangerate-api.com/v4/latest")

