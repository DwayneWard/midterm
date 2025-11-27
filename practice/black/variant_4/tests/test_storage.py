"""
Тесты для storage.py
Проверяют ОРы: 3.2 (работа с данными в памяти)
"""
import pytest
from datetime import datetime

try:
    from storage import (
        get_all_users,
        get_user_by_id,
        create_user,
        update_user,
        delete_user
    )
    from models import User, UserCreate
except ImportError:
    pytest.skip("storage module not available", allow_module_level=True)


class TestOR32_DataStorage:
    """ОР 3.2: Работать с данными в памяти"""
    
    def test_get_all_users_returns_list(self):
        """Проверка получения всех пользователей"""
        users = get_all_users()
        assert isinstance(users, list)
        assert len(users) > 0
    
    def test_get_user_by_id_exists(self):
        """Проверка получения пользователя по существующему ID"""
        # Создаем пользователя для гарантии, что он существует
        new_user = UserCreate(
            username="testuser",
            email="test@example.com",
            role="user"
        )
        created = create_user(new_user)
        user_id = created.id
        
        # Проверяем получение пользователя
        user = get_user_by_id(user_id)
        assert user is not None
        assert user.id == user_id
    
    def test_get_user_by_id_not_exists(self):
        """Проверка получения пользователя по несуществующему ID"""
        user = get_user_by_id(99999)
        assert user is None
    
    def test_create_user_adds_to_storage(self):
        """Проверка создания нового пользователя"""
        initial_count = len(get_all_users())
        new_user = UserCreate(
            username="newuser",
            email="newuser@example.com",
            role="user"
        )
        created = create_user(new_user)
        assert created.id is not None
        assert created.created_at is not None
        assert len(get_all_users()) == initial_count + 1
    
    def test_update_user_exists(self):
        """Проверка обновления существующего пользователя"""
        # Создаем пользователя для обновления
        new_user = UserCreate(
            username="user_to_update",
            email="update@example.com",
            role="user"
        )
        created = create_user(new_user)
        
        # Обновляем пользователя
        from models import UserUpdate
        updated_data = UserUpdate(is_active=False)
        updated = update_user(created.id, updated_data)
        assert updated is not None
        assert updated.is_active is False
    
    def test_delete_user_exists(self):
        """Проверка удаления существующего пользователя"""
        # Создаем пользователя для удаления
        new_user = UserCreate(
            username="user_to_delete",
            email="delete@example.com",
            role="user"
        )
        created = create_user(new_user)
        user_id = created.id
        
        # Удаляем пользователя
        result = delete_user(user_id)
        assert result is True
        assert get_user_by_id(user_id) is None

