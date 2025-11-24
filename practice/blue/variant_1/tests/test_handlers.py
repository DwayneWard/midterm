"""
Тесты для handlers.py
Проверяют ОРы: 4.2, 5.1, 5.2
"""
import pytest
from unittest.mock import Mock, MagicMock, patch
import telebot
from telebot import types

# Импортируем обработчики
try:
    from handlers import (
        start_handler,
        country_handler,
        favorites_handler,
        button_callback_handler,
        register_handlers
    )
except ImportError:
    # Если модуль не импортируется, тесты пропустятся
    pass


class TestOR42_CommandHandling:
    """ОР 4.2: Реализовать обработку команд и текстовых сообщений"""
    
    @pytest.fixture
    def mock_bot(self):
        """Мок бота"""
        bot = MagicMock(spec=telebot.TeleBot)
        return bot
    
    @pytest.fixture
    def mock_message(self):
        """Мок сообщения"""
        message = MagicMock(spec=types.Message)
        message.chat = MagicMock()
        message.chat.id = 12345
        message.from_user = MagicMock()
        message.from_user.id = 67890
        message.text = "/country russia"
        return message
    
    def test_start_handler_sends_message(self, mock_bot, mock_message):
        """Проверка отправки приветственного сообщения"""
        start_handler(mock_bot, mock_message)
        
        mock_bot.send_message.assert_called_once()
        call_args = mock_bot.send_message.call_args
        assert call_args[0][0] == mock_message.chat.id
        assert "/country" in call_args[0][1] or "страна" in call_args[0][1].lower()
    
    @patch('handlers.get_country_info')
    def test_country_handler_with_command(self, mock_get_country, mock_bot, mock_message):
        """Проверка обработки команды /country"""
        mock_get_country.return_value = {
            "name": {"common": "Russia"},
            "capital": ["Moscow"],
            "population": 144104080,
            "currencies": {"RUB": {"name": "Russian ruble"}},
            "languages": {"rus": "Russian"},
            "region": "Europe"
        }
        
        country_handler(mock_bot, mock_message)
        
        mock_bot.send_message.assert_called()
        # Проверяем, что отправлено сообщение с информацией о стране
        call_args = mock_bot.send_message.call_args
        assert "Russia" in call_args[0][1] or "Moscow" in call_args[0][1]
    
    @patch('handlers.get_country_info')
    def test_country_handler_with_text(self, mock_get_country, mock_bot):
        """Проверка обработки текстового сообщения"""
        message = MagicMock(spec=types.Message)
        message.chat = MagicMock()
        message.chat.id = 12345
        message.text = "russia"
        
        mock_get_country.return_value = {
            "name": {"common": "Russia"},
            "capital": ["Moscow"],
            "population": 144104080,
            "currencies": {"RUB": {"name": "Russian ruble"}},
            "languages": {"rus": "Russian"},
            "region": "Europe"
        }
        
        country_handler(mock_bot, message)
        
        mock_get_country.assert_called_once_with("russia")
        mock_bot.send_message.assert_called()
    
    @patch('handlers.get_country_info')
    def test_country_handler_no_country_returns_error(self, mock_get_country, mock_bot):
        """Проверка обработки отсутствия названия страны"""
        message = MagicMock(spec=types.Message)
        message.chat = MagicMock()
        message.chat.id = 12345
        message.text = "/country"
        
        country_handler(mock_bot, message)
        
        mock_bot.send_message.assert_called()
        call_args = mock_bot.send_message.call_args
        assert "название" in call_args[0][1].lower() or "укажите" in call_args[0][1].lower()
    
    @patch('handlers.get_user_favorites')
    def test_favorites_handler_empty_list(self, mock_get_favorites, mock_bot, mock_message):
        """Проверка обработки пустого списка избранных"""
        mock_get_favorites.return_value = []
        
        favorites_handler(mock_bot, mock_message)
        
        mock_bot.send_message.assert_called_once()
        call_args = mock_bot.send_message.call_args
        assert "нет" in call_args[0][1].lower() or "пуст" in call_args[0][1].lower()


class TestOR51_InlineButtons:
    """ОР 5.1: Реализовать интерактивное меню с inline-кнопками"""
    
    @pytest.fixture
    def mock_bot(self):
        return MagicMock(spec=telebot.TeleBot)
    
    @patch('handlers.get_country_info')
    def test_country_handler_creates_inline_button(self, mock_get_country, mock_bot):
        """Проверка создания inline-кнопки в country_handler"""
        message = MagicMock(spec=types.Message)
        message.chat = MagicMock()
        message.chat.id = 12345
        message.text = "russia"
        
        mock_get_country.return_value = {
            "name": {"common": "Russia"},
            "capital": ["Moscow"],
            "population": 144104080,
            "currencies": {"RUB": {"name": "Russian ruble"}},
            "languages": {"rus": "Russian"},
            "region": "Europe"
        }
        
        country_handler(mock_bot, message)
        
        # Проверяем, что send_message вызван с reply_markup
        mock_bot.send_message.assert_called()
        call_kwargs = mock_bot.send_message.call_args[1]
        assert "reply_markup" in call_kwargs
        assert call_kwargs["reply_markup"] is not None
    
    @patch('handlers.get_user_favorites')
    def test_favorites_handler_creates_keyboard(self, mock_get_favorites, mock_bot, mock_message):
        """Проверка создания клавиатуры в favorites_handler"""
        mock_get_favorites.return_value = ["Russia", "USA"]
        
        favorites_handler(mock_bot, mock_message)
        
        mock_bot.send_message.assert_called_once()
        call_kwargs = mock_bot.send_message.call_args[1]
        assert "reply_markup" in call_kwargs
        keyboard = call_kwargs["reply_markup"]
        assert keyboard is not None


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
    
    @patch('handlers.add_favorite_country')
    def test_callback_add_country(self, mock_add_favorite, mock_bot, mock_call):
        """Проверка обработки callback для добавления страны"""
        mock_call.data = "add_russia"
        mock_add_favorite.return_value = True
        
        button_callback_handler(mock_bot, mock_call)
        
        mock_add_favorite.assert_called_once_with(67890, "russia")
        mock_bot.answer_callback_query.assert_called()
    
    @patch('handlers.get_country_info')
    def test_callback_show_country(self, mock_get_country, mock_bot, mock_call):
        """Проверка обработки callback для показа страны"""
        mock_call.data = "country_russia"
        mock_get_country.return_value = {
            "name": {"common": "Russia"},
            "capital": ["Moscow"],
            "population": 144104080,
            "currencies": {"RUB": {"name": "Russian ruble"}},
            "languages": {"rus": "Russian"},
            "region": "Europe"
        }
        
        button_callback_handler(mock_bot, mock_call)
        
        mock_get_country.assert_called_once_with("russia")
        mock_bot.send_message.assert_called()
    
    @patch('handlers.get_user_favorites')
    @patch('handlers.remove_favorite_country')
    def test_callback_clear_all(self, mock_remove, mock_get_favorites, mock_bot, mock_call):
        """Проверка обработки callback для очистки всех стран"""
        mock_call.data = "clear_all"
        mock_get_favorites.return_value = ["Russia", "USA"]
        
        button_callback_handler(mock_bot, mock_call)
        
        assert mock_remove.call_count == 2
        mock_bot.answer_callback_query.assert_called()
    
    def test_callback_answers_query(self, mock_bot, mock_call):
        """Проверка вызова answer_callback_query"""
        mock_call.data = "add_russia"
        
        with patch('handlers.add_favorite_country', return_value=True):
            button_callback_handler(mock_bot, mock_call)
        
        mock_bot.answer_callback_query.assert_called_with("test_callback_id")

