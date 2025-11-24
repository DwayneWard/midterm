"""
Тесты для проверки модульной структуры
Проверяют ОР 3.1, 3.2, 3.3
"""
import pytest


class TestOR31_ModuleStructure:
    """ОР 3.1: Разбить код на отдельные модули"""
    
    def test_api_client_module_exists(self):
        try:
            import api_client
            assert hasattr(api_client, 'get_todos')
        except ImportError:
            pytest.fail("Module api_client not found")
    
    def test_handlers_module_exists(self):
        try:
            import handlers
            assert hasattr(handlers, 'register_handlers')
            assert hasattr(handlers, 'start_handler')
            assert hasattr(handlers, 'todos_handler')
        except ImportError:
            pytest.fail("Module handlers not found")
    
    def test_storage_module_exists(self):
        try:
            import storage
            assert hasattr(storage, 'get_user_favorites')
            assert hasattr(storage, 'add_favorite_task')
        except ImportError:
            pytest.fail("Module storage not found")


class TestOR32_Imports:
    """ОР 3.2: Настраивать импорты между модулями"""
    
    def test_handlers_imports_api_client(self):
        import handlers
        import inspect
        source = inspect.getsource(handlers)
        assert 'get_todos' in source or 'from api_client' in source
    
    def test_handlers_imports_storage(self):
        import handlers
        import inspect
        source = inspect.getsource(handlers)
        assert 'get_user_favorites' in source or 'from storage' in source
    
    def test_api_client_imports_config(self):
        import api_client
        import inspect
        source = inspect.getsource(api_client)
        assert 'TODOS_API_URL' in source or 'from config' in source


class TestOR33_CodeSeparation:
    """ОР 3.3: Структурировать проект для расширения"""
    
    def test_api_client_has_only_api_logic(self):
        import api_client
        import inspect
        source = inspect.getsource(api_client)
        assert 'telebot' not in source
        assert 'send_message' not in source
    
    def test_handlers_uses_api_client(self):
        import handlers
        import inspect
        source = inspect.getsource(handlers)
        assert 'get_todos' in source

