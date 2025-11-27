from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime


class ArticleCreate(BaseModel):
    """
    Модель для создания новой статьи (без ID, так как он генерируется на сервере)
    
    TODO: Реализовать модель согласно требованиям:
    - title - обязательное поле, строка от 1 до 200 символов
    - content - обязательное поле, строка (содержание статьи)
    - author - обязательное поле, строка от 1 до 100 символов
    - category - обязательное поле, строка: "tech", "science", "business" или "other"
    - published - необязательное поле, булево значение, по умолчанию False
    """
    pass


class Article(ArticleCreate):
    """
    Модель для чтения статьи (включает ID и дату создания)
    
    TODO: Наследовать от ArticleCreate и добавить поля:
    - id - уникальный идентификатор статьи, целое число
    - created_at - дата и время создания статьи (datetime)
    """
    pass


class ArticleUpdate(BaseModel):
    """
    Модель для обновления статьи (все поля необязательные)
    
    TODO: Реализовать модель согласно требованиям:
    - title - необязательное поле, строка от 1 до 200 символов или None
    - content - необязательное поле, строка или None
    - author - необязательное поле, строка от 1 до 100 символов или None
    - category - необязательное поле, строка: "tech", "science", "business" или "other", или None
    - published - необязательное поле, булево значение или None
    """
    pass

