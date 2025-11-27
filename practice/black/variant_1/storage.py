from typing import List, Optional
from datetime import datetime
from models import Task, TaskCreate, TaskUpdate


# Хранилище задач в памяти
tasks_db: List[Task] = [
    Task(id=1, title="Изучить FastAPI", description="Изучить основы FastAPI", priority="high", completed=False, created_at=datetime.now()),
    Task(id=2, title="Настроить Redis", description="Установить и настроить Redis", priority="medium", completed=False, created_at=datetime.now()),
    Task(id=3, title="Написать тесты", description="Написать unit-тесты для проекта", priority="low", completed=True, created_at=datetime.now()),
]


def get_all_tasks() -> List[Task]:
    """
    Получить все задачи
    
    Returns:
        Список всех задач
    """
    return tasks_db


def get_task_by_id(task_id: int) -> Optional[Task]:
    """
    Получить задачу по ID
    
    Args:
        task_id: ID задачи
        
    Returns:
        Задача или None, если задача не найдена
        
    TODO: Реализовать функцию:
    1. Пройтись по списку tasks_db
    2. Найти задачу с указанным id
    3. Вернуть задачу или None, если не найдена
    """
    pass


def create_task(task_data: TaskCreate) -> Task:
    """
    Создать новую задачу
    
    Args:
        task_data: Данные новой задачи (без id и created_at)
        
    Returns:
        Созданная задача с присвоенным id и created_at
        
    TODO: Реализовать функцию:
    1. Определить новый id (максимальный id в tasks_db + 1, или 1 если список пуст)
    2. Создать объект Task с новым id, created_at=datetime.now() и данными из task_data
    3. Добавить задачу в tasks_db
    4. Вернуть созданную задачу
    """
    pass


def update_task(task_id: int, task_data: TaskUpdate) -> Optional[Task]:
    """
    Обновить задачу
    
    Args:
        task_id: ID задачи для обновления
        task_data: Новые данные задачи
        
    Returns:
        Обновленная задача или None, если задача не найдена
        
    TODO: Реализовать функцию:
    1. Найти задачу с указанным id в tasks_db
    2. Если задача не найдена, вернуть None
    3. Обновить поля задачи данными из task_data (только те поля, которые не None)
       Используй: task.field = task_data.field if task_data.field is not None else task.field
    4. Вернуть обновленную задачу
    """
    pass


def delete_task(task_id: int) -> bool:
    """
    Удалить задачу
    
    Args:
        task_id: ID задачи для удаления
        
    Returns:
        True, если задача удалена, False если не найдена
        
    TODO: Реализовать функцию:
    1. Найти задачу с указанным id в tasks_db
    2. Если задача не найдена, вернуть False
    3. Удалить задачу из tasks_db
    4. Вернуть True
    """
    pass

