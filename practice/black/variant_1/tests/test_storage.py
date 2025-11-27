"""
Тесты для storage.py
Проверяют ОРы: 3.2 (работа с данными в памяти)
"""
import pytest
from datetime import datetime

try:
    from storage import (
        get_all_tasks,
        get_task_by_id,
        create_task,
        update_task,
        delete_task
    )
    from models import Task, TaskCreate
except ImportError:
    pytest.skip("storage module not available", allow_module_level=True)


class TestOR32_DataStorage:
    """ОР 3.2: Работать с данными в памяти"""
    
    def test_get_all_tasks_returns_list(self):
        """Проверка получения всех задач"""
        tasks = get_all_tasks()
        assert isinstance(tasks, list)
        assert len(tasks) > 0
    
    def test_get_task_by_id_exists(self):
        """Проверка получения задачи по существующему ID"""
        # Создаем задачу для гарантии, что она существует
        new_task = TaskCreate(
            title="Тестовая задача для проверки",
            priority="medium"
        )
        created = create_task(new_task)
        task_id = created.id
        
        # Проверяем получение задачи
        task = get_task_by_id(task_id)
        assert task is not None
        assert task.id == task_id
    
    def test_get_task_by_id_not_exists(self):
        """Проверка получения задачи по несуществующему ID"""
        task = get_task_by_id(99999)
        assert task is None
    
    def test_create_task_adds_to_storage(self):
        """Проверка создания новой задачи"""
        initial_count = len(get_all_tasks())
        new_task = TaskCreate(
            title="Новая тестовая задача",
            priority="high"
        )
        created = create_task(new_task)
        assert created.id is not None
        assert created.created_at is not None
        assert len(get_all_tasks()) == initial_count + 1
    
    def test_update_task_exists(self):
        """Проверка обновления существующей задачи"""
        # Создаем задачу для обновления
        new_task = TaskCreate(
            title="Задача для обновления",
            priority="low"
        )
        created = create_task(new_task)
        
        # Обновляем задачу
        from models import TaskUpdate
        updated_data = TaskUpdate(title="Обновленное название")
        updated = update_task(created.id, updated_data)
        assert updated is not None
        assert updated.title == "Обновленное название"
    
    def test_delete_task_exists(self):
        """Проверка удаления существующей задачи"""
        # Создаем задачу для удаления
        new_task = TaskCreate(
            title="Задача для удаления",
            priority="medium"
        )
        created = create_task(new_task)
        task_id = created.id
        
        # Удаляем задачу
        result = delete_task(task_id)
        assert result is True
        assert get_task_by_id(task_id) is None

