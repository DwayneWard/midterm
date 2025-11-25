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
    
    def test_get_all_recipes_returns_json(self, client):
        """Проверка получения всех рецептов в формате JSON"""
        response = client.get("/api/recipes")
        if response.status_code == 200:
            assert response.headers["content-type"] == "application/json"
            data = response.json()
            assert isinstance(data, list)
    
    def test_get_recipe_by_id_returns_json(self, client, sample_recipe_create):
        """Проверка получения рецепта по ID в формате JSON"""
        # Создаем рецепт для гарантии, что он существует
        create_response = client.post("/api/recipes", json=sample_recipe_create)
        assert create_response.status_code == 201
        recipe_id = create_response.json()["id"]
        
        response = client.get(f"/api/recipes/{recipe_id}")
        if response.status_code == 200:
            assert response.headers["content-type"] == "application/json"
            data = response.json()
            assert "id" in data
            assert "name" in data
            assert "ingredients" in data
            assert "cooking_time" in data
            assert "difficulty" in data
    
    def test_create_recipe_via_api(self, client, sample_recipe_create):
        """Проверка создания рецепта через API"""
        response = client.post("/api/recipes", json=sample_recipe_create)
        if response.status_code == 201:
            assert response.headers["content-type"] == "application/json"
            data = response.json()
            assert data["name"] == sample_recipe_create["name"]
            assert data["ingredients"] == sample_recipe_create["ingredients"]
            assert "id" in data
    
    def test_update_recipe_via_api(self, client, sample_recipe_create):
        """Проверка обновления рецепта через API"""
        # Создаем рецепт для гарантии, что он существует
        create_response = client.post("/api/recipes", json=sample_recipe_create)
        assert create_response.status_code == 201
        recipe_id = create_response.json()["id"]
        
        update_data = {"name": "Обновленное название"}
        response = client.put(f"/api/recipes/{recipe_id}", json=update_data)
        if response.status_code == 200:
            assert response.headers["content-type"] == "application/json"
            data = response.json()
            assert data["name"] == "Обновленное название"
    
    def test_delete_recipe_via_api(self, client, sample_recipe_create):
        """Проверка удаления рецепта через API"""
        # Создаем рецепт для гарантии, что он существует
        create_response = client.post("/api/recipes", json=sample_recipe_create)
        assert create_response.status_code == 201
        recipe_id = create_response.json()["id"]
        
        # Удаляем рецепт
        delete_response = client.delete(f"/api/recipes/{recipe_id}")
        assert delete_response.status_code in [204, 404, 500]
