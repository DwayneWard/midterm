from typing import List, Optional
from datetime import datetime
from models import Order, OrderCreate, OrderUpdate


# Хранилище заказов в памяти
orders_db: List[Order] = [
    Order(id=1, customer_name="Иван Иванов", product_name="Ноутбук", quantity=1, total_price=99999.99, status="pending", created_at=datetime.now()),
    Order(id=2, customer_name="Мария Петрова", product_name="Смартфон", quantity=2, total_price=59999.98, status="processing", created_at=datetime.now()),
    Order(id=3, customer_name="Петр Сидоров", product_name="Планшет", quantity=1, total_price=29999.99, status="completed", created_at=datetime.now()),
]


def get_all_orders() -> List[Order]:
    """
    Получить все заказы
    
    Returns:
        Список всех заказов
    """
    return orders_db


def get_order_by_id(order_id: int) -> Optional[Order]:
    """
    Получить заказ по ID
    
    Args:
        order_id: ID заказа
        
    Returns:
        Заказ или None, если заказ не найден
        
    TODO: Реализовать функцию:
    1. Пройтись по списку orders_db
    2. Найти заказ с указанным id
    3. Вернуть заказ или None, если не найден
    """
    pass


def create_order(order_data: OrderCreate) -> Order:
    """
    Создать новый заказ
    
    Args:
        order_data: Данные нового заказа (без id и created_at)
        
    Returns:
        Созданный заказ с присвоенным id и created_at
        
    TODO: Реализовать функцию:
    1. Определить новый id (максимальный id в orders_db + 1, или 1 если список пуст)
    2. Создать объект Order с новым id, created_at=datetime.now() и данными из order_data
    3. Добавить заказ в orders_db
    4. Вернуть созданный заказ
    """
    pass


def update_order(order_id: int, order_data: OrderUpdate) -> Optional[Order]:
    """
    Обновить заказ
    
    Args:
        order_id: ID заказа для обновления
        order_data: Новые данные заказа
        
    Returns:
        Обновленный заказ или None, если заказ не найден
        
    TODO: Реализовать функцию:
    1. Найти заказ с указанным id в orders_db
    2. Если заказ не найден, вернуть None
    3. Обновить поля заказа данными из order_data (только те поля, которые не None)
       Используй: order.field = order_data.field if order_data.field is not None else order.field
    4. Вернуть обновленный заказ
    """
    pass


def delete_order(order_id: int) -> bool:
    """
    Удалить заказ
    
    Args:
        order_id: ID заказа для удаления
        
    Returns:
        True, если заказ удален, False если не найден
        
    TODO: Реализовать функцию:
    1. Найти заказ с указанным id в orders_db
    2. Если заказ не найден, вернуть False
    3. Удалить заказ из orders_db
    4. Вернуть True
    """
    pass

