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
def sample_note_data():
    """Пример данных заметки для тестов"""
    return {
        "id": 1,
        "title": "Тестовая заметка",
        "content": "Содержание тестовой заметки",
        "tags": "тест, важное",
        "is_pinned": False
    }


@pytest.fixture
def sample_note_create():
    """Пример данных для создания заметки (без ID)"""
    return {
        "title": "Новая заметка",
        "content": "Содержание новой заметки",
        "tags": "новая, идеи",
        "is_pinned": True
    }
