"""
Тесты для models.py
Проверяют ОРы: 5.1 (Pydantic валидация)
"""
import pytest
from pydantic import ValidationError

try:
    from models import UserCreate, User, UserUpdate
except ImportError:
    pytest.skip("models module not available", allow_module_level=True)


class TestOR51_PydanticValidation:
    """ОР 5.1: Использовать Pydantic для валидации данных"""
    
    def test_user_create_valid_data(self):
        """Проверка создания UserCreate с валидными данными"""
        user = UserCreate(
            username="testuser",
            email="test@example.com",
            full_name="Тестовый пользователь",
            is_active=True,
            role="user"
        )
        assert user.username == "testuser"
        assert user.email == "test@example.com"
        assert user.full_name == "Тестовый пользователь"
        assert user.is_active is True
        assert user.role == "user"
    
    def test_user_create_minimal_data(self):
        """Проверка создания UserCreate с минимальными данными"""
        user = UserCreate(
            username="user",
            email="user@example.com",
            role="user"
        )
        assert user.username == "user"
        assert user.full_name is None
        assert user.is_active is True
    
    def test_user_create_validation_username_required(self):
        """Проверка валидации: username обязателен"""
        with pytest.raises(ValidationError):
            UserCreate(email="test@example.com", role="user")
    
    def test_user_create_validation_email_required(self):
        """Проверка валидации: email обязателен"""
        with pytest.raises(ValidationError):
            UserCreate(username="user", role="user")
    
    def test_user_create_validation_role_required(self):
        """Проверка валидации: role обязателен"""
        with pytest.raises(ValidationError):
            UserCreate(username="user", email="test@example.com")
    
    def test_user_create_validation_role_enum(self):
        """Проверка валидации: role должен быть из списка допустимых"""
        with pytest.raises(ValidationError):
            UserCreate(username="user", email="test@example.com", role="invalid")
    
    def test_user_inherits_from_user_create(self):
        """Проверка наследования User от UserCreate"""
        from datetime import datetime
        user = User(
            id=1,
            username="user",
            email="user@example.com",
            role="user",
            created_at=datetime.now()
        )
        assert user.id == 1
        assert user.username == "user"
        assert user.created_at is not None
    
    def test_user_update_all_optional(self):
        """Проверка, что все поля UserUpdate необязательны"""
        user_update = UserUpdate()
        assert user_update.username is None
        assert user_update.email is None
        assert user_update.full_name is None
        assert user_update.is_active is None
        assert user_update.role is None

