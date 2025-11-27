import json
import logging
from typing import Optional, Any
import redis.asyncio as aioredis
from config import REDIS_HOST, REDIS_PORT, REDIS_DB, CACHE_TTL

logger = logging.getLogger(__name__)

# Глобальное подключение к Redis
redis_client: Optional[aioredis.Redis] = None


async def get_redis_client() -> aioredis.Redis:
    """
    Получить клиент Redis (singleton)
    
    Returns:
        Клиент Redis
        
    TODO: Реализовать функцию:
    1. Использовать глобальную переменную redis_client
    2. Если redis_client is None, создать новое подключение:
       redis_client = aioredis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
    3. Вернуть redis_client
    """
    global redis_client
    pass


async def close_redis_client():
    """
    Закрыть подключение к Redis
    
    TODO: Реализовать функцию:
    1. Использовать глобальную переменную redis_client
    2. Если redis_client не None, закрыть подключение: await redis_client.close()
    3. Установить redis_client = None
    """
    global redis_client
    pass


async def get_from_cache(key: str) -> Optional[Any]:
    """
    Получить значение из кеша
    
    Args:
        key: Ключ кеша
        
    Returns:
        Десериализованное значение или None, если ключ не найден
        
    TODO: Реализовать функцию:
    1. Получить клиент Redis через get_redis_client()
    2. Получить значение по ключу: value = await client.get(key)
    3. Если value is None, вернуть None
    4. Декодировать bytes в строку: value.decode('utf-8')
    5. Десериализовать JSON: json.loads(value)
    6. Вернуть десериализованное значение
    7. Обработать возможные исключения (redis.RedisError, json.JSONDecodeError) и вернуть None
    """
    pass


async def set_to_cache(key: str, value: Any, ttl: Optional[int] = None) -> bool:
    """
    Сохранить значение в кеш
    
    Args:
        key: Ключ кеша
        value: Значение для сохранения (будет сериализовано в JSON)
        ttl: Время жизни кеша в секундах (если None, используется CACHE_TTL)
        
    Returns:
        True, если успешно сохранено, False в случае ошибки
        
    TODO: Реализовать функцию:
    1. Получить клиент Redis через get_redis_client()
    2. Сериализовать value в JSON: json.dumps(value)
    3. Если ttl is None, использовать CACHE_TTL из config
    4. Сохранить в Redis с TTL: await client.setex(key, ttl, json_value)
    5. Вернуть True
    6. Обработать возможные исключения (redis.RedisError, TypeError) и вернуть False
    """
    pass


async def delete_from_cache(key: str) -> bool:
    """
    Удалить значение из кеша
    
    Args:
        key: Ключ кеша
        
    Returns:
        True, если успешно удалено, False в случае ошибки
        
    TODO: Реализовать функцию:
    1. Получить клиент Redis через get_redis_client()
    2. Удалить ключ: await client.delete(key)
    3. Вернуть True
    4. Обработать возможные исключения (redis.RedisError) и вернуть False
    """
    pass


async def invalidate_cache_pattern(pattern: str) -> int:
    """
    Инвалидировать кеш по паттерну (удалить все ключи, соответствующие паттерну)
    
    Args:
        pattern: Паттерн для поиска ключей (например, "task:*")
        
    Returns:
        Количество удаленных ключей
        
    TODO: Реализовать функцию:
    1. Получить клиент Redis через get_redis_client()
    2. Найти все ключи по паттерну: keys = await client.keys(pattern)
    3. Если keys пустой список, вернуть 0
    4. Удалить все найденные ключи: await client.delete(*keys)
    5. Вернуть количество удаленных ключей
    6. Обработать возможные исключения (redis.RedisError) и вернуть 0
    """
    pass

