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
def sample_country_data():
    """Пример данных о стране из API."""
    return {
        "name": {"common": "Russia", "official": "Russian Federation"},
        "capital": ["Moscow"],
        "population": 144104080,
        "currencies": {"RUB": {"name": "Russian ruble", "symbol": "₽"}},
        "languages": {"rus": "Russian"},
        "region": "Europe"
    }


@pytest.fixture
def sample_country_api_response(sample_country_data):
    """Пример ответа API (массив стран)."""
    return [sample_country_data]

