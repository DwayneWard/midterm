"""
Конфигурация для тестов
"""
import pytest
from fastapi.testclient import TestClient
from fastapi import FastAPI
from unittest.mock import patch
from datetime import date

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
def sample_event_data():
    """Пример данных события для тестов"""
    return {
        "id": 1,
        "title": "Тестовое событие",
        "event_date": date(2024, 12, 1),
        "location": "Офис",
        "category": "work",
        "description": "Описание тестового события"
    }


@pytest.fixture
def sample_event_create():
    """Пример данных для создания события (без ID)"""
    return {
        "title": "Новое событие",
        "event_date": date(2024, 12, 5),
        "location": "Кафе",
        "category": "personal",
        "description": "Описание нового события"
    }
