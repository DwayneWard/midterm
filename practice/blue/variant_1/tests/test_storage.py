"""
Тесты для storage.py
Проверяют базовую функциональность хранения данных
"""
import pytest
from storage import (
    get_user_favorites,
    add_favorite_country,
    remove_favorite_country
)


class TestStorageFunctions:
    """Тесты функций хранения"""
    
    def test_get_user_favorites_empty(self):
        """Проверка получения пустого списка"""
        result = get_user_favorites(99999)
        assert result == []
    
    def test_add_favorite_country(self):
        """Проверка добавления страны"""
        user_id = 11111
        # Очищаем перед тестом
        remove_favorite_country(user_id, "TestCountry")
        
        result = add_favorite_country(user_id, "TestCountry")
        assert result is True
        
        favorites = get_user_favorites(user_id)
        assert "TestCountry" in favorites
    
    def test_add_duplicate_country(self):
        """Проверка добавления дубликата"""
        user_id = 22222
        add_favorite_country(user_id, "DuplicateCountry")
        
        result = add_favorite_country(user_id, "DuplicateCountry")
        assert result is False
    
    def test_remove_favorite_country(self):
        """Проверка удаления страны"""
        user_id = 33333
        add_favorite_country(user_id, "ToRemove")
        
        result = remove_favorite_country(user_id, "ToRemove")
        assert result is True
        
        favorites = get_user_favorites(user_id)
        assert "ToRemove" not in favorites
    
    def test_remove_nonexistent_country(self):
        """Проверка удаления несуществующей страны"""
        user_id = 44444
        result = remove_favorite_country(user_id, "Nonexistent")
        assert result is False

