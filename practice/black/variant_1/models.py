from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class TaskCreate(BaseModel):
    """
    Модель для создания новой задачи (без ID, так как он генерируется на сервере)
    
    TODO: Реализовать модель согласно требованиям:
    - title - обязательное поле, строка от 1 до 200 символов
    - description - необязательное поле, строка или None
    - priority - обязательное поле, строка: "low", "medium" или "high"
    - completed - необязательное поле, булево значение, по умолчанию False
    """
    pass


class Task(TaskCreate):
    """
    Модель для чтения задачи (включает ID и дату создания)
    
    TODO: Наследовать от TaskCreate и добавить поля:
    - id - уникальный идентификатор задачи, целое число
    - created_at - дата и время создания задачи (datetime)
    """
    pass


class TaskUpdate(BaseModel):
    """
    Модель для обновления задачи (все поля необязательные)
    
    TODO: Реализовать модель согласно требованиям:
    - title - необязательное поле, строка от 1 до 200 символов или None
    - description - необязательное поле, строка или None
    - priority - необязательное поле, строка: "low", "medium" или "high", или None
    - completed - необязательное поле, булево значение или None
    """
    pass

