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
def sample_event_data():
    """Пример данных события для тестов"""
    from datetime import datetime, date
    return {
        "id": 1,
        "title": "Тестовое событие",
        "description": "Описание тестового события",
        "event_date": date(2024, 12, 15),
        "location": "Москва",
        "category": "conference",
        "created_at": datetime.now()
    }


@pytest.fixture
def sample_event_create():
    """Пример данных для создания события (без ID)"""
    from datetime import date
    return {
        "title": "Новое событие",
        "description": "Описание нового события",
        "event_date": date(2024, 12, 20),
        "location": "Санкт-Петербург",
        "category": "workshop"
    }

