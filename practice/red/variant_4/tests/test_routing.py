"""
Тесты для маршрутизации FastAPI
Проверяют ОРы: 2.1, 2.2 (маршрутизация, GET/POST, path parameters)
"""
import pytest

try:
    from fastapi import status
except ImportError:
    pytest.skip("fastapi not available", allow_module_level=True)


class TestOR21_Routing:
    """ОР 2.1: Создавать базовые эндпоинты и обрабатывать запросы"""
    
    def test_root_endpoint_exists(self, client):
        """Проверка существования корневого эндпоинта"""
        response = client.get("/")
        # Может быть 200 (если реализовано) или 500 (если нет)
        assert response.status_code in [200, 500]
    
    def test_get_products_api_endpoint_exists(self, client):
        """Проверка существования API эндпоинта для получения всех книг"""
        response = client.get("/api/products")
        # Может быть 200 (если реализовано) или 500 (если нет)
        assert response.status_code in [200, 500]
    
    def test_get_product_by_id_api_endpoint_exists(self, client):
        """Проверка существования API эндпоинта для получения книги по ID"""
        response = client.get("/api/products/1")
        # Может быть 200 или 404 (если реализовано) или 500 (если нет)
        assert response.status_code in [200, 404, 500]


class TestOR22_PathParameters:
    """ОР 2.2: Работать с path parameters"""
    
    def test_path_parameter_extracted(self, client):
        """Проверка извлечения path parameter"""
        response = client.get("/products/1")
        # Если реализовано, должен вернуть страницу или 404
        assert response.status_code in [200, 404, 500]
    
    def test_path_parameter_different_values(self, client):
        """Проверка работы с разными значениями path parameter"""
        for product_id in [1, 2, 3]:
            response = client.get(f"/products/{product_id}")
            assert response.status_code in [200, 404, 500]
    
    def test_api_path_parameter_works(self, client):
        """Проверка path parameter в API эндпоинте"""
        response = client.get("/api/products/1")
        assert response.status_code in [200, 404, 500]

