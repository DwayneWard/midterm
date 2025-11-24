"""
Тесты для storage.py
Проверяют базовую функциональность хранения данных
"""
import pytest
from storage import (
    get_user_favorites,
    add_favorite_category,
    remove_favorite_category
)


class TestStorageFunctions:
    """Тесты функций хранения"""
    
    def test_get_user_favorites_empty(self):
        result = get_user_favorites(99999)
        assert result == []
    
    def test_add_favorite_category(self):
        user_id = 11111
        remove_favorite_category(user_id, "technology")
        
        result = add_favorite_category(user_id, "technology")
        assert result is True
        
        favorites = get_user_favorites(user_id)
        assert "technology" in favorites
    
    def test_add_duplicate_category(self):
        user_id = 22222
        add_favorite_category(user_id, "business")
        
        result = add_favorite_category(user_id, "business")
        assert result is False

