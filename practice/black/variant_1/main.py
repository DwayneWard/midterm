import logging
from fastapi import FastAPI, Depends, BackgroundTasks, HTTPException, status
from fastapi.responses import JSONResponse
from typing import List, Optional
from contextlib import asynccontextmanager

from models import Task, TaskCreate, TaskUpdate
from storage import get_all_tasks, get_task_by_id, create_task, update_task, delete_task
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
    title="Task Management API",
    description="API для управления задачами с кешированием и фоновыми задачами",
    lifespan=lifespan
)

# Подключение Middleware
# TODO: Добавить TraceMiddleware через app.add_middleware()


@app.get("/api/tasks", response_model=List[Task])
async def get_tasks(
    trace_id: Optional[str] = Depends(get_trace_id)
):
    """
    Получить все задачи (с кешированием)
    
    TODO: Реализовать функцию:
    1. Сформировать ключ кеша: cache_key = "tasks:all"
    2. Попытаться получить данные из кеша через await get_from_cache(cache_key)
    3. Если данные в кеше есть, вернуть их
    4. Если данных нет:
       - Получить задачи через get_all_tasks()
       - Сохранить в кеш через await set_to_cache(cache_key, tasks)
       - Вернуть задачи
    5. Залогировать операцию с trace_id: logger.info(f"[{trace_id}] Retrieved {len(tasks)} tasks")
    """
    pass


@app.get("/api/tasks/{task_id}", response_model=Task)
async def get_task(
    task_id: int,
    trace_id: Optional[str] = Depends(get_trace_id)
):
    """
    Получить задачу по ID (с кешированием)
    
    TODO: Реализовать функцию:
    1. Сформировать ключ кеша: cache_key = f"task:{task_id}"
    2. Попытаться получить данные из кеша через await get_from_cache(cache_key)
    3. Если данные в кеше есть, вернуть их
    4. Если данных нет:
       - Получить задачу через get_task_by_id(task_id)
       - Если задача не найдена, вызвать HTTPException со статусом 404
       - Сохранить в кеш через await set_to_cache(cache_key, task)
       - Вернуть задачу
    5. Залогировать операцию с trace_id: logger.info(f"[{trace_id}] Retrieved task {task_id}")
    """
    pass


@app.post("/api/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
async def create_task_endpoint(
    task_data: TaskCreate,
    background_tasks: BackgroundTasks,
    trace_id: Optional[str] = Depends(get_trace_id)
):
    """
    Создать новую задачу
    
    TODO: Реализовать функцию:
    1. Создать задачу через create_task(task_data)
    2. Инвалидировать кеш списка задач: await invalidate_cache_pattern("tasks:*")
    3. Добавить фоновую задачу для логирования:
       background_tasks.add_task(log_task_creation, task.id, trace_id)
    4. Вернуть созданную задачу со статусом 201
    5. Залогировать операцию: logger.info(f"[{trace_id}] Created task {task.id}")
    """
    pass


@app.put("/api/tasks/{task_id}", response_model=Task)
async def update_task_endpoint(
    task_id: int,
    task_data: TaskUpdate,
    trace_id: Optional[str] = Depends(get_trace_id)
):
    """
    Обновить задачу
    
    TODO: Реализовать функцию:
    1. Обновить задачу через update_task(task_id, task_data)
    2. Если задача не найдена, вызвать HTTPException со статусом 404
    3. Инвалидировать кеш для этой задачи: await invalidate_cache_pattern(f"task:{task_id}")
    4. Инвалидировать кеш списка задач: await invalidate_cache_pattern("tasks:*")
    5. Вернуть обновленную задачу
    6. Залогировать операцию: logger.info(f"[{trace_id}] Updated task {task_id}")
    """
    pass


@app.delete("/api/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task_endpoint(
    task_id: int,
    trace_id: Optional[str] = Depends(get_trace_id)
):
    """
    Удалить задачу
    
    TODO: Реализовать функцию:
    1. Удалить задачу через delete_task(task_id)
    2. Если задача не найдена (delete_task вернул False), вызвать HTTPException со статусом 404
    3. Инвалидировать кеш для этой задачи и списка задач: await invalidate_cache_pattern("tasks:*")
    4. Вернуть пустой ответ со статусом 204: return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
    5. Залогировать операцию: logger.info(f"[{trace_id}] Deleted task {task_id}")
    """
    pass


def log_task_creation(task_id: int, trace_id: Optional[str]):
    """
    Фоновая задача для логирования создания задачи
    
    TODO: Реализовать функцию:
    1. Залогировать: logger.info(f"[{trace_id}] Background task: Task {task_id} created")
    """
    pass

