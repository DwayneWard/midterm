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
def sample_order_data():
    """Пример данных заказа для тестов"""
    from datetime import datetime
    return {
        "id": 1,
        "customer_name": "Иван Иванов",
        "product_name": "Тестовый продукт",
        "quantity": 2,
        "total_price": 1999.98,
        "status": "pending",
        "created_at": datetime.now()
    }


@pytest.fixture
def sample_order_create():
    """Пример данных для создания заказа (без ID)"""
    return {
        "customer_name": "Петр Петров",
        "product_name": "Новый продукт",
        "quantity": 1,
        "total_price": 999.99,
        "status": "pending"
    }

