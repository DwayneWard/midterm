"""
Конфигурация приложения.
"""
import os

# Токен бота 
BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")

# URL API для получения задач
# Для упрощения используем простой REST API
TODOS_API_URL = os.getenv("TODOS_API_URL", "https://jsonplaceholder.typicode.com/todos")

