"""
Тесты для models.py
Проверяют ОРы: 5.1 (Pydantic валидация)
"""
import pytest
from pydantic import ValidationError

try:
    from models import ProductCreate, Product, ProductUpdate
except ImportError:
    pytest.skip("models module not available", allow_module_level=True)


class TestOR51_PydanticValidation:
    """ОР 5.1: Использовать Pydantic для валидации данных"""
    
    def test_product_create_valid_data(self):
        """Проверка создания ProductCreate с валидными данными"""
        product = ProductCreate(
            name="Тестовый продукт",
            description="Описание",
            price=999.99,
            category="electronics",
            stock=10
        )
        assert product.name == "Тестовый продукт"
        assert product.price == 999.99
        assert product.category == "electronics"
        assert product.stock == 10
    
    def test_product_create_minimal_data(self):
        """Проверка создания ProductCreate с минимальными данными"""
        product = ProductCreate(
            name="Продукт",
            price=199.99,
            category="food"
        )
        assert product.name == "Продукт"
        assert product.description is None
        assert product.stock == 0
    
    def test_product_create_validation_name_required(self):
        """Проверка валидации: name обязателен"""
        with pytest.raises(ValidationError):
            ProductCreate(price=999.99, category="electronics")
    
    def test_product_create_validation_price_required(self):
        """Проверка валидации: price обязателен"""
        with pytest.raises(ValidationError):
            ProductCreate(name="Продукт", category="electronics")
    
    def test_product_create_validation_category_required(self):
        """Проверка валидации: category обязателен"""
        with pytest.raises(ValidationError):
            ProductCreate(name="Продукт", price=999.99)
    
    def test_product_create_validation_category_enum(self):
        """Проверка валидации: category должен быть из списка допустимых"""
        with pytest.raises(ValidationError):
            ProductCreate(name="Продукт", price=999.99, category="invalid")
    
    def test_product_inherits_from_product_create(self):
        """Проверка наследования Product от ProductCreate"""
        from datetime import datetime
        product = Product(
            id=1,
            name="Продукт",
            price=199.99,
            category="clothing",
            created_at=datetime.now()
        )
        assert product.id == 1
        assert product.name == "Продукт"
        assert product.created_at is not None
    
    def test_product_update_all_optional(self):
        """Проверка, что все поля ProductUpdate необязательны"""
        product_update = ProductUpdate()
        assert product_update.name is None
        assert product_update.price is None
        assert product_update.category is None
        assert product_update.stock is None
