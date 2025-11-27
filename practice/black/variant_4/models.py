from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime


class UserCreate(BaseModel):
    """
    Модель для создания нового пользователя (без ID, так как он генерируется на сервере)
    
    TODO: Реализовать модель согласно требованиям:
    - username - обязательное поле, строка от 1 до 100 символов
    - email - обязательное поле, строка (email адрес)
    - full_name - необязательное поле, строка или None
    - is_active - необязательное поле, булево значение, по умолчанию True
    - role - обязательное поле, строка: "user", "admin" или "moderator"
    """
    pass


class User(UserCreate):
    """
    Модель для чтения пользователя (включает ID и дату создания)
    
    TODO: Наследовать от UserCreate и добавить поля:
    - id - уникальный идентификатор пользователя, целое число
    - created_at - дата и время создания пользователя (datetime)
    """
    pass


class UserUpdate(BaseModel):
    """
    Модель для обновления пользователя (все поля необязательные)
    
    TODO: Реализовать модель согласно требованиям:
    - username - необязательное поле, строка от 1 до 100 символов или None
    - email - необязательное поле, строка (email адрес) или None
    - full_name - необязательное поле, строка или None
    - is_active - необязательное поле, булево значение или None
    - role - необязательное поле, строка: "user", "admin" или "moderator", или None
    """
    pass

