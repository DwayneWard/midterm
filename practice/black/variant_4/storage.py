from typing import List, Optional
from datetime import datetime
from models import User, UserCreate, UserUpdate


# Хранилище пользователей в памяти
users_db: List[User] = [
    User(id=1, username="admin", email="admin@example.com", full_name="Администратор", is_active=True, role="admin", created_at=datetime.now()),
    User(id=2, username="user1", email="user1@example.com", full_name="Иван Иванов", is_active=True, role="user", created_at=datetime.now()),
    User(id=3, username="moderator", email="moderator@example.com", full_name="Модератор", is_active=False, role="moderator", created_at=datetime.now()),
]


def get_all_users() -> List[User]:
    """
    Получить всех пользователей
    
    Returns:
        Список всех пользователей
    """
    return users_db


def get_user_by_id(user_id: int) -> Optional[User]:
    """
    Получить пользователя по ID
    
    Args:
        user_id: ID пользователя
        
    Returns:
        Пользователь или None, если пользователь не найден
        
    TODO: Реализовать функцию:
    1. Пройтись по списку users_db
    2. Найти пользователя с указанным id
    3. Вернуть пользователя или None, если не найден
    """
    pass


def create_user(user_data: UserCreate) -> User:
    """
    Создать нового пользователя
    
    Args:
        user_data: Данные нового пользователя (без id и created_at)
        
    Returns:
        Созданный пользователь с присвоенным id и created_at
        
    TODO: Реализовать функцию:
    1. Определить новый id (максимальный id в users_db + 1, или 1 если список пуст)
    2. Создать объект User с новым id, created_at=datetime.now() и данными из user_data
    3. Добавить пользователя в users_db
    4. Вернуть созданного пользователя
    """
    pass


def update_user(user_id: int, user_data: UserUpdate) -> Optional[User]:
    """
    Обновить пользователя
    
    Args:
        user_id: ID пользователя для обновления
        user_data: Новые данные пользователя
        
    Returns:
        Обновленный пользователь или None, если пользователь не найден
        
    TODO: Реализовать функцию:
    1. Найти пользователя с указанным id в users_db
    2. Если пользователь не найден, вернуть None
    3. Обновить поля пользователя данными из user_data (только те поля, которые не None)
       Используй: user.field = user_data.field if user_data.field is not None else user.field
    4. Вернуть обновленного пользователя
    """
    pass


def delete_user(user_id: int) -> bool:
    """
    Удалить пользователя
    
    Args:
        user_id: ID пользователя для удаления
        
    Returns:
        True, если пользователь удален, False если не найден
        
    TODO: Реализовать функцию:
    1. Найти пользователя с указанным id в users_db
    2. Если пользователь не найден, вернуть False
    3. Удалить пользователя из users_db
    4. Вернуть True
    """
    pass

