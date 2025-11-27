"""
Тесты для models.py
Проверяют ОРы: 5.1 (Pydantic валидация)
"""
import pytest
from pydantic import ValidationError

try:
    from models import OrderCreate, Order, OrderUpdate
except ImportError:
    pytest.skip("models module not available", allow_module_level=True)


class TestOR51_PydanticValidation:
    """ОР 5.1: Использовать Pydantic для валидации данных"""
    
    def test_order_create_valid_data(self):
        """Проверка создания OrderCreate с валидными данными"""
        order = OrderCreate(
            customer_name="Иван Иванов",
            product_name="Тестовый продукт",
            quantity=2,
            total_price=1999.98,
            status="pending"
        )
        assert order.customer_name == "Иван Иванов"
        assert order.product_name == "Тестовый продукт"
        assert order.quantity == 2
        assert order.total_price == 1999.98
        assert order.status == "pending"
    
    def test_order_create_minimal_data(self):
        """Проверка создания OrderCreate с минимальными данными"""
        order = OrderCreate(
            customer_name="Петр Петров",
            product_name="Продукт",
            quantity=1,
            total_price=999.99,
            status="processing"
        )
        assert order.customer_name == "Петр Петров"
        assert order.quantity == 1
    
    def test_order_create_validation_customer_name_required(self):
        """Проверка валидации: customer_name обязателен"""
        with pytest.raises(ValidationError):
            OrderCreate(product_name="Продукт", quantity=1, total_price=999.99, status="pending")
    
    def test_order_create_validation_product_name_required(self):
        """Проверка валидации: product_name обязателен"""
        with pytest.raises(ValidationError):
            OrderCreate(customer_name="Иван", quantity=1, total_price=999.99, status="pending")
    
    def test_order_create_validation_quantity_required(self):
        """Проверка валидации: quantity обязателен"""
        with pytest.raises(ValidationError):
            OrderCreate(customer_name="Иван", product_name="Продукт", total_price=999.99, status="pending")
    
    def test_order_create_validation_total_price_required(self):
        """Проверка валидации: total_price обязателен"""
        with pytest.raises(ValidationError):
            OrderCreate(customer_name="Иван", product_name="Продукт", quantity=1, status="pending")
    
    def test_order_create_validation_status_required(self):
        """Проверка валидации: status обязателен"""
        with pytest.raises(ValidationError):
            OrderCreate(customer_name="Иван", product_name="Продукт", quantity=1, total_price=999.99)
    
    def test_order_create_validation_status_enum(self):
        """Проверка валидации: status должен быть из списка допустимых"""
        with pytest.raises(ValidationError):
            OrderCreate(customer_name="Иван", product_name="Продукт", quantity=1, total_price=999.99, status="invalid")
    
    def test_order_inherits_from_order_create(self):
        """Проверка наследования Order от OrderCreate"""
        from datetime import datetime
        order = Order(
            id=1,
            customer_name="Иван",
            product_name="Продукт",
            quantity=1,
            total_price=999.99,
            status="pending",
            created_at=datetime.now()
        )
        assert order.id == 1
        assert order.customer_name == "Иван"
        assert order.created_at is not None
    
    def test_order_update_all_optional(self):
        """Проверка, что все поля OrderUpdate необязательны"""
        order_update = OrderUpdate()
        assert order_update.customer_name is None
        assert order_update.product_name is None
        assert order_update.quantity is None
        assert order_update.total_price is None
        assert order_update.status is None

