import logging
from datetime import datetime, timedelta, date
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger

logger = logging.getLogger(__name__)

# Глобальный планировщик задач
scheduler: AsyncIOScheduler = None


def get_scheduler() -> AsyncIOScheduler:
    """
    Получить планировщик задач (singleton)
    
    Returns:
        Планировщик задач
        
    TODO: Реализовать функцию:
    1. Использовать глобальную переменную scheduler
    2. Если scheduler is None, создать новый:
       scheduler = AsyncIOScheduler()
       scheduler.start()
    3. Вернуть scheduler
    """
    global scheduler
    pass


async def cleanup_past_events():
    """
    Фоновая задача для очистки прошедших событий
    
    TODO: Реализовать функцию:
    1. Импортировать storage: from storage import get_all_events, delete_event
    2. Получить все события через get_all_events()
    3. Найти события, которые:
       - event_date в прошлом (event_date < date.today())
       - event_date старше 30 дней (event_date < date.today() - timedelta(days=30))
    4. Удалить найденные события через delete_event(event.id)
    5. Залогировать результат: logger.info(f"Cleaned up {count} past events")
    6. Обработать возможные исключения и залогировать ошибку
    """
    pass


def setup_periodic_tasks():
    """
    Настроить периодические задачи
    
    TODO: Реализовать функцию:
    1. Получить планировщик через get_scheduler()
    2. Добавить периодическую задачу cleanup_past_events:
       - Использовать IntervalTrigger(hours=24) для запуска раз в сутки
       - Функция: cleanup_past_events
       - ID задачи: "cleanup_past_events"
    3. Залогировать: logger.info("Periodic tasks configured")
    """
    pass
