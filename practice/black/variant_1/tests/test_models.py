"""
Тесты для models.py
Проверяют ОРы: 5.1 (Pydantic валидация)
"""
import pytest
from pydantic import ValidationError

try:
    from models import TaskCreate, Task, TaskUpdate
except ImportError:
    pytest.skip("models module not available", allow_module_level=True)


class TestOR51_PydanticValidation:
    """ОР 5.1: Использовать Pydantic для валидации данных"""
    
    def test_task_create_valid_data(self):
        """Проверка создания TaskCreate с валидными данными"""
        task = TaskCreate(
            title="Тестовая задача",
            description="Описание",
            priority="high",
            completed=False
        )
        assert task.title == "Тестовая задача"
        assert task.priority == "high"
        assert task.completed is False
    
    def test_task_create_minimal_data(self):
        """Проверка создания TaskCreate с минимальными данными"""
        task = TaskCreate(
            title="Задача",
            priority="low"
        )
        assert task.title == "Задача"
        assert task.description is None
        assert task.completed is False
    
    def test_task_create_validation_title_required(self):
        """Проверка валидации: title обязателен"""
        with pytest.raises(ValidationError):
            TaskCreate(priority="medium")
    
    def test_task_create_validation_priority_required(self):
        """Проверка валидации: priority обязателен"""
        with pytest.raises(ValidationError):
            TaskCreate(title="Задача")
    
    def test_task_inherits_from_task_create(self):
        """Проверка наследования Task от TaskCreate"""
        from datetime import datetime
        task = Task(
            id=1,
            title="Задача",
            priority="medium",
            created_at=datetime.now()
        )
        assert task.id == 1
        assert task.title == "Задача"
        assert task.created_at is not None
    
    def test_task_update_all_optional(self):
        """Проверка, что все поля TaskUpdate необязательны"""
        task_update = TaskUpdate()
        assert task_update.title is None
        assert task_update.priority is None
        assert task_update.completed is None

