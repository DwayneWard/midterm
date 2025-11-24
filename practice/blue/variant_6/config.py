"""
Конфигурация приложения.
"""
import os

# Токен бота (в реальном проекте должен быть в переменных окружения)
BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")

# URL API для получения рецептов
# TheMealDB - бесплатный, не требует API ключа
RECIPES_API_URL = os.getenv("RECIPES_API_URL", "https://www.themealdb.com/api/json/v1/1/search.php")

