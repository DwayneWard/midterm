from typing import List, Dict

# Временное хранилище
_user_favorites: Dict[int, List[int]] = {}


def get_user_favorites(user_id: int) -> List[int]:
    """
    Получить список избранных ID задач пользователя.
    
    Args:
        user_id: ID пользователя Telegram
        
    Returns:
        Список ID задач
    """
    return _user_favorites.get(user_id, [])


def add_favorite_task(user_id: int, task_id: int) -> bool:
    """
    Добавить задачу в избранное пользователя.
    
    Args:
        user_id: ID пользователя Telegram
        task_id: ID задачи
        
    Returns:
        True если задача добавлена, False если уже была в списке
    """
    if user_id not in _user_favorites:
        _user_favorites[user_id] = []
    
    if task_id not in _user_favorites[user_id]:
        _user_favorites[user_id].append(task_id)
        return True
    return False


def remove_favorite_task(user_id: int, task_id: int) -> bool:
    """
    Удалить задачу из избранного пользователя.
    
    Args:
        user_id: ID пользователя Telegram
        task_id: ID задачи
        
    Returns:
        True если задача удалена, False если её не было в списке
    """
    if user_id in _user_favorites and task_id in _user_favorites[user_id]:
        _user_favorites[user_id].remove(task_id)
        return True
    return False

