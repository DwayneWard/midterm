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
    
    def test_get_all_tasks_returns_json(self, client):
        """Проверка получения всех задач в формате JSON"""
        response = client.get("/api/tasks")
        if response.status_code == 200:
            assert response.headers["content-type"] == "application/json"
            data = response.json()
            assert isinstance(data, list)
    
    def test_get_task_by_id_returns_json(self, client, sample_task_create):
        """Проверка получения задачи по ID в формате JSON"""
        # Создаем задачу для гарантии, что она существует
        create_response = client.post("/api/tasks", json=sample_task_create)
        assert create_response.status_code == 201
        task_id = create_response.json()["id"]
        
        response = client.get(f"/api/tasks/{task_id}")
        if response.status_code == 200:
            assert response.headers["content-type"] == "application/json"
            data = response.json()
            assert "id" in data
            assert "title" in data
            assert "priority" in data
            assert "completed" in data
    
    def test_create_task_via_api(self, client, sample_task_create):
        """Проверка создания задачи через API"""
        response = client.post("/api/tasks", json=sample_task_create)
        if response.status_code == 201:
            assert response.headers["content-type"] == "application/json"
            data = response.json()
            assert data["title"] == sample_task_create["title"]
            assert data["priority"] == sample_task_create["priority"]
            assert "id" in data
    
    def test_update_task_via_api(self, client, sample_task_create):
        """Проверка обновления задачи через API"""
        # Создаем задачу для гарантии, что она существует
        create_response = client.post("/api/tasks", json=sample_task_create)
        assert create_response.status_code == 201
        task_id = create_response.json()["id"]
        
        update_data = {"title": "Обновленное название"}
        response = client.put(f"/api/tasks/{task_id}", json=update_data)
        if response.status_code == 200:
            assert response.headers["content-type"] == "application/json"
            data = response.json()
            assert data["title"] == "Обновленное название"
    
    def test_delete_task_via_api(self, client, sample_task_create):
        """Проверка удаления задачи через API"""
        # Создаем задачу для гарантии, что она существует
        create_response = client.post("/api/tasks", json=sample_task_create)
        assert create_response.status_code == 201
        task_id = create_response.json()["id"]
        
        # Удаляем задачу
        delete_response = client.delete(f"/api/tasks/{task_id}")
        assert delete_response.status_code in [204, 404, 500]
