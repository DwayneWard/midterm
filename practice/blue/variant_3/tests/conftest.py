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
def sample_news_data():
    """Пример данных о новостях из API."""
    return {
        "status": "ok",
        "totalResults": 3,
        "articles": [
            {
                "title": "Test News 1",
                "description": "Description 1",
                "url": "https://example.com/news1",
                "publishedAt": "2024-01-15T10:00:00Z"
            },
            {
                "title": "Test News 2",
                "description": "Description 2",
                "url": "https://example.com/news2",
                "publishedAt": "2024-01-15T11:00:00Z"
            }
        ]
    }

