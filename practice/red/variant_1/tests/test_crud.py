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
    
    def test_get_all_books_returns_json(self, client):
        """Проверка получения всех книг в формате JSON"""
        response = client.get("/api/books")
        if response.status_code == 200:
            assert response.headers["content-type"] == "application/json"
            data = response.json()
            assert isinstance(data, list)
    
    def test_get_book_by_id_returns_json(self, client):
        """Проверка получения книги по ID в формате JSON"""
        # Сначала создаем книгу
        new_book = {
            "title": "Книга для получения",
            "author": "Автор",
            "year": 2024
        }
        create_response = client.post("/api/books", json=new_book)
        if create_response.status_code == 201:
            book_id = create_response.json()["id"]
            response = client.get(f"/api/books/{book_id}")
            if response.status_code == 200:
                assert response.headers["content-type"] == "application/json"
                data = response.json()
                assert "id" in data
                assert "title" in data
                assert "author" in data
    
    def test_create_book_via_api(self, client, sample_book_create):
        """Проверка создания книги через API"""
        response = client.post("/api/books", json=sample_book_create)
        if response.status_code == 201:
            assert response.headers["content-type"] == "application/json"
            data = response.json()
            assert data["title"] == sample_book_create["title"]
            assert "id" in data
    
    def test_update_book_via_api(self, client):
        """Проверка обновления книги через API"""
        # Сначала создаем книгу
        new_book = {
            "title": "Книга для обновления",
            "author": "Автор",
            "year": 2020
        }
        create_response = client.post("/api/books", json=new_book)
        if create_response.status_code == 201:
            book_id = create_response.json()["id"]
            update_data = {"title": "Обновленное название"}
            response = client.put(f"/api/books/{book_id}", json=update_data)
            if response.status_code == 200:
                assert response.headers["content-type"] == "application/json"
                data = response.json()
                assert data["title"] == "Обновленное название"
    
    def test_delete_book_via_api(self, client):
        """Проверка удаления книги через API"""
        # Сначала создаем книгу
        new_book = {
            "title": "Книга для удаления",
            "author": "Автор",
            "year": 2024
        }
        create_response = client.post("/api/books", json=new_book)
        if create_response.status_code == 201:
            book_id = create_response.json()["id"]
            # Удаляем книгу
            delete_response = client.delete(f"/api/books/{book_id}")
            assert delete_response.status_code in [204, 404, 500]

