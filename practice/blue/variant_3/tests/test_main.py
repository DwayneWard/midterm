"""
Тесты для main.py
Проверяют ОР 4.1: Настроить и запустить бота
"""
import pytest


class TestOR41_BotSetup:
    """ОР 4.1: Настроить и запустить Telegram-бота"""
    
    def test_main_function_exists(self):
        import main
        assert hasattr(main, 'main')
        assert callable(main.main)

