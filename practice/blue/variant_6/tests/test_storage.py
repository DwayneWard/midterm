"""
Тесты для storage.py
Проверяют базовую функциональность хранения данных
"""
import pytest
from storage import (
    get_user_favorites,
    add_favorite_meal,
    remove_favorite_meal
)


class TestStorageFunctions:
    """Тесты функций хранения"""
    
    def test_get_user_favorites_empty(self):
        """Проверка получения пустого списка"""
        result = get_user_favorites(99999)
        assert result == []
    
    def test_add_favorite_meal(self):
        """Проверка добавления блюда"""
        user_id = 11111
        remove_favorite_meal(user_id, "Pasta")
        
        result = add_favorite_meal(user_id, "Pasta")
        assert result is True
        
        favorites = get_user_favorites(user_id)
        assert "Pasta" in favorites
    
    def test_add_duplicate_meal(self):
        """Проверка добавления дубликата"""
        user_id = 22222
        add_favorite_meal(user_id, "Pizza")
        
        result = add_favorite_meal(user_id, "Pizza")
        assert result is False
    
    def test_remove_favorite_meal(self):
        """Проверка удаления блюда"""
        user_id = 33333
        add_favorite_meal(user_id, "Salad")
        
        result = remove_favorite_meal(user_id, "Salad")
        assert result is True
        
        favorites = get_user_favorites(user_id)
        assert "Salad" not in favorites

