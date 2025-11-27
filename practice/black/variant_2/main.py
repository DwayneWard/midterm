import logging
from fastapi import FastAPI, Depends, BackgroundTasks, HTTPException, status
from fastapi.responses import JSONResponse
from typing import List, Optional
from contextlib import asynccontextmanager

from models import Product, ProductCreate, ProductUpdate
from storage import get_all_products, get_product_by_id, create_product, update_product, delete_product
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
    title="Product Management API",
    description="API для управления продуктами с кешированием и фоновыми задачами",
    lifespan=lifespan
)

# Подключение Middleware
# TODO: Добавить TraceMiddleware через app.add_middleware()


@app.get("/api/products", response_model=List[Product])
async def get_products(
    trace_id: Optional[str] = Depends(get_trace_id)
):
    """
    Получить все продукты (с кешированием)
    
    TODO: Реализовать функцию:
    1. Сформировать ключ кеша: cache_key = "products:all"
    2. Попытаться получить данные из кеша через await get_from_cache(cache_key)
    3. Если данные в кеше есть, вернуть их
    4. Если данных нет:
       - Получить продукты через get_all_products()
       - Сохранить в кеш через await set_to_cache(cache_key, products)
       - Вернуть продукты
    5. Залогировать операцию с trace_id: logger.info(f"[{trace_id}] Retrieved {len(products)} products")
    """
    pass


@app.get("/api/products/{product_id}", response_model=Product)
async def get_product(
    product_id: int,
    trace_id: Optional[str] = Depends(get_trace_id)
):
    """
    Получить продукт по ID (с кешированием)
    
    TODO: Реализовать функцию:
    1. Сформировать ключ кеша: cache_key = f"product:{product_id}"
    2. Попытаться получить данные из кеша через await get_from_cache(cache_key)
    3. Если данные в кеше есть, вернуть их
    4. Если данных нет:
       - Получить продукт через get_product_by_id(product_id)
       - Если продукт не найден, вызвать HTTPException со статусом 404
       - Сохранить в кеш через await set_to_cache(cache_key, product)
       - Вернуть продукт
    5. Залогировать операцию с trace_id: logger.info(f"[{trace_id}] Retrieved product {product_id}")
    """
    pass


@app.post("/api/products", response_model=Product, status_code=status.HTTP_201_CREATED)
async def create_product_endpoint(
    product_data: ProductCreate,
    background_tasks: BackgroundTasks,
    trace_id: Optional[str] = Depends(get_trace_id)
):
    """
    Создать новый продукт
    
    TODO: Реализовать функцию:
    1. Создать продукт через create_product(product_data)
    2. Инвалидировать кеш списка продуктов: await invalidate_cache_pattern("products:*")
    3. Добавить фоновую задачу для логирования:
       background_tasks.add_task(log_product_creation, product.id, trace_id)
    4. Вернуть созданный продукт со статусом 201
    5. Залогировать операцию: logger.info(f"[{trace_id}] Created product {product.id}")
    """
    pass


@app.put("/api/products/{product_id}", response_model=Product)
async def update_product_endpoint(
    product_id: int,
    product_data: ProductUpdate,
    trace_id: Optional[str] = Depends(get_trace_id)
):
    """
    Обновить продукт
    
    TODO: Реализовать функцию:
    1. Обновить продукт через update_product(product_id, product_data)
    2. Если продукт не найден, вызвать HTTPException со статусом 404
    3. Инвалидировать кеш для этого продукта: await invalidate_cache_pattern(f"product:{product_id}")
    4. Инвалидировать кеш списка продуктов: await invalidate_cache_pattern("products:*")
    5. Вернуть обновленный продукт
    6. Залогировать операцию: logger.info(f"[{trace_id}] Updated product {product_id}")
    """
    pass


@app.delete("/api/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product_endpoint(
    product_id: int,
    trace_id: Optional[str] = Depends(get_trace_id)
):
    """
    Удалить продукт
    
    TODO: Реализовать функцию:
    1. Удалить продукт через delete_product(product_id)
    2. Если продукт не найден (delete_product вернул False), вызвать HTTPException со статусом 404
    3. Инвалидировать кеш для этого продукта и списка продуктов: await invalidate_cache_pattern("products:*")
    4. Вернуть пустой ответ со статусом 204: return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
    5. Залогировать операцию: logger.info(f"[{trace_id}] Deleted product {product_id}")
    """
    pass


def log_product_creation(product_id: int, trace_id: Optional[str]):
    """
    Фоновая задача для логирования создания продукта
    
    TODO: Реализовать функцию:
    1. Залогировать: logger.info(f"[{trace_id}] Background task: Product {product_id} created")
    """
    pass
