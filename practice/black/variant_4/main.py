import logging
from fastapi import FastAPI, Depends, BackgroundTasks, HTTPException, status
from fastapi.responses import JSONResponse
from typing import List, Optional
from contextlib import asynccontextmanager

from models import User, UserCreate, UserUpdate
from storage import get_all_users, get_user_by_id, create_user, update_user, delete_user
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
    title="User Management API",
    description="API для управления пользователями с кешированием и фоновыми задачами",
    lifespan=lifespan
)

# Подключение Middleware
# TODO: Добавить TraceMiddleware через app.add_middleware()


@app.get("/api/users", response_model=List[User])
async def get_users(
    trace_id: Optional[str] = Depends(get_trace_id)
):
    """
    Получить всех пользователей (с кешированием)
    
    TODO: Реализовать функцию:
    1. Сформировать ключ кеша: cache_key = "users:all"
    2. Попытаться получить данные из кеша через await get_from_cache(cache_key)
    3. Если данные в кеше есть, вернуть их
    4. Если данных нет:
       - Получить пользователей через get_all_users()
       - Сохранить в кеш через await set_to_cache(cache_key, users)
       - Вернуть пользователей
    5. Залогировать операцию с trace_id: logger.info(f"[{trace_id}] Retrieved {len(users)} users")
    """
    pass


@app.get("/api/users/{user_id}", response_model=User)
async def get_user(
    user_id: int,
    trace_id: Optional[str] = Depends(get_trace_id)
):
    """
    Получить пользователя по ID (с кешированием)
    
    TODO: Реализовать функцию:
    1. Сформировать ключ кеша: cache_key = f"user:{user_id}"
    2. Попытаться получить данные из кеша через await get_from_cache(cache_key)
    3. Если данные в кеше есть, вернуть их
    4. Если данных нет:
       - Получить пользователя через get_user_by_id(user_id)
       - Если пользователь не найден, вызвать HTTPException со статусом 404
       - Сохранить в кеш через await set_to_cache(cache_key, user)
       - Вернуть пользователя
    5. Залогировать операцию с trace_id: logger.info(f"[{trace_id}] Retrieved user {user_id}")
    """
    pass


@app.post("/api/users", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user_endpoint(
    user_data: UserCreate,
    background_tasks: BackgroundTasks,
    trace_id: Optional[str] = Depends(get_trace_id)
):
    """
    Создать нового пользователя
    
    TODO: Реализовать функцию:
    1. Создать пользователя через create_user(user_data)
    2. Инвалидировать кеш списка пользователей: await invalidate_cache_pattern("users:*")
    3. Добавить фоновую задачу для логирования:
       background_tasks.add_task(log_user_creation, user.id, trace_id)
    4. Вернуть созданного пользователя со статусом 201
    5. Залогировать операцию: logger.info(f"[{trace_id}] Created user {user.id}")
    """
    pass


@app.put("/api/users/{user_id}", response_model=User)
async def update_user_endpoint(
    user_id: int,
    user_data: UserUpdate,
    trace_id: Optional[str] = Depends(get_trace_id)
):
    """
    Обновить пользователя
    
    TODO: Реализовать функцию:
    1. Обновить пользователя через update_user(user_id, user_data)
    2. Если пользователь не найден, вызвать HTTPException со статусом 404
    3. Инвалидировать кеш для этого пользователя: await invalidate_cache_pattern(f"user:{user_id}")
    4. Инвалидировать кеш списка пользователей: await invalidate_cache_pattern("users:*")
    5. Вернуть обновленного пользователя
    6. Залогировать операцию: logger.info(f"[{trace_id}] Updated user {user_id}")
    """
    pass


@app.delete("/api/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user_endpoint(
    user_id: int,
    trace_id: Optional[str] = Depends(get_trace_id)
):
    """
    Удалить пользователя
    
    TODO: Реализовать функция:
    1. Удалить пользователя через delete_user(user_id)
    2. Если пользователь не найден (delete_user вернул False), вызвать HTTPException со статусом 404
    3. Инвалидировать кеш для этого пользователя и списка пользователей: await invalidate_cache_pattern("users:*")
    4. Вернуть пустой ответ со статусом 204: return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
    5. Залогировать операцию: logger.info(f"[{trace_id}] Deleted user {user_id}")
    """
    pass


def log_user_creation(user_id: int, trace_id: Optional[str]):
    """
    Фоновая задача для логирования создания пользователя
    
    TODO: Реализовать функцию:
    1. Залогировать: logger.info(f"[{trace_id}] Background task: User {user_id} created")
    """
    pass

