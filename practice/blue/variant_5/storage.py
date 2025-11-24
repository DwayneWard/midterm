from typing import List, Dict

# Временное хранилище
_user_favorites: Dict[int, List[str]] = {}


def get_user_favorites(user_id: int) -> List[str]:
    """
    Получить список избранных авторов цитат пользователя.
    
    Args:
        user_id: ID пользователя Telegram
        
    Returns:
        Список имен авторов
    """
    return _user_favorites.get(user_id, [])


def add_favorite_author(user_id: int, author: str) -> bool:
    """
    Добавить автора в избранное пользователя.
    
    Args:
        user_id: ID пользователя Telegram
        author: Имя автора
        
    Returns:
        True если автор добавлен, False если уже был в списке
    """
    if user_id not in _user_favorites:
        _user_favorites[user_id] = []
    
    if author not in _user_favorites[user_id]:
        _user_favorites[user_id].append(author)
        return True
    return False


def remove_favorite_author(user_id: int, author: str) -> bool:
    """
    Удалить автора из избранного пользователя.
    
    Args:
        user_id: ID пользователя Telegram
        author: Имя автора
        
    Returns:
        True если автор удален, False если его не было в списке
    """
    if user_id in _user_favorites and author in _user_favorites[user_id]:
        _user_favorites[user_id].remove(author)
        return True
    return False

