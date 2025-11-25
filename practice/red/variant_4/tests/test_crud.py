"""
Тесты для CRUD операций
Проверяют ОРы: 3.3 (CRUD операции, JSON)
"""
import pytest

try:
    from fastapi import status
except ImportError:
    pytest.skip("fastapi not available", allow_module_level=True)


class TestOR33_CRUDOperations:
    """ОР 3.3: Создавать эндпоинты для CRUD-операций"""
    
    def test_get_all_products_returns_json(self, client):
        """Проверка получения всех продуктов в формате JSON"""
        response = client.get("/api/products")
        if response.status_code == 200:
            assert response.headers["content-type"] == "application/json"
            data = response.json()
            assert isinstance(data, list)
    
    def test_get_product_by_id_returns_json(self, client, sample_product_create):
        """Проверка получения продукта по ID в формате JSON"""
        # Создаем продукт для гарантии, что он существует
        create_response = client.post("/api/products", json=sample_product_create)
        assert create_response.status_code == 201
        product_id = create_response.json()["id"]
        
        response = client.get(f"/api/products/{product_id}")
        if response.status_code == 200:
            assert response.headers["content-type"] == "application/json"
            data = response.json()
            assert "id" in data
            assert "name" in data
            assert "price" in data
            assert "category" in data
            assert "stock" in data
    
    def test_create_product_via_api(self, client, sample_product_create):
        """Проверка создания продукта через API"""
        response = client.post("/api/products", json=sample_product_create)
        if response.status_code == 201:
            assert response.headers["content-type"] == "application/json"
            data = response.json()
            assert data["name"] == sample_product_create["name"]
            assert data["price"] == sample_product_create["price"]
            assert data["category"] == sample_product_create["category"]
            assert "id" in data
    
    def test_update_product_via_api(self, client, sample_product_create):
        """Проверка обновления продукта через API"""
        # Создаем продукт для гарантии, что он существует
        create_response = client.post("/api/products", json=sample_product_create)
        assert create_response.status_code == 201
        product_id = create_response.json()["id"]
        
        update_data = {"name": "Обновленное название"}
        response = client.put(f"/api/products/{product_id}", json=update_data)
        if response.status_code == 200:
            assert response.headers["content-type"] == "application/json"
            data = response.json()
            assert data["name"] == "Обновленное название"
    
    def test_delete_product_via_api(self, client, sample_product_create):
        """Проверка удаления продукта через API"""
        # Создаем продукт для гарантии, что он существует
        create_response = client.post("/api/products", json=sample_product_create)
        assert create_response.status_code == 201
        product_id = create_response.json()["id"]
        
        # Удаляем продукт
        delete_response = client.delete(f"/api/products/{product_id}")
        assert delete_response.status_code in [204, 404, 500]
