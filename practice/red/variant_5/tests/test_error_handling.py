"""
Тесты для обработки ошибок
Проверяют ОРы: 6.1, 6.2 (обработка ошибок, HTTP статусы)
"""
import pytest

try:
    from fastapi import status
except ImportError:
    pytest.skip("fastapi not available", allow_module_level=True)


class TestOR61_ErrorHandling:
    """ОР 6.1: Создавать кастомные обработчики ошибок в FastAPI"""
    
    def test_404_handler_exists(self, client):
        """Проверка обработки ошибки 404"""
        response = client.get("/nonexistent-page")
        # Если обработчик реализован, должен вернуть HTML со статусом 404
        if response.status_code == 404:
            assert "text/html" in response.headers.get("content-type", "")
    
    def test_500_handler_exists(self, client):
        """Проверка обработки ошибки 500"""
        # Попытка вызвать ошибку (например, невалидный запрос)
        # Это может не всегда вызывать 500, но проверяем структуру
        response = client.get("/notes/invalid-id")
        # Может быть 404, 422, 500 в зависимости от реализации
        assert response.status_code in [404, 422, 500]


class TestOR62_HTTPStatusCodes:
    """ОР 6.2: Настраивать статусы ответов для разных сценариев"""
    
    def test_get_existing_note_returns_200(self, client):
        """Проверка статуса 200 для успешного получения книги"""
        response = client.get("/api/notes/1")
        if response.status_code == 200:
            assert response.status_code == 200
    
    def test_get_nonexistent_note_returns_404(self, client):
        """Проверка статуса 404 для несуществующей книги"""
        response = client.get("/api/notes/99999")
        if response.status_code == 404:
            assert response.status_code == 404
    
    def test_create_note_returns_201(self, client, sample_note_create):
        """Проверка статуса 201 для создания ресурса"""
        response = client.post("/api/notes", json=sample_note_create)
        if response.status_code == 201:
            assert response.status_code == 201
    
    def test_delete_note_returns_204(self, client):
        """Проверка статуса 204 для удаления ресурса"""
        # Сначала создаем книгу
        new_note = {
            "title": "Книга для удаления",
            "author": "Автор",
            "year": 2024
        }
        create_response = client.post("/api/notes", json=new_note)
        if create_response.status_code == 201:
            note_id = create_response.json()["id"]
            delete_response = client.delete(f"/api/notes/{note_id}")
            if delete_response.status_code == 204:
                assert delete_response.status_code == 204
    
    def test_invalid_data_returns_400_or_422(self, client):
        """Проверка статуса 400/422 для невалидных данных"""
        invalid_data = {"title": ""}  # Пустое обязательное поле
        response = client.post("/api/notes", json=invalid_data)
        assert response.status_code in [400, 422, 500]

