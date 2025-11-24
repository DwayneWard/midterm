import pytest
import sys
from pathlib import Path

# Добавляем корневую директорию проекта в путь
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Импорты для моков
from unittest.mock import Mock, patch, MagicMock


@pytest.fixture
def mock_requests():
    """Фикстура для мокирования requests."""
    with patch('api_client.requests') as mock:
        yield mock


@pytest.fixture
def sample_exchange_data():
    """Пример данных о курсах валют из API."""
    return {
        "base": "USD",
        "date": "2024-01-15",
        "rates": {
            "EUR": 0.92,
            "RUB": 90.5,
            "GBP": 0.79,
            "JPY": 149.2
        }
    }

