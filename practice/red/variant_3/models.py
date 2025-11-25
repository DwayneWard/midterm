from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class EventCreate(BaseModel):
    """
    Модель для создания нового события (без ID, так как он генерируется на сервере)
    
    TODO: Реализовать модель согласно требованиям:
    - title - обязательное поле, строка от 1 до 200 символов
    - description - необязательное поле, строка или None
    - event_date - обязательное поле, дата (date)
    - location - обязательное поле, строка от 1 до 100 символов
    - category - обязательное поле, строка: "work", "personal" или "other"
    """
    pass


class Event(EventCreate):
    """
    Модель для чтения события (включает ID)
    
    TODO: Наследовать от EventCreate и добавить поле:
    - id - уникальный идентификатор события, целое число
    """
    pass


class EventUpdate(BaseModel):
    """
    Модель для обновления события (все поля необязательные)
    
    TODO: Реализовать модель согласно требованиям:
    - title - необязательное поле, строка от 1 до 200 символов или None
    - description - необязательное поле, строка или None
    - event_date - необязательное поле, дата (date) или None
    - location - необязательное поле, строка от 1 до 100 символов или None
    - category - необязательное поле, строка: "work", "personal" или "other", или None
    """
    pass

