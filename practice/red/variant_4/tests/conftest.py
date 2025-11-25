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
def sample_product_data():
    """Пример данных продукта для тестов"""
    return {
        "id": 1,
        "name": "Тестовый продукт",
        "price": 999.99,
        "category": "electronics",
        "stock": 10,
        "description": "Описание тестового продукта"
    }


@pytest.fixture
def sample_product_create():
    """Пример данных для создания продукта (без ID)"""
    return {
        "name": "Новый продукт",
        "price": 199.99,
        "category": "clothing",
        "stock": 5,
        "description": "Описание нового продукта"
    }
