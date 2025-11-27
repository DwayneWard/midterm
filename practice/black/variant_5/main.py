import logging
from fastapi import FastAPI, Depends, BackgroundTasks, HTTPException, status
from fastapi.responses import JSONResponse
from typing import List, Optional
from contextlib import asynccontextmanager

from models import Event, EventCreate, EventUpdate
from storage import get_all_events, get_event_by_id, create_event, update_event, delete_event
from middlewares.trace_middleware import TraceMiddleware
from services.cache_service import close_redis_client, get_from_cache, set_to_cache, invalidate_cache_pattern
from services.background_service import setup_periodic_tasks
from dependencies import get_cache_service, get_trace_id

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Управление жизненным циклом приложения
    
    TODO: Реализовать функцию:
    1. При запуске (yield до):
       - Вызвать setup_periodic_tasks() для настройки периодических задач
       - Залогировать: logger.info("Application started")
    2. При остановке (после yield):
       - Вызвать close_redis_client() для закрытия подключения к Redis
       - Залогировать: logger.info("Application stopped")
    """
    # Startup
    yield
    # Shutdown


# Создание экземпляра FastAPI приложения
app = FastAPI(
    title="Event Management API",
    description="API для управления событиями с кешированием и фоновыми задачами",
    lifespan=lifespan
)

# Подключение Middleware
# TODO: Добавить TraceMiddleware через app.add_middleware()


@app.get("/api/events", response_model=List[Event])
async def get_events(
    trace_id: Optional[str] = Depends(get_trace_id)
):
    """
    Получить все события (с кешированием)
    
    TODO: Реализовать функцию:
    1. Сформировать ключ кеша: cache_key = "events:all"
    2. Попытаться получить данные из кеша через await get_from_cache(cache_key)
    3. Если данные в кеше есть, вернуть их
    4. Если данных нет:
       - Получить события через get_all_events()
       - Сохранить в кеш через await set_to_cache(cache_key, events)
       - Вернуть события
    5. Залогировать операцию с trace_id: logger.info(f"[{trace_id}] Retrieved {len(events)} events")
    """
    pass


@app.get("/api/events/{event_id}", response_model=Event)
async def get_event(
    event_id: int,
    trace_id: Optional[str] = Depends(get_trace_id)
):
    """
    Получить событие по ID (с кешированием)
    
    TODO: Реализовать функцию:
    1. Сформировать ключ кеша: cache_key = f"event:{event_id}"
    2. Попытаться получить данные из кеша через await get_from_cache(cache_key)
    3. Если данные в кеше есть, вернуть их
    4. Если данных нет:
       - Получить событие через get_event_by_id(event_id)
       - Если событие не найдено, вызвать HTTPException со статусом 404
       - Сохранить в кеш через await set_to_cache(cache_key, event)
       - Вернуть событие
    5. Залогировать операцию с trace_id: logger.info(f"[{trace_id}] Retrieved event {event_id}")
    """
    pass


@app.post("/api/events", response_model=Event, status_code=status.HTTP_201_CREATED)
async def create_event_endpoint(
    event_data: EventCreate,
    background_tasks: BackgroundTasks,
    trace_id: Optional[str] = Depends(get_trace_id)
):
    """
    Создать новое событие
    
    TODO: Реализовать функцию:
    1. Создать событие через create_event(event_data)
    2. Инвалидировать кеш списка событий: await invalidate_cache_pattern("events:*")
    3. Добавить фоновую задачу для логирования:
       background_tasks.add_task(log_event_creation, event.id, trace_id)
    4. Вернуть созданное событие со статусом 201
    5. Залогировать операцию: logger.info(f"[{trace_id}] Created event {event.id}")
    """
    pass


@app.put("/api/events/{event_id}", response_model=Event)
async def update_event_endpoint(
    event_id: int,
    event_data: EventUpdate,
    trace_id: Optional[str] = Depends(get_trace_id)
):
    """
    Обновить событие
    
    TODO: Реализовать функцию:
    1. Обновить событие через update_event(event_id, event_data)
    2. Если событие не найдено, вызвать HTTPException со статусом 404
    3. Инвалидировать кеш для этого события: await invalidate_cache_pattern(f"event:{event_id}")
    4. Инвалидировать кеш списка событий: await invalidate_cache_pattern("events:*")
    5. Вернуть обновленное событие
    6. Залогировать операцию: logger.info(f"[{trace_id}] Updated event {event_id}")
    """
    pass


@app.delete("/api/events/{event_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_event_endpoint(
    event_id: int,
    trace_id: Optional[str] = Depends(get_trace_id)
):
    """
    Удалить событие
    
    TODO: Реализовать функцию:
    1. Удалить событие через delete_event(event_id)
    2. Если событие не найдено (delete_event вернул False), вызвать HTTPException со статусом 404
    3. Инвалидировать кеш для этого события и списка событий: await invalidate_cache_pattern("events:*")
    4. Вернуть пустой ответ со статусом 204: return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
    5. Залогировать операцию: logger.info(f"[{trace_id}] Deleted event {event_id}")
    """
    pass


def log_event_creation(event_id: int, trace_id: Optional[str]):
    """
    Фоновая задача для логирования создания события
    
    TODO: Реализовать функцию:
    1. Залогировать: logger.info(f"[{trace_id}] Background task: Event {event_id} created")
    """
    pass

