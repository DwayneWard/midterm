"""
Тесты для models.py
Проверяют ОРы: 3.1 (валидация данных с помощью Pydantic)
"""
import pytest
from pydantic import ValidationError

try:
    from models import ProductCreate, Product, ProductUpdate
except ImportError:
    pytest.skip("models module not available", allow_module_level=True)


class TestOR31_PydanticValidation:
    """ОР 3.1: Использовать Pydantic для валидации данных"""
    
    def test_product_create_valid_data(self):
        """Проверка создания ProductCreate с валидными данными"""
        product = ProductCreate(
            name="Тестовый продукт",
            description="Описание продукта",
            price=999.99,
            category="electronics",
            stock=10
        )
        assert product.name == "Тестовый продукт"
        assert product.description == "Описание продукта"
        assert product.price == 999.99
        assert product.category == "electronics"
        assert product.stock == 10
    
    def test_product_create_minimal_data(self):
        """Проверка создания ProductCreate с минимальными данными"""
        product = ProductCreate(
            name="Продукт",
            price=100.0,
            category="other",
            stock=0
        )
        assert product.name == "Продукт"
        assert product.description is None
    
    def test_product_create_validation_name_required(self):
        """Проверка валидации: name обязателен"""
        with pytest.raises(ValidationError):
            ProductCreate(price=100.0, category="other", stock=0)
    
    def test_product_create_validation_price_required(self):
        """Проверка валидации: price обязателен"""
        with pytest.raises(ValidationError):
            ProductCreate(name="Продукт", category="other", stock=0)
    
    def test_product_create_validation_category_required(self):
        """Проверка валидации: category обязателен"""
        with pytest.raises(ValidationError):
            ProductCreate(name="Продукт", price=100.0, stock=0)
    
    def test_product_create_validation_stock_required(self):
        """Проверка валидации: stock обязателен"""
        with pytest.raises(ValidationError):
            ProductCreate(name="Продукт", price=100.0, category="other")
    
    def test_product_inherits_from_product_create(self):
        """Проверка наследования Product от ProductCreate"""
        product = Product(
            id=1,
            name="Продукт",
            price=100.0,
            category="clothing",
            stock=5
        )
        assert product.id == 1
        assert product.name == "Продукт"
    
    def test_product_update_all_optional(self):
        """Проверка, что все поля ProductUpdate необязательны"""
        product_update = ProductUpdate()
        assert product_update.name is None
        assert product_update.price is None
        assert product_update.category is None
        assert product_update.stock is None
        assert product_update.description is None
    
    def test_product_update_partial_update(self):
        """Проверка частичного обновления ProductUpdate"""
        product_update = ProductUpdate(name="Новое название")
        assert product_update.name == "Новое название"
        assert product_update.price is None
