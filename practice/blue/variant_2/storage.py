from typing import List, Dict

# Временное хранилище
_user_favorites: Dict[int, List[str]] = {}


def get_user_favorites(user_id: int) -> List[str]:
    """
    Получить список избранных валютных пар пользователя.
    
    Args:
        user_id: ID пользователя Telegram
        
    Returns:
        Список валютных пар в формате "BASE/TARGET" (например, "USD/EUR")
    """
    return _user_favorites.get(user_id, [])


def add_favorite_pair(user_id: int, base_currency: str, target_currency: str) -> bool:
    """
    Добавить валютную пару в избранное пользователя.
    
    Args:
        user_id: ID пользователя Telegram
        base_currency: Код базовой валюты
        target_currency: Код целевой валюты
        
    Returns:
        True если пара добавлена, False если уже была в списке
    """
    pair = f"{base_currency}/{target_currency}"
    if user_id not in _user_favorites:
        _user_favorites[user_id] = []
    
    if pair not in _user_favorites[user_id]:
        _user_favorites[user_id].append(pair)
        return True
    return False


def remove_favorite_pair(user_id: int, base_currency: str, target_currency: str) -> bool:
    """
    Удалить валютную пару из избранного пользователя.
    
    Args:
        user_id: ID пользователя Telegram
        base_currency: Код базовой валюты
        target_currency: Код целевой валюты
        
    Returns:
        True если пара удалена, False если её не было в списке
    """
    pair = f"{base_currency}/{target_currency}"
    if user_id in _user_favorites and pair in _user_favorites[user_id]:
        _user_favorites[user_id].remove(pair)
        return True
    return False

