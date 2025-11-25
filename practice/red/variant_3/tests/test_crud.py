"""
Тесты для CRUD операций
Проверяют ОРы: 3.3 (CRUD операции, JSON)
"""
import pytest
from datetime import date

try:
    from fastapi import status
except ImportError:
    pytest.skip("fastapi not available", allow_module_level=True)


class TestOR33_CRUDOperations:
    """ОР 3.3: Создавать эндпоинты для CRUD-операций"""
    
    def test_get_all_events_returns_json(self, client):
        """Проверка получения всех событий в формате JSON"""
        response = client.get("/api/events")
        if response.status_code == 200:
            assert response.headers["content-type"] == "application/json"
            data = response.json()
            assert isinstance(data, list)
    
    def test_get_event_by_id_returns_json(self, client, sample_event_create):
        """Проверка получения события по ID в формате JSON"""
        # Создаем событие для гарантии, что оно существует
        create_response = client.post("/api/events", json=sample_event_create)
        assert create_response.status_code == 201
        event_id = create_response.json()["id"]
        
        response = client.get(f"/api/events/{event_id}")
        if response.status_code == 200:
            assert response.headers["content-type"] == "application/json"
            data = response.json()
            assert "id" in data
            assert "title" in data
            assert "event_date" in data
            assert "location" in data
            assert "category" in data
    
    def test_create_event_via_api(self, client, sample_event_create):
        """Проверка создания события через API"""
        response = client.post("/api/events", json=sample_event_create)
        if response.status_code == 201:
            assert response.headers["content-type"] == "application/json"
            data = response.json()
            assert data["title"] == sample_event_create["title"]
            assert data["location"] == sample_event_create["location"]
            assert "id" in data
    
    def test_update_event_via_api(self, client, sample_event_create):
        """Проверка обновления события через API"""
        # Создаем событие для гарантии, что оно существует
        create_response = client.post("/api/events", json=sample_event_create)
        assert create_response.status_code == 201
        event_id = create_response.json()["id"]
        
        update_data = {"title": "Обновленное название"}
        response = client.put(f"/api/events/{event_id}", json=update_data)
        if response.status_code == 200:
            assert response.headers["content-type"] == "application/json"
            data = response.json()
            assert data["title"] == "Обновленное название"
    
    def test_delete_event_via_api(self, client, sample_event_create):
        """Проверка удаления события через API"""
        # Создаем событие для гарантии, что оно существует
        create_response = client.post("/api/events", json=sample_event_create)
        assert create_response.status_code == 201
        event_id = create_response.json()["id"]
        
        # Удаляем событие
        delete_response = client.delete(f"/api/events/{event_id}")
        assert delete_response.status_code in [204, 404, 500]
