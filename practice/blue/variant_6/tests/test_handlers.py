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
        recipe_handler,
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
        message.text = "/recipe pasta"
        return message
    
    def test_start_handler_sends_message(self, mock_bot, mock_message):
        """Проверка отправки приветственного сообщения"""
        try:
            from handlers import start_handler
            start_handler(mock_bot, mock_message)
            mock_bot.send_message.assert_called_once()
            call_args = mock_bot.send_message.call_args
            assert call_args[0][0] == mock_message.chat.id
            assert "/recipe" in call_args[0][1] or "рецепт" in call_args[0][1].lower()
        except ImportError:
            pytest.skip("handlers module not available")
    
    @patch('handlers.get_recipe')
    def test_recipe_handler_with_command(self, mock_get_recipe, mock_bot, mock_message):
        """Проверка обработки команды /recipe"""
        try:
            from handlers import recipe_handler
            mock_get_recipe.return_value = {
                "strMeal": "Pasta",
                "strCategory": "Italian",
                "strInstructions": "Test instructions"
            }
            recipe_handler(mock_bot, mock_message)
            mock_bot.send_message.assert_called()
            call_args = mock_bot.send_message.call_args
            assert "Pasta" in call_args[0][1] or "Test" in call_args[0][1]
        except ImportError:
            pytest.skip("handlers module not available")


class TestOR51_InlineButtons:
    """ОР 5.1: Реализовать интерактивное меню с inline-кнопками"""
    
    @pytest.fixture
    def mock_bot(self):
        return MagicMock(spec=telebot.TeleBot)
    
    @patch('handlers.get_recipe')
    def test_recipe_handler_creates_inline_button(self, mock_get_recipe, mock_bot):
        """Проверка создания inline-кнопки в recipe_handler"""
        try:
            from handlers import recipe_handler
            message = MagicMock(spec=types.Message)
            message.chat = MagicMock()
            message.chat.id = 12345
            message.text = "pasta"
            mock_get_recipe.return_value = {
                "strMeal": "Pasta",
                "strCategory": "Italian",
                "strInstructions": "Test"
            }
            recipe_handler(mock_bot, message)
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
    
    @patch('handlers.add_favorite_meal')
    def test_callback_add_meal(self, mock_add_meal, mock_bot, mock_call):
        """Проверка обработки callback для добавления блюда"""
        try:
            from handlers import button_callback_handler
            mock_call.data = "add_Pasta"
            mock_add_meal.return_value = True
            button_callback_handler(mock_bot, mock_call)
            mock_add_meal.assert_called_once_with(67890, "Pasta")
            mock_bot.answer_callback_query.assert_called()
        except ImportError:
            pytest.skip("handlers module not available")

