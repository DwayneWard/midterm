import logging
from datetime import datetime, timedelta
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


async def cleanup_inactive_users():
    """
    Фоновая задача для очистки неактивных пользователей
    
    TODO: Реализовать функцию:
    1. Импортировать storage: from storage import get_all_users, delete_user
    2. Получить всех пользователей через get_all_users()
    3. Найти пользователей, которые:
       - is_active == False
       - created_at старше 90 дней (используй datetime.now() - timedelta(days=90))
    4. Удалить найденных пользователей через delete_user(user.id)
    5. Залогировать результат: logger.info(f"Cleaned up {count} inactive users")
    6. Обработать возможные исключения и залогировать ошибку
    """
    pass


def setup_periodic_tasks():
    """
    Настроить периодические задачи
    
    TODO: Реализовать функцию:
    1. Получить планировщик через get_scheduler()
    2. Добавить периодическую задачу cleanup_inactive_users:
       - Использовать IntervalTrigger(hours=24) для запуска раз в сутки
       - Функция: cleanup_inactive_users
       - ID задачи: "cleanup_inactive_users"
    3. Залогировать: logger.info("Periodic tasks configured")
    """
    pass
