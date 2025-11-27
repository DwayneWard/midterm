"""
Конфигурация для тестов
"""
import pytest
from fastapi.testclient import TestClient
from fastapi import FastAPI
from unittest.mock import AsyncMock, MagicMock, patch
import fakeredis.aioredis as aioredis

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
def mock_redis():
    """Мок Redis клиента для тестов"""
    return AsyncMock()


@pytest.fixture
def sample_article_data():
    """Пример данных статьи для тестов"""
    from datetime import datetime
    return {
        "id": 1,
        "title": "Тестовая статья",
        "content": "Содержание тестовой статьи",
        "author": "Иван Иванов",
        "category": "tech",
        "published": True,
        "created_at": datetime.now()
    }


@pytest.fixture
def sample_article_create():
    """Пример данных для создания статьи (без ID)"""
    return {
        "title": "Новая статья",
        "content": "Содержание новой статьи",
        "author": "Петр Петров",
        "category": "science",
        "published": False
    }

