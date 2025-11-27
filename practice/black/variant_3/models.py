from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime


class OrderCreate(BaseModel):
    """
    Модель для создания нового заказа (без ID, так как он генерируется на сервере)
    
    TODO: Реализовать модель согласно требованиям:
    - customer_name - обязательное поле, строка от 1 до 200 символов
    - product_name - обязательное поле, строка от 1 до 200 символов
    - quantity - обязательное поле, положительное целое число
    - total_price - обязательное поле, положительное число (float)
    - status - обязательное поле, строка: "pending", "processing", "completed" или "cancelled"
    """
    pass


class Order(OrderCreate):
    """
    Модель для чтения заказа (включает ID и дату создания)
    
    TODO: Наследовать от OrderCreate и добавить поля:
    - id - уникальный идентификатор заказа, целое число
    - created_at - дата и время создания заказа (datetime)
    """
    pass


class OrderUpdate(BaseModel):
    """
    Модель для обновления заказа (все поля необязательные)
    
    TODO: Реализовать модель согласно требованиям:
    - customer_name - необязательное поле, строка от 1 до 200 символов или None
    - product_name - необязательное поле, строка от 1 до 200 символов или None
    - quantity - необязательное поле, положительное целое число или None
    - total_price - необязательное поле, положительное число (float) или None
    - status - необязательное поле, строка: "pending", "processing", "completed" или "cancelled", или None
    """
    pass

