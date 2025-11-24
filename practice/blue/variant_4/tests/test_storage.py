"""
Тесты для storage.py
Проверяют базовую функциональность хранения данных
"""
import pytest
from storage import (
    get_user_favorites,
    add_favorite_task,
    remove_favorite_task
)


class TestStorageFunctions:
    """Тесты функций хранения"""
    
    def test_get_user_favorites_empty(self):
        """Проверка получения пустого списка"""
        result = get_user_favorites(99999)
        assert result == []
    
    def test_add_favorite_task(self):
        """Проверка добавления задачи"""
        user_id = 11111
        remove_favorite_task(user_id, 1)
        
        result = add_favorite_task(user_id, 1)
        assert result is True
        
        favorites = get_user_favorites(user_id)
        assert 1 in favorites
    
    def test_add_duplicate_task(self):
        """Проверка добавления дубликата"""
        user_id = 22222
        add_favorite_task(user_id, 2)
        
        result = add_favorite_task(user_id, 2)
        assert result is False
    
    def test_remove_favorite_task(self):
        """Проверка удаления задачи"""
        user_id = 33333
        add_favorite_task(user_id, 3)
        
        result = remove_favorite_task(user_id, 3)
        assert result is True
        
        favorites = get_user_favorites(user_id)
        assert 3 not in favorites

