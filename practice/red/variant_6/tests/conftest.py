"""
Конфигурация для тестов
"""
import pytest
from fastapi.testclient import TestClient
from fastapi import FastAPI
from unittest.mock import patch

# Импортируем приложение
try:
    from main import app
except ImportError:
    # Если модуль не импортируется, создаем заглушку
    app = FastAPI()


@pytest.fixture
def client():
    """Тестовый клиент FastAPI"""
    return TestClient(app)


@pytest.fixture
def sample_recipe_data():
    """Пример данных рецепта для тестов"""
    return {
        "id": 1,
        "name": "Тестовый рецепт",
        "ingredients": "Ингредиент1, Ингредиент2",
        "cooking_time": 60,
        "difficulty": "medium",
        "description": "Описание тестового рецепта"
    }


@pytest.fixture
def sample_recipe_create():
    """Пример данных для создания рецепта (без ID)"""
    return {
        "name": "Новый рецепт",
        "ingredients": "Ингредиенты",
        "cooking_time": 45,
        "difficulty": "easy",
        "description": "Описание нового рецепта"
    }
