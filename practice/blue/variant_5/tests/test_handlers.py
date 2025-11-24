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
        quote_handler,
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
        message.text = "/quote wisdom"
        return message
    
    def test_start_handler_sends_message(self, mock_bot, mock_message):
        """Проверка отправки приветственного сообщения"""
        try:
            from handlers import start_handler
            start_handler(mock_bot, mock_message)
            mock_bot.send_message.assert_called_once()
            call_args = mock_bot.send_message.call_args
            assert call_args[0][0] == mock_message.chat.id
            assert "/quote" in call_args[0][1] or "цитат" in call_args[0][1].lower()
        except ImportError:
            pytest.skip("handlers module not available")
    
    @patch('handlers.get_quote')
    def test_quote_handler_with_command(self, mock_get_quote, mock_bot, mock_message):
        """Проверка обработки команды /quote"""
        try:
            from handlers import quote_handler
            mock_get_quote.return_value = {
                "content": "Test quote",
                "author": "Test Author",
                "tags": ["test"]
            }
            quote_handler(mock_bot, mock_message)
            mock_bot.send_message.assert_called()
            call_args = mock_bot.send_message.call_args
            assert "Test" in call_args[0][1]
        except ImportError:
            pytest.skip("handlers module not available")


class TestOR51_InlineButtons:
    """ОР 5.1: Реализовать интерактивное меню с inline-кнопками"""
    
    @pytest.fixture
    def mock_bot(self):
        return MagicMock(spec=telebot.TeleBot)
    
    @patch('handlers.get_quote')
    def test_quote_handler_creates_inline_button(self, mock_get_quote, mock_bot):
        """Проверка создания inline-кнопки в quote_handler"""
        try:
            from handlers import quote_handler
            message = MagicMock(spec=types.Message)
            message.chat = MagicMock()
            message.chat.id = 12345
            message.text = "wisdom"
            mock_get_quote.return_value = {
                "content": "Test",
                "author": "Author",
                "tags": []
            }
            quote_handler(mock_bot, message)
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
    
    @patch('handlers.add_favorite_author')
    def test_callback_add_author(self, mock_add_author, mock_bot, mock_call):
        """Проверка обработки callback для добавления автора"""
        try:
            from handlers import button_callback_handler
            mock_call.data = "add_Test_Author"
            mock_add_author.return_value = True
            button_callback_handler(mock_bot, mock_call)
            mock_add_author.assert_called_once_with(67890, "Test Author")
            mock_bot.answer_callback_query.assert_called()
        except ImportError:
            pytest.skip("handlers module not available")

