from typing import List, Dict

# Временное хранилище
_user_favorites: Dict[int, List[str]] = {}


def get_user_favorites(user_id: int) -> List[str]:
    """
    Получить список избранных стран пользователя.
    
    Args:
        user_id: ID пользователя Telegram
        
    Returns:
        Список названий стран
    """
    return _user_favorites.get(user_id, [])


def add_favorite_country(user_id: int, country_name: str) -> bool:
    """
    Добавить страну в избранное пользователя.
    
    Args:
        user_id: ID пользователя Telegram
        country_name: Название страны
        
    Returns:
        True если страна добавлена, False если уже была в списке
    """
    if user_id not in _user_favorites:
        _user_favorites[user_id] = []
    
    if country_name not in _user_favorites[user_id]:
        _user_favorites[user_id].append(country_name)
        return True
    return False


def remove_favorite_country(user_id: int, country_name: str) -> bool:
    """
    Удалить страну из избранного пользователя.
    
    Args:
        user_id: ID пользователя Telegram
        country_name: Название страны
        
    Returns:
        True если страна удалена, False если её не было в списке
    """
    if user_id in _user_favorites and country_name in _user_favorites[user_id]:
        _user_favorites[user_id].remove(country_name)
        return True
    return False

