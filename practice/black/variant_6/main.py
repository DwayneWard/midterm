import logging
from fastapi import FastAPI, Depends, BackgroundTasks, HTTPException, status
from fastapi.responses import JSONResponse
from typing import List, Optional
from contextlib import asynccontextmanager

from models import Article, ArticleCreate, ArticleUpdate
from storage import get_all_articles, get_article_by_id, create_article, update_article, delete_article
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
    title="Article Management API",
    description="API для управления статьями с кешированием и фоновыми задачами",
    lifespan=lifespan
)

# Подключение Middleware
# TODO: Добавить TraceMiddleware через app.add_middleware()


@app.get("/api/articles", response_model=List[Article])
async def get_articles(
    trace_id: Optional[str] = Depends(get_trace_id)
):
    """
    Получить все статьи (с кешированием)
    
    TODO: Реализовать функцию:
    1. Сформировать ключ кеша: cache_key = "articles:all"
    2. Попытаться получить данные из кеша через await get_from_cache(cache_key)
    3. Если данные в кеше есть, вернуть их
    4. Если данных нет:
       - Получить статьи через get_all_articles()
       - Сохранить в кеш через await set_to_cache(cache_key, articles)
       - Вернуть статьи
    5. Залогировать операцию с trace_id: logger.info(f"[{trace_id}] Retrieved {len(articles)} articles")
    """
    pass


@app.get("/api/articles/{article_id}", response_model=Article)
async def get_article(
    article_id: int,
    trace_id: Optional[str] = Depends(get_trace_id)
):
    """
    Получить статью по ID (с кешированием)
    
    TODO: Реализовать функцию:
    1. Сформировать ключ кеша: cache_key = f"article:{article_id}"
    2. Попытаться получить данные из кеша через await get_from_cache(cache_key)
    3. Если данные в кеше есть, вернуть их
    4. Если данных нет:
       - Получить статью через get_article_by_id(article_id)
       - Если статья не найдена, вызвать HTTPException со статусом 404
       - Сохранить в кеш через await set_to_cache(cache_key, article)
       - Вернуть статью
    5. Залогировать операцию с trace_id: logger.info(f"[{trace_id}] Retrieved article {article_id}")
    """
    pass


@app.post("/api/articles", response_model=Article, status_code=status.HTTP_201_CREATED)
async def create_article_endpoint(
    article_data: ArticleCreate,
    background_tasks: BackgroundTasks,
    trace_id: Optional[str] = Depends(get_trace_id)
):
    """
    Создать новую статью
    
    TODO: Реализовать функцию:
    1. Создать статью через create_article(article_data)
    2. Инвалидировать кеш списка статей: await invalidate_cache_pattern("articles:*")
    3. Добавить фоновую задачу для логирования:
       background_tasks.add_task(log_article_creation, article.id, trace_id)
    4. Вернуть созданную статью со статусом 201
    5. Залогировать операцию: logger.info(f"[{trace_id}] Created article {article.id}")
    """
    pass


@app.put("/api/articles/{article_id}", response_model=Article)
async def update_article_endpoint(
    article_id: int,
    article_data: ArticleUpdate,
    trace_id: Optional[str] = Depends(get_trace_id)
):
    """
    Обновить статью
    
    TODO: Реализовать функцию:
    1. Обновить статью через update_article(article_id, article_data)
    2. Если статья не найдена, вызвать HTTPException со статусом 404
    3. Инвалидировать кеш для этой статьи: await invalidate_cache_pattern(f"article:{article_id}")
    4. Инвалидировать кеш списка статей: await invalidate_cache_pattern("articles:*")
    5. Вернуть обновленную статью
    6. Залогировать операцию: logger.info(f"[{trace_id}] Updated article {article_id}")
    """
    pass


@app.delete("/api/articles/{article_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_article_endpoint(
    article_id: int,
    trace_id: Optional[str] = Depends(get_trace_id)
):
    """
    Удалить статью
    
    TODO: Реализовать функцию:
    1. Удалить статью через delete_article(article_id)
    2. Если статья не найдена (delete_article вернул False), вызвать HTTPException со статусом 404
    3. Инвалидировать кеш для этой статьи и списка статей: await invalidate_cache_pattern("articles:*")
    4. Вернуть пустой ответ со статусом 204: return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
    5. Залогировать операцию: logger.info(f"[{trace_id}] Deleted article {article_id}")
    """
    pass


def log_article_creation(article_id: int, trace_id: Optional[str]):
    """
    Фоновая задача для логирования создания статьи
    
    TODO: Реализовать функцию:
    1. Залогировать: logger.info(f"[{trace_id}] Background task: Article {article_id} created")
    """
    pass

