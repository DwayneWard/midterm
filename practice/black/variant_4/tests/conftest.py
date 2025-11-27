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
def sample_user_data():
    """Пример данных пользователя для тестов"""
    from datetime import datetime
    return {
        "id": 1,
        "username": "testuser",
        "email": "test@example.com",
        "full_name": "Тестовый пользователь",
        "is_active": True,
        "role": "user",
        "created_at": datetime.now()
    }


@pytest.fixture
def sample_user_create():
    """Пример данных для создания пользователя (без ID)"""
    return {
        "username": "newuser",
        "email": "newuser@example.com",
        "full_name": "Новый пользователь",
        "is_active": True,
        "role": "user"
    }

