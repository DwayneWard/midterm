from typing import List, Optional
from datetime import datetime, date
from models import Event, EventCreate, EventUpdate


# Хранилище событий в памяти
events_db: List[Event] = [
    Event(id=1, title="Конференция по Python", description="Ежегодная конференция", event_date=date(2024, 12, 15), location="Москва", category="conference", created_at=datetime.now()),
    Event(id=2, title="Воркшоп по FastAPI", description="Практический воркшоп", event_date=date(2024, 11, 20), location="Санкт-Петербург", category="workshop", created_at=datetime.now()),
    Event(id=3, title="Встреча команды", description="Еженедельная встреча", event_date=date(2024, 10, 10), location="Онлайн", category="meeting", created_at=datetime.now()),
]


def get_all_events() -> List[Event]:
    """
    Получить все события
    
    Returns:
        Список всех событий
    """
    return events_db


def get_event_by_id(event_id: int) -> Optional[Event]:
    """
    Получить событие по ID
    
    Args:
        event_id: ID события
        
    Returns:
        Событие или None, если событие не найдено
        
    TODO: Реализовать функцию:
    1. Пройтись по списку events_db
    2. Найти событие с указанным id
    3. Вернуть событие или None, если не найдено
    """
    pass


def create_event(event_data: EventCreate) -> Event:
    """
    Создать новое событие
    
    Args:
        event_data: Данные нового события (без id и created_at)
        
    Returns:
        Созданное событие с присвоенным id и created_at
        
    TODO: Реализовать функцию:
    1. Определить новый id (максимальный id в events_db + 1, или 1 если список пуст)
    2. Создать объект Event с новым id, created_at=datetime.now() и данными из event_data
    3. Добавить событие в events_db
    4. Вернуть созданное событие
    """
    pass


def update_event(event_id: int, event_data: EventUpdate) -> Optional[Event]:
    """
    Обновить событие
    
    Args:
        event_id: ID события для обновления
        event_data: Новые данные события
        
    Returns:
        Обновленное событие или None, если событие не найдено
        
    TODO: Реализовать функцию:
    1. Найти событие с указанным id в events_db
    2. Если событие не найдено, вернуть None
    3. Обновить поля события данными из event_data (только те поля, которые не None)
       Используй: event.field = event_data.field if event_data.field is not None else event.field
    4. Вернуть обновленное событие
    """
    pass


def delete_event(event_id: int) -> bool:
    """
    Удалить событие
    
    Args:
        event_id: ID события для удаления
        
    Returns:
        True, если событие удалено, False если не найдено
        
    TODO: Реализовать функцию:
    1. Найти событие с указанным id в events_db
    2. Если событие не найдено, вернуть False
    3. Удалить событие из events_db
    4. Вернуть True
    """
    pass

