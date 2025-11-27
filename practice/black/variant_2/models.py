from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime


class ProductCreate(BaseModel):
    """
    Модель для создания нового продукта (без ID, так как он генерируется на сервере)
    
    TODO: Реализовать модель согласно требованиям:
    - name - обязательное поле, строка от 1 до 200 символов
    - description - необязательное поле, строка или None
    - price - обязательное поле, положительное число (float)
    - category - обязательное поле, строка: "electronics", "clothing", "food" или "other"
    - stock - необязательное поле, целое число, по умолчанию 0
    """
    pass


class Product(ProductCreate):
    """
    Модель для чтения продукта (включает ID и дату создания)
    
    TODO: Наследовать от ProductCreate и добавить поля:
    - id - уникальный идентификатор продукта, целое число
    - created_at - дата и время создания продукта (datetime)
    """
    pass


class ProductUpdate(BaseModel):
    """
    Модель для обновления продукта (все поля необязательные)
    
    TODO: Реализовать модель согласно требованиям:
    - name - необязательное поле, строка от 1 до 200 символов или None
    - description - необязательное поле, строка или None
    - price - необязательное поле, положительное число (float) или None
    - category - необязательное поле, строка: "electronics", "clothing", "food" или "other", или None
    - stock - необязательное поле, целое число или None
    """
    pass
