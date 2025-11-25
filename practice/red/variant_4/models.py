from pydantic import BaseModel, Field
from typing import Optional


class ProductCreate(BaseModel):
    """
    Модель для создания нового продукта (без ID, так как он генерируется на сервере)
    
    TODO: Реализовать модель согласно требованиям:
    - name - обязательное поле, строка от 1 до 200 символов
    - description - необязательное поле, строка или None
    - price - обязательное поле, число с плавающей точкой, больше 0
    - category - обязательное поле, строка: "electronics", "clothing", "food" или "other"
    - stock - обязательное поле, целое число, больше или равно 0
    """
    pass


class Product(ProductCreate):
    """
    Модель для чтения продукта (включает ID)
    
    TODO: Наследовать от ProductCreate и добавить поле:
    - id - уникальный идентификатор продукта, целое число
    """
    pass


class ProductUpdate(BaseModel):
    """
    Модель для обновления продукта (все поля необязательные)
    
    TODO: Реализовать модель согласно требованиям:
    - name - необязательное поле, строка от 1 до 200 символов или None
    - description - необязательное поле, строка или None
    - price - необязательное поле, число с плавающей точкой, больше 0, или None
    - category - необязательное поле, строка: "electronics", "clothing", "food" или "other", или None
    - stock - необязательное поле, целое число, больше или равно 0, или None
    """
    pass

