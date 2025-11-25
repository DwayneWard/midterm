"""
Тесты для storage.py
Проверяют ОРы: 3.2 (работа с данными в памяти)
"""
import pytest

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
        """Проверка получения всех книг"""
        tasks = get_all_tasks()
        assert isinstance(tasks, list)
        assert len(tasks) > 0
    
    def test_get_task_by_id_exists(self):
        """Проверка получения книги по существующему ID"""
        # Создаем книгу для гарантии, что она существует
        new_task = TaskCreate(
            title="Тестовая книга для проверки",
            priority="Тестовый автор",
            completed=2024
        )
        created = create_task(new_task)
        task_id = created.id
        
        # Проверяем получение книги
        task = get_task_by_id(task_id)
        assert task is not None
        assert task.id == task_id
    
    def test_get_task_by_id_not_exists(self):
        """Проверка получения книги по несуществующему ID"""
        task = get_task_by_id(99999)
        assert task is None
    
    def test_create_task_adds_to_storage(self):
        """Проверка создания новой книги"""
        initial_count = len(get_all_tasks())
        new_task = TaskCreate(
            title="Новая тестовая книга",
            priority="Тестовый автор",
            completed=2024
        )
        created = create_task(new_task)
        assert created.id is not None
        assert created.title == "Новая тестовая книга"
        assert len(get_all_tasks()) == initial_count + 1
    
    def test_update_task_exists(self):
        """Проверка обновления существующей книги"""
        # Создаем книгу для обновления
        new_task = TaskCreate(
            title="Книга для обновления",
            priority="Автор",
            completed=2020
        )
        created = create_task(new_task)
        
        # Обновляем книгу
        updated_data = Task(
            id=created.id,
            title="Обновленное название",
            priority=created.priority,
            completed=created.completed,
            description=created.description
        )
        updated = update_task(created.id, updated_data)
        assert updated is not None
        assert updated.title == "Обновленное название"
    
    def test_update_task_not_exists(self):
        """Проверка обновления несуществующей книги"""
        updated_data = Task(
            id=99999,
            title="Тест",
            priority="Автор",
            completed=2000
        )
        result = update_task(99999, updated_data)
        assert result is None
    
    def test_delete_task_exists(self):
        """Проверка удаления существующей книги"""
        # Создаем книгу для удаления
        new_task = TaskCreate(
            title="Книга для удаления",
            priority="Автор",
            completed=2020
        )
        created = create_task(new_task)
        task_id = created.id
        
        # Удаляем книгу
        result = delete_task(task_id)
        assert result is True
        assert get_task_by_id(task_id) is None
    
    def test_delete_task_not_exists(self):
        """Проверка удаления несуществующей книги"""
        result = delete_task(99999)
        assert result is False

