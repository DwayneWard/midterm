import logging
from fastapi import FastAPI, Depends, BackgroundTasks, HTTPException, status
from fastapi.responses import JSONResponse
from typing import List, Optional
from contextlib import asynccontextmanager

from models import Order, OrderCreate, OrderUpdate
from storage import get_all_orders, get_order_by_id, create_order, update_order, delete_order
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
    title="Order Management API",
    description="API для управления заказами с кешированием и фоновыми задачами",
    lifespan=lifespan
)

# Подключение Middleware
# TODO: Добавить TraceMiddleware через app.add_middleware()


@app.get("/api/orders", response_model=List[Order])
async def get_orders(
    trace_id: Optional[str] = Depends(get_trace_id)
):
    """
    Получить все заказы (с кешированием)
    
    TODO: Реализовать функцию:
    1. Сформировать ключ кеша: cache_key = "orders:all"
    2. Попытаться получить данные из кеша через await get_from_cache(cache_key)
    3. Если данные в кеше есть, вернуть их
    4. Если данных нет:
       - Получить заказы через get_all_orders()
       - Сохранить в кеш через await set_to_cache(cache_key, orders)
       - Вернуть заказы
    5. Залогировать операцию с trace_id: logger.info(f"[{trace_id}] Retrieved {len(orders)} orders")
    """
    pass


@app.get("/api/orders/{order_id}", response_model=Order)
async def get_order(
    order_id: int,
    trace_id: Optional[str] = Depends(get_trace_id)
):
    """
    Получить заказ по ID (с кешированием)
    
    TODO: Реализовать функцию:
    1. Сформировать ключ кеша: cache_key = f"order:{order_id}"
    2. Попытаться получить данные из кеша через await get_from_cache(cache_key)
    3. Если данные в кеше есть, вернуть их
    4. Если данных нет:
       - Получить заказ через get_order_by_id(order_id)
       - Если заказ не найден, вызвать HTTPException со статусом 404
       - Сохранить в кеш через await set_to_cache(cache_key, order)
       - Вернуть заказ
    5. Залогировать операцию с trace_id: logger.info(f"[{trace_id}] Retrieved order {order_id}")
    """
    pass


@app.post("/api/orders", response_model=Order, status_code=status.HTTP_201_CREATED)
async def create_order_endpoint(
    order_data: OrderCreate,
    background_tasks: BackgroundTasks,
    trace_id: Optional[str] = Depends(get_trace_id)
):
    """
    Создать новый заказ
    
    TODO: Реализовать функцию:
    1. Создать заказ через create_order(order_data)
    2. Инвалидировать кеш списка заказов: await invalidate_cache_pattern("orders:*")
    3. Добавить фоновую задачу для логирования:
       background_tasks.add_task(log_order_creation, order.id, trace_id)
    4. Вернуть созданный заказ со статусом 201
    5. Залогировать операцию: logger.info(f"[{trace_id}] Created order {order.id}")
    """
    pass


@app.put("/api/orders/{order_id}", response_model=Order)
async def update_order_endpoint(
    order_id: int,
    order_data: OrderUpdate,
    trace_id: Optional[str] = Depends(get_trace_id)
):
    """
    Обновить заказ
    
    TODO: Реализовать функцию:
    1. Обновить заказ через update_order(order_id, order_data)
    2. Если заказ не найден, вызвать HTTPException со статусом 404
    3. Инвалидировать кеш для этого заказа: await invalidate_cache_pattern(f"order:{order_id}")
    4. Инвалидировать кеш списка заказов: await invalidate_cache_pattern("orders:*")
    5. Вернуть обновленный заказ
    6. Залогировать операцию: logger.info(f"[{trace_id}] Updated order {order_id}")
    """
    pass


@app.delete("/api/orders/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_order_endpoint(
    order_id: int,
    trace_id: Optional[str] = Depends(get_trace_id)
):
    """
    Удалить заказ
    
    TODO: Реализовать функцию:
    1. Удалить заказ через delete_order(order_id)
    2. Если заказ не найден (delete_order вернул False), вызвать HTTPException со статусом 404
    3. Инвалидировать кеш для этого заказа и списка заказов: await invalidate_cache_pattern("orders:*")
    4. Вернуть пустой ответ со статусом 204: return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
    5. Залогировать операцию: logger.info(f"[{trace_id}] Deleted order {order_id}")
    """
    pass


def log_order_creation(order_id: int, trace_id: Optional[str]):
    """
    Фоновая задача для логирования создания заказа
    
    TODO: Реализовать функцию:
    1. Залогировать: logger.info(f"[{trace_id}] Background task: Order {order_id} created")
    """
    pass

