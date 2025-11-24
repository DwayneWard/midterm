"""
Конфигурация приложения.
"""
import os

# Токен бота (в реальном проекте должен быть в переменных окружения)
BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")

# URL API для получения информации о странах
# REST Countries API - бесплатный, не требует API ключа
COUNTRIES_API_URL = os.getenv("COUNTRIES_API_URL", "https://restcountries.com/v3.1/name")

