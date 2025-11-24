"""
Тесты для handlers.py
Проверяют ОРы: 4.2, 5.1, 5.2
"""
import pytest
from unittest.mock import Mock, MagicMock, patch
import telebot
from telebot import types

try:
    from handlers import (
        start_handler,
        news_handler,
        favorites_handler,
        button_callback_handler,
        register_handlers
    )
except ImportError:
    pass


class TestOR42_CommandHandling:
    """ОР 4.2: Реализовать обработку команд и текстовых сообщений"""
    
    @pytest.fixture
    def mock_bot(self):
        return MagicMock(spec=telebot.TeleBot)
    
    @pytest.fixture
    def mock_message(self):
        message = MagicMock(spec=types.Message)
        message.chat = MagicMock()
        message.chat.id = 12345
        message.from_user = MagicMock()
        message.from_user.id = 67890
        message.text = "/news technology"
        return message
    
    def test_start_handler_sends_message(self, mock_bot, mock_message):
        try:
            from handlers import start_handler
            start_handler(mock_bot, mock_message)
            mock_bot.send_message.assert_called_once()
            call_args = mock_bot.send_message.call_args
            assert call_args[0][0] == mock_message.chat.id
        except ImportError:
            pytest.skip("handlers module not available")
    
    @patch('handlers.get_news')
    def test_news_handler_with_command(self, mock_get_news, mock_bot, mock_message):
        try:
            from handlers import news_handler
            mock_get_news.return_value = {
                "status": "ok",
                "totalResults": 2,
                "articles": [{"title": "Test", "description": "Desc", "url": "http://test.com"}]
            }
            news_handler(mock_bot, mock_message)
            mock_bot.send_message.assert_called()
        except ImportError:
            pytest.skip("handlers module not available")


class TestOR51_InlineButtons:
    """ОР 5.1: Реализовать интерактивное меню с inline-кнопками"""
    
    @pytest.fixture
    def mock_bot(self):
        return MagicMock(spec=telebot.TeleBot)
    
    @patch('handlers.get_news')
    def test_news_handler_creates_inline_button(self, mock_get_news, mock_bot):
        try:
            from handlers import news_handler
            message = MagicMock(spec=types.Message)
            message.chat = MagicMock()
            message.chat.id = 12345
            message.text = "technology"
            mock_get_news.return_value = {
                "status": "ok",
                "totalResults": 1,
                "articles": [{"title": "Test", "url": "http://test.com"}]
            }
            news_handler(mock_bot, message)
            mock_bot.send_message.assert_called()
            call_kwargs = mock_bot.send_message.call_args[1]
            assert "reply_markup" in call_kwargs
        except ImportError:
            pytest.skip("handlers module not available")


class TestOR52_CallbackHandling:
    """ОР 5.2: Настроить обработку callback-запросов"""
    
    @pytest.fixture
    def mock_bot(self):
        return MagicMock(spec=telebot.TeleBot)
    
    @pytest.fixture
    def mock_call(self):
        call = MagicMock(spec=types.CallbackQuery)
        call.id = "test_callback_id"
        call.from_user = MagicMock()
        call.from_user.id = 67890
        call.message = MagicMock()
        call.message.chat = MagicMock()
        call.message.chat.id = 12345
        return call
    
    @patch('handlers.add_favorite_category')
    def test_callback_add_category(self, mock_add_category, mock_bot, mock_call):
        try:
            from handlers import button_callback_handler
            mock_call.data = "add_technology"
            mock_add_category.return_value = True
            button_callback_handler(mock_bot, mock_call)
            mock_add_category.assert_called_once_with(67890, "technology")
        except ImportError:
            pytest.skip("handlers module not available")

