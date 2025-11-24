"""
Тесты для проверки модульной структуры
Проверяют ОР 3.1, 3.2, 3.3
"""
import pytest
import importlib
import sys
from pathlib import Path


class TestOR31_ModuleStructure:
    """ОР 3.1: Разбить код на отдельные модули"""
    
    def test_api_client_module_exists(self):
        """Проверка существования модуля api_client"""
        try:
            import api_client
            assert hasattr(api_client, 'get_country_info')
        except ImportError:
            pytest.fail("Module api_client not found")
    
    def test_handlers_module_exists(self):
        """Проверка существования модуля handlers"""
        try:
            import handlers
            assert hasattr(handlers, 'register_handlers')
            assert hasattr(handlers, 'start_handler')
            assert hasattr(handlers, 'country_handler')
        except ImportError:
            pytest.fail("Module handlers not found")
    
    def test_storage_module_exists(self):
        """Проверка существования модуля storage"""
        try:
            import storage
            assert hasattr(storage, 'get_user_favorites')
            assert hasattr(storage, 'add_favorite_country')
        except ImportError:
            pytest.fail("Module storage not found")


class TestOR32_Imports:
    """ОР 3.2: Настраивать импорты между модулями"""
    
    def test_handlers_imports_api_client(self):
        """Проверка импорта api_client в handlers"""
        import handlers
        import inspect
        
        source = inspect.getsource(handlers)
        # Проверяем, что есть импорт get_country_info
        assert 'get_country_info' in source or 'from api_client' in source
    
    def test_handlers_imports_storage(self):
        """Проверка импорта storage в handlers"""
        import handlers
        import inspect
        
        source = inspect.getsource(handlers)
        # Проверяем, что есть импорт функций storage
        assert 'get_user_favorites' in source or 'from storage' in source
    
    def test_api_client_imports_config(self):
        """Проверка импорта config в api_client"""
        import api_client
        import inspect
        
        source = inspect.getsource(api_client)
        assert 'COUNTRIES_API_URL' in source or 'from config' in source


class TestOR33_CodeSeparation:
    """ОР 3.3: Структурировать проект для расширения"""
    
    def test_api_client_has_only_api_logic(self):
        """Проверка, что api_client содержит только логику API"""
        import api_client
        import inspect
        
        source = inspect.getsource(api_client)
        # Не должно быть логики бота
        assert 'telebot' not in source
        assert 'send_message' not in source
    
    def test_handlers_uses_api_client(self):
        """Проверка, что handlers использует api_client, а не делает запросы напрямую"""
        import handlers
        import inspect
        
        source = inspect.getsource(handlers)
        # Должен использовать функцию из api_client
        assert 'get_country_info' in source

