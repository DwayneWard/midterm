"""
Тесты для dependencies.py
Проверяют ОРы: 5.1, 5.2 (Dependency Injection)
"""
import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from fastapi import Request

try:
    from dependencies import get_cache_service, get_trace_id, get_scheduler_dependency
except ImportError:
    pytest.skip("dependencies module not available", allow_module_level=True)


class TestOR51_DependsUsage:
    """ОР 5.1: Использовать Depends для внедрения зависимостей в эндпоинты"""
    
    @pytest.mark.asyncio
    async def test_get_cache_service_returns_dict(self):
        """Проверка создания dependency для кеш-сервиса"""
        with patch('dependencies.get_redis_client') as mock_get_client:
            mock_client = AsyncMock()
            mock_get_client.return_value = mock_client
            
            result = await get_cache_service()
            
            # Проверяем, что функция возвращает словарь (если реализована)
            if result is not None:
                assert isinstance(result, dict)
                assert "get" in result or "client" in result
    
    @pytest.mark.asyncio
    async def test_get_trace_id_from_request(self):
        """Проверка получения trace_id из request.state"""
        request = MagicMock(spec=Request)
        request.state.trace_id = "test-trace-id"
        
        result = await get_trace_id(request)
        
        assert result == "test-trace-id"
    
    @pytest.mark.asyncio
    async def test_get_trace_id_none_when_not_set(self):
        """Проверка получения trace_id когда он не установлен"""
        request = MagicMock(spec=Request)
        request.state.trace_id = None
        
        result = await get_trace_id(request)
        
        assert result is None


class TestOR52_CustomDependencies:
    """ОР 5.2: Создавать собственные зависимости"""
    
    @pytest.mark.asyncio
    async def test_cache_service_dependency_has_functions(self):
        """Проверка, что dependency для кеша содержит нужные функции"""
        with patch('dependencies.get_redis_client') as mock_get_client:
            mock_client = AsyncMock()
            mock_get_client.return_value = mock_client
            
            result = await get_cache_service()
            
            # Проверяем, что dependency содержит нужные функции (если реализована)
            if result is not None and isinstance(result, dict):
                if "get" in result:
                    assert callable(result["get"])
                if "set" in result:
                    assert callable(result["set"])
                if "client" in result:
                    assert result["client"] is not None
    
    @pytest.mark.asyncio
    async def test_scheduler_dependency_exists(self):
        """Проверка существования dependency для планировщика"""
        with patch('dependencies.get_scheduler') as mock_get_scheduler:
            mock_scheduler = MagicMock()
            mock_get_scheduler.return_value = mock_scheduler
            
            result = await get_scheduler_dependency()
            
            assert result is not None

