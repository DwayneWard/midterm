"""
Тесты для storage.py
Проверяют ОРы: 3.2 (работа с данными в памяти)
"""
import pytest
from datetime import datetime

try:
    from storage import (
        get_all_orders,
        get_order_by_id,
        create_order,
        update_order,
        delete_order
    )
    from models import Order, OrderCreate
except ImportError:
    pytest.skip("storage module not available", allow_module_level=True)


class TestOR32_DataStorage:
    """ОР 3.2: Работать с данными в памяти"""
    
    def test_get_all_orders_returns_list(self):
        """Проверка получения всех заказов"""
        orders = get_all_orders()
        assert isinstance(orders, list)
        assert len(orders) > 0
    
    def test_get_order_by_id_exists(self):
        """Проверка получения заказа по существующему ID"""
        # Создаем заказ для гарантии, что он существует
        new_order = OrderCreate(
            customer_name="Тестовый клиент",
            product_name="Тестовый продукт",
            quantity=1,
            total_price=999.99,
            status="pending"
        )
        created = create_order(new_order)
        order_id = created.id
        
        # Проверяем получение заказа
        order = get_order_by_id(order_id)
        assert order is not None
        assert order.id == order_id
    
    def test_get_order_by_id_not_exists(self):
        """Проверка получения заказа по несуществующему ID"""
        order = get_order_by_id(99999)
        assert order is None
    
    def test_create_order_adds_to_storage(self):
        """Проверка создания нового заказа"""
        initial_count = len(get_all_orders())
        new_order = OrderCreate(
            customer_name="Новый клиент",
            product_name="Новый продукт",
            quantity=2,
            total_price=1999.98,
            status="processing"
        )
        created = create_order(new_order)
        assert created.id is not None
        assert created.created_at is not None
        assert len(get_all_orders()) == initial_count + 1
    
    def test_update_order_exists(self):
        """Проверка обновления существующего заказа"""
        # Создаем заказ для обновления
        new_order = OrderCreate(
            customer_name="Клиент для обновления",
            product_name="Продукт",
            quantity=1,
            total_price=999.99,
            status="pending"
        )
        created = create_order(new_order)
        
        # Обновляем заказ
        from models import OrderUpdate
        updated_data = OrderUpdate(status="completed")
        updated = update_order(created.id, updated_data)
        assert updated is not None
        assert updated.status == "completed"
    
    def test_delete_order_exists(self):
        """Проверка удаления существующего заказа"""
        # Создаем заказ для удаления
        new_order = OrderCreate(
            customer_name="Клиент для удаления",
            product_name="Продукт",
            quantity=1,
            total_price=999.99,
            status="pending"
        )
        created = create_order(new_order)
        order_id = created.id
        
        # Удаляем заказ
        result = delete_order(order_id)
        assert result is True
        assert get_order_by_id(order_id) is None

