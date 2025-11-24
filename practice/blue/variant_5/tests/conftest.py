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
def sample_quote_data():
    """Пример данных о цитате из API."""
    return [{
        "_id": "5d91bacc5eb3c80001c8e4b3",
        "content": "The way to get started is to quit talking and begin doing.",
        "author": "Walt Disney",
        "tags": ["success", "inspirational"]
    }]

