from typing import List, Dict

# Временное хранилище
_user_favorites: Dict[int, List[str]] = {}


def get_user_favorites(user_id: int) -> List[str]:
    """
    Получить список избранных названий блюд пользователя.
    
    Args:
        user_id: ID пользователя Telegram
        
    Returns:
        Список названий блюд
    """
    return _user_favorites.get(user_id, [])


def add_favorite_meal(user_id: int, meal_name: str) -> bool:
    """
    Добавить блюдо в избранное пользователя.
    
    Args:
        user_id: ID пользователя Telegram
        meal_name: Название блюда
        
    Returns:
        True если блюдо добавлено, False если уже было в списке
    """
    if user_id not in _user_favorites:
        _user_favorites[user_id] = []
    
    if meal_name not in _user_favorites[user_id]:
        _user_favorites[user_id].append(meal_name)
        return True
    return False


def remove_favorite_meal(user_id: int, meal_name: str) -> bool:
    """
    Удалить блюдо из избранного пользователя.
    
    Args:
        user_id: ID пользователя Telegram
        meal_name: Название блюда
        
    Returns:
        True если блюдо удалено, False если его не было в списке
    """
    if user_id in _user_favorites and meal_name in _user_favorites[user_id]:
        _user_favorites[user_id].remove(meal_name)
        return True
    return False

