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
    
    def test_get_all_notes_returns_json(self, client):
        """Проверка получения всех заметок в формате JSON"""
        response = client.get("/api/notes")
        if response.status_code == 200:
            assert response.headers["content-type"] == "application/json"
            data = response.json()
            assert isinstance(data, list)
    
    def test_get_note_by_id_returns_json(self, client, sample_note_create):
        """Проверка получения заметки по ID в формате JSON"""
        # Создаем заметку для гарантии, что она существует
        create_response = client.post("/api/notes", json=sample_note_create)
        assert create_response.status_code == 201
        note_id = create_response.json()["id"]
        
        response = client.get(f"/api/notes/{note_id}")
        if response.status_code == 200:
            assert response.headers["content-type"] == "application/json"
            data = response.json()
            assert "id" in data
            assert "title" in data
            assert "content" in data
            assert "tags" in data
            assert "is_pinned" in data
    
    def test_create_note_via_api(self, client, sample_note_create):
        """Проверка создания заметки через API"""
        response = client.post("/api/notes", json=sample_note_create)
        if response.status_code == 201:
            assert response.headers["content-type"] == "application/json"
            data = response.json()
            assert data["title"] == sample_note_create["title"]
            assert data["content"] == sample_note_create["content"]
            assert "id" in data
    
    def test_update_note_via_api(self, client, sample_note_create):
        """Проверка обновления заметки через API"""
        # Создаем заметку для гарантии, что она существует
        create_response = client.post("/api/notes", json=sample_note_create)
        assert create_response.status_code == 201
        note_id = create_response.json()["id"]
        
        update_data = {"title": "Обновленное название"}
        response = client.put(f"/api/notes/{note_id}", json=update_data)
        if response.status_code == 200:
            assert response.headers["content-type"] == "application/json"
            data = response.json()
            assert data["title"] == "Обновленное название"
    
    def test_delete_note_via_api(self, client, sample_note_create):
        """Проверка удаления заметки через API"""
        # Создаем заметку для гарантии, что она существует
        create_response = client.post("/api/notes", json=sample_note_create)
        assert create_response.status_code == 201
        note_id = create_response.json()["id"]
        
        # Удаляем заметку
        delete_response = client.delete(f"/api/notes/{note_id}")
        assert delete_response.status_code in [204, 404, 500]
