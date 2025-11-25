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
def sample_task_data():
    """Пример данных задачи для тестов"""
    return {
        "id": 1,
        "title": "Тестовая задача",
        "priority": "high",
        "completed": False,
        "description": "Описание тестовой задачи"
    }


@pytest.fixture
def sample_task_create():
    """Пример данных для создания задачи (без ID)"""
    return {
        "title": "Новая задача",
        "priority": "medium",
        "completed": False,
        "description": "Описание новой задачи"
    }
