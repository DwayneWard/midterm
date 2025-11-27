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
def sample_product_data():
    """Пример данных продукта для тестов"""
    from datetime import datetime
    return {
        "id": 1,
        "name": "Тестовый продукт",
        "description": "Описание тестового продукта",
        "price": 999.99,
        "category": "electronics",
        "stock": 10,
        "created_at": datetime.now()
    }


@pytest.fixture
def sample_product_create():
    """Пример данных для создания продукта (без ID)"""
    return {
        "name": "Новый продукт",
        "description": "Описание нового продукта",
        "price": 1999.99,
        "category": "clothing",
        "stock": 5
    }
