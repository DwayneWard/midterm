"""
Тесты для storage.py
Проверяют базовую функциональность хранения данных
"""
import pytest
from storage import (
    get_user_favorites,
    add_favorite_author,
    remove_favorite_author
)


class TestStorageFunctions:
    """Тесты функций хранения"""
    
    def test_get_user_favorites_empty(self):
        """Проверка получения пустого списка"""
        result = get_user_favorites(99999)
        assert result == []
    
    def test_add_favorite_author(self):
        """Проверка добавления автора"""
        user_id = 11111
        remove_favorite_author(user_id, "Test Author")
        
        result = add_favorite_author(user_id, "Test Author")
        assert result is True
        
        favorites = get_user_favorites(user_id)
        assert "Test Author" in favorites
    
    def test_add_duplicate_author(self):
        """Проверка добавления дубликата"""
        user_id = 22222
        add_favorite_author(user_id, "Duplicate Author")
        
        result = add_favorite_author(user_id, "Duplicate Author")
        assert result is False
    
    def test_remove_favorite_author(self):
        """Проверка удаления автора"""
        user_id = 33333
        add_favorite_author(user_id, "To Remove")
        
        result = remove_favorite_author(user_id, "To Remove")
        assert result is True
        
        favorites = get_user_favorites(user_id)
        assert "To Remove" not in favorites

