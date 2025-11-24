"""
Тесты для storage.py
Проверяют базовую функциональность хранения данных
"""
import pytest
from storage import (
    get_user_favorites,
    add_favorite_pair,
    remove_favorite_pair
)


class TestStorageFunctions:
    """Тесты функций хранения"""
    
    def test_get_user_favorites_empty(self):
        """Проверка получения пустого списка"""
        result = get_user_favorites(99999)
        assert result == []
    
    def test_add_favorite_pair(self):
        """Проверка добавления валютной пары"""
        user_id = 11111
        remove_favorite_pair(user_id, "USD", "EUR")
        
        result = add_favorite_pair(user_id, "USD", "EUR")
        assert result is True
        
        favorites = get_user_favorites(user_id)
        assert "USD/EUR" in favorites
    
    def test_add_duplicate_pair(self):
        """Проверка добавления дубликата"""
        user_id = 22222
        add_favorite_pair(user_id, "USD", "RUB")
        
        result = add_favorite_pair(user_id, "USD", "RUB")
        assert result is False
    
    def test_remove_favorite_pair(self):
        """Проверка удаления пары"""
        user_id = 33333
        add_favorite_pair(user_id, "EUR", "GBP")
        
        result = remove_favorite_pair(user_id, "EUR", "GBP")
        assert result is True
        
        favorites = get_user_favorites(user_id)
        assert "EUR/GBP" not in favorites

