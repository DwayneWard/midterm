from typing import List, Dict

# Временное хранилище
_user_favorites: Dict[int, List[str]] = {}


def get_user_favorites(user_id: int) -> List[str]:
    """
    Получить список избранных категорий новостей пользователя.
    
    Args:
        user_id: ID пользователя Telegram
        
    Returns:
        Список категорий новостей
    """
    return _user_favorites.get(user_id, [])


def add_favorite_category(user_id: int, category: str) -> bool:
    """
    Добавить категорию новостей в избранное пользователя.
    
    Args:
        user_id: ID пользователя Telegram
        category: Категория новостей
        
    Returns:
        True если категория добавлена, False если уже была в списке
    """
    if user_id not in _user_favorites:
        _user_favorites[user_id] = []
    
    if category not in _user_favorites[user_id]:
        _user_favorites[user_id].append(category)
        return True
    return False


def remove_favorite_category(user_id: int, category: str) -> bool:
    """
    Удалить категорию новостей из избранного пользователя.
    
    Args:
        user_id: ID пользователя Telegram
        category: Категория новостей
        
    Returns:
        True если категория удалена, False если её не было в списке
    """
    if user_id in _user_favorites and category in _user_favorites[user_id]:
        _user_favorites[user_id].remove(category)
        return True
    return False

