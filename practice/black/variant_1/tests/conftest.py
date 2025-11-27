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
def sample_task_data():
    """Пример данных задачи для тестов"""
    from datetime import datetime
    return {
        "id": 1,
        "title": "Тестовая задача",
        "description": "Описание тестовой задачи",
        "priority": "high",
        "completed": False,
        "created_at": datetime.now()
    }


@pytest.fixture
def sample_task_create():
    """Пример данных для создания задачи (без ID)"""
    return {
        "title": "Новая задача",
        "description": "Описание новой задачи",
        "priority": "medium",
        "completed": False
    }

