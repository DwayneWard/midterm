from typing import List, Optional
from datetime import datetime
from models import Product, ProductCreate, ProductUpdate


# Хранилище продуктов в памяти
products_db: List[Product] = [
    Product(id=1, name="Ноутбук", description="Игровой ноутбук", price=99999.99, category="electronics", stock=5, created_at=datetime.now()),
    Product(id=2, name="Футболка", description="Хлопковая футболка", price=1999.99, category="clothing", stock=20, created_at=datetime.now()),
    Product(id=3, name="Яблоки", description="Свежие яблоки", price=149.99, category="food", stock=100, created_at=datetime.now()),
]


def get_all_products() -> List[Product]:
    """
    Получить все продукты
    
    Returns:
        Список всех продуктов
    """
    return products_db


def get_product_by_id(product_id: int) -> Optional[Product]:
    """
    Получить продукт по ID
    
    Args:
        product_id: ID продукта
        
    Returns:
        Продукт или None, если продукт не найден
        
    TODO: Реализовать функцию:
    1. Пройтись по списку products_db
    2. Найти продукт с указанным id
    3. Вернуть продукт или None, если не найден
    """
    pass


def create_product(product_data: ProductCreate) -> Product:
    """
    Создать новый продукт
    
    Args:
        product_data: Данные нового продукта (без id и created_at)
        
    Returns:
        Созданный продукт с присвоенным id и created_at
        
    TODO: Реализовать функцию:
    1. Определить новый id (максимальный id в products_db + 1, или 1 если список пуст)
    2. Создать объект Product с новым id, created_at=datetime.now() и данными из product_data
    3. Добавить продукт в products_db
    4. Вернуть созданный продукт
    """
    pass


def update_product(product_id: int, product_data: ProductUpdate) -> Optional[Product]:
    """
    Обновить продукт
    
    Args:
        product_id: ID продукта для обновления
        product_data: Новые данные продукта
        
    Returns:
        Обновленный продукт или None, если продукт не найден
        
    TODO: Реализовать функцию:
    1. Найти продукт с указанным id в products_db
    2. Если продукт не найден, вернуть None
    3. Обновить поля продукта данными из product_data (только те поля, которые не None)
       Используй: product.field = product_data.field if product_data.field is not None else product.field
    4. Вернуть обновленный продукт
    """
    pass


def delete_product(product_id: int) -> bool:
    """
    Удалить продукт
    
    Args:
        product_id: ID продукта для удаления
        
    Returns:
        True, если продукт удален, False если не найден
        
    TODO: Реализовать функцию:
    1. Найти продукт с указанным id в products_db
    2. Если продукт не найден, вернуть False
    3. Удалить продукт из products_db
    4. Вернуть True
    """
    pass
