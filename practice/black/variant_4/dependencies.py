from fastapi import Depends, Request
from typing import Optional
from services.cache_service import get_redis_client, get_from_cache, set_to_cache
from services.background_service import get_scheduler
import redis.asyncio as aioredis


async def get_cache_service():
    """
    Dependency для получения сервиса кеширования
    
    TODO: Реализовать функцию:
    1. Получить клиент Redis через get_redis_client()
    2. Вернуть словарь с функциями кеширования:
       {
           "get": get_from_cache,
           "set": set_to_cache,
           "client": redis_client
       }
    """
    pass


async def get_trace_id(request: Request) -> Optional[str]:
    """
    Dependency для получения trace_id из request.state
    
    TODO: Реализовать функцию:
    1. Получить trace_id из request.state.trace_id
    2. Вернуть trace_id (может быть None, если middleware не установил его)
    """
    pass


async def get_scheduler_dependency():
    """
    Dependency для получения планировщика задач
    
    TODO: Реализовать функцию:
    1. Получить планировщик через get_scheduler()
    2. Вернуть планировщик
    """
    pass

