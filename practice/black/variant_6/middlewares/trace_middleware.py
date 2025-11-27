import uuid
import logging
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

logger = logging.getLogger(__name__)


class TraceMiddleware(BaseHTTPMiddleware):
    """
    Middleware для присвоения каждому запросу уникального UUID и логирования
    
    TODO: Реализовать метод dispatch:
    1. Сгенерировать уникальный UUID используя uuid.uuid4()
    2. Преобразовать UUID в строку: str(uuid.uuid4())
    3. Сохранить trace_id в request.state.trace_id
    4. Залогировать входящий запрос с trace_id:
       logger.info(f"[{trace_id}] {request.method} {request.url.path}")
    5. Вызвать call_next(request) для передачи управления дальше
    6. Получить response
    7. Добавить trace_id в заголовок ответа: response.headers["X-Trace-ID"] = trace_id
    8. Залогировать исходящий ответ с trace_id:
       logger.info(f"[{trace_id}] Response: {response.status_code}")
    9. Вернуть response
    """
    async def dispatch(self, request: Request, call_next):
        pass

