"""
Тесты для storage.py
Проверяют ОРы: 3.2 (работа с данными в памяти)
"""
import pytest

try:
    from storage import (
        get_all_products,
        get_product_by_id,
        create_product,
        update_product,
        delete_product
    )
    from models import Product, ProductCreate
except ImportError:
    pytest.skip("storage module not available", allow_module_level=True)


class TestOR32_DataStorage:
    """ОР 3.2: Работать с данными в памяти"""
    
    def test_get_all_products_returns_list(self):
        """Проверка получения всех продуктов"""
        products = get_all_products()
        assert isinstance(products, list)
        assert len(products) > 0
    
    def test_get_product_by_id_exists(self):
        """Проверка получения продукта по существующему ID"""
        # Создаем продукт для гарантии, что он существует
        new_product = ProductCreate(
            name="Тестовый продукт для проверки",
            price=199.99,
            category="other",
            stock=1
        )
        created = create_product(new_product)
        product_id = created.id
        
        # Проверяем получение продукта
        product = get_product_by_id(product_id)
        assert product is not None
        assert product.id == product_id
    
    def test_get_product_by_id_not_exists(self):
        """Проверка получения продукта по несуществующему ID"""
        product = get_product_by_id(99999)
        assert product is None
    
    def test_create_product_adds_to_storage(self):
        """Проверка создания нового продукта"""
        initial_count = len(get_all_products())
        new_product = ProductCreate(
            name="Новый тестовый продукт",
            price=299.99,
            category="food",
            stock=20
        )
        created = create_product(new_product)
        assert created.id is not None
        assert created.name == "Новый тестовый продукт"
        assert len(get_all_products()) == initial_count + 1
    
    def test_update_product_exists(self):
        """Проверка обновления существующего продукта"""
        # Создаем продукт для обновления
        new_product = ProductCreate(
            name="Продукт для обновления",
            price=99.99,
            category="clothing",
            stock=5
        )
        created = create_product(new_product)
        
        # Обновляем продукт
        from models import ProductUpdate
        updated_data = ProductUpdate(name="Обновленное название")
        updated = update_product(created.id, updated_data)
        assert updated is not None
        assert updated.name == "Обновленное название"
    
    def test_update_product_not_exists(self):
        """Проверка обновления несуществующего продукта"""
        from models import ProductUpdate
        updated_data = ProductUpdate(name="Тест")
        result = update_product(99999, updated_data)
        assert result is None
    
    def test_delete_product_exists(self):
        """Проверка удаления существующего продукта"""
        # Создаем продукт для удаления
        new_product = ProductCreate(
            name="Продукт для удаления",
            price=49.99,
            category="other",
            stock=0
        )
        created = create_product(new_product)
        product_id = created.id
        
        # Удаляем продукт
        result = delete_product(product_id)
        assert result is True
        assert get_product_by_id(product_id) is None
    
    def test_delete_product_not_exists(self):
        """Проверка удаления несуществующего продукта"""
        result = delete_product(99999)
        assert result is False
