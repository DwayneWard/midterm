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
def sample_recipe_data():
    """Пример данных о рецепте из API."""
    return {
        "meals": [{
            "idMeal": "52771",
            "strMeal": "Spaghetti Carbonara",
            "strCategory": "Pasta",
            "strArea": "Italian",
            "strInstructions": "Инструкции по приготовлению...",
            "strIngredient1": "Spaghetti",
            "strMeasure1": "400g"
        }]
    }

