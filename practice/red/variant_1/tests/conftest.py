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
def sample_book_data():
    """Пример данных книги для тестов"""
    return {
        "id": 1,
        "title": "Тестовая книга",
        "author": "Тестовый автор",
        "year": 2024,
        "description": "Описание тестовой книги"
    }


@pytest.fixture
def sample_book_create():
    """Пример данных для создания книги (без ID)"""
    return {
        "title": "Новая книга",
        "author": "Новый автор",
        "year": 2024,
        "description": "Описание новой книги"
    }

