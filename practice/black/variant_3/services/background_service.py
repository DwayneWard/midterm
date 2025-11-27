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


async def cleanup_old_orders():
    """
    Фоновая задача для очистки старых отмененных заказов
    
    TODO: Реализовать функцию:
    1. Импортировать storage: from storage import get_all_orders, delete_order
    2. Получить все заказы через get_all_orders()
    3. Найти заказы, которые:
       - status == "cancelled"
       - created_at старше 30 дней (используй datetime.now() - timedelta(days=30))
    4. Удалить найденные заказы через delete_order(order.id)
    5. Залогировать результат: logger.info(f"Cleaned up {count} old orders")
    6. Обработать возможные исключения и залогировать ошибку
    """
    pass


def setup_periodic_tasks():
    """
    Настроить периодические задачи
    
    TODO: Реализовать функцию:
    1. Получить планировщик через get_scheduler()
    2. Добавить периодическую задачу cleanup_old_orders:
       - Использовать IntervalTrigger(hours=24) для запуска раз в сутки
       - Функция: cleanup_old_orders
       - ID задачи: "cleanup_old_orders"
    3. Залогировать: logger.info("Periodic tasks configured")
    """
    pass
