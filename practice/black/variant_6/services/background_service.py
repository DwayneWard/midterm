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


async def cleanup_unpublished_articles():
    """
    Фоновая задача для очистки неопубликованных статей
    
    TODO: Реализовать функцию:
    1. Импортировать storage: from storage import get_all_articles, delete_article
    2. Получить все статьи через get_all_articles()
    3. Найти статьи, которые:
       - published == False
       - created_at старше 90 дней (используй datetime.now() - timedelta(days=90))
    4. Удалить найденные статьи через delete_article(article.id)
    5. Залогировать результат: logger.info(f"Cleaned up {count} unpublished articles")
    6. Обработать возможные исключения и залогировать ошибку
    """
    pass


def setup_periodic_tasks():
    """
    Настроить периодические задачи
    
    TODO: Реализовать функцию:
    1. Получить планировщик через get_scheduler()
    2. Добавить периодическую задачу cleanup_unpublished_articles:
       - Использовать IntervalTrigger(hours=24) для запуска раз в сутки
       - Функция: cleanup_unpublished_articles
       - ID задачи: "cleanup_unpublished_articles"
    3. Залогировать: logger.info("Periodic tasks configured")
    """
    pass
