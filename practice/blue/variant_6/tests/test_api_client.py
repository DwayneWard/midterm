"""
Тесты для api_client.py
Проверяют ОРы: 1.1, 1.2, 2.1, 2.2, 2.3, 2.4
"""
import pytest
import requests
from requests.exceptions import Timeout, RequestException
from unittest.mock import Mock, patch
import json

from api_client import get_recipe


class TestOR11_HTTPRequest:
    """ОР 1.1: Сформировать HTTP-запрос с нужным методом и необходимыми заголовками"""
    
    def test_get_request_formed_correctly(self, mock_requests, sample_recipe_data):
        """Проверка формирования GET-запроса с правильным URL"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = sample_recipe_data
        mock_requests.get.return_value = mock_response
        
        get_recipe("pasta")
        
        mock_requests.get.assert_called_once()
        call_args = mock_requests.get.call_args
        assert "themealdb.com" in call_args[0][0] or "s=" in str(call_args)


class TestOR12_StatusCodeHandling:
    """ОР 1.2: Анализировать ответ сервера, интерпретировать статус-коды"""
    
    def test_status_200_returns_data(self, mock_requests, sample_recipe_data):
        """Проверка обработки статус-кода 200"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = sample_recipe_data
        mock_requests.get.return_value = mock_response
        
        result = get_recipe("pasta")
        
        assert result is not None
        assert isinstance(result, dict)
        assert "strMeal" in result
    
    def test_empty_meals_returns_none(self, mock_requests):
        """Проверка обработки пустого ответа"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"meals": None}
        mock_requests.get.return_value = mock_response
        
        result = get_recipe("nonexistent")
        
        assert result is None


class TestOR21_RequestsUsage:
    """ОР 2.1: Использовать requests для отправки HTTP-запросов"""
    
    def test_uses_requests_get(self, mock_requests, sample_recipe_data):
        """Проверка использования requests.get()"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = sample_recipe_data
        mock_requests.get.return_value = mock_response
        
        get_recipe("pasta")
        
        mock_requests.get.assert_called_once()


class TestOR22_ErrorHandling:
    """ОР 2.2: Реализовывать обработку ошибок в запросах"""
    
    def test_timeout_exception_handled(self, mock_requests):
        """Проверка обработки Timeout"""
        mock_requests.get.side_effect = Timeout()
        
        result = get_recipe("pasta")
        
        assert result is None
    
    def test_request_exception_handled(self, mock_requests):
        """Проверка обработки RequestException"""
        mock_requests.get.side_effect = RequestException()
        
        result = get_recipe("pasta")
        
        assert result is None


class TestOR23_JSONParsing:
    """ОР 2.3: Преобразовывать данные из формата JSON в объекты Python"""
    
    def test_json_response_parsed(self, mock_requests, sample_recipe_data):
        """Проверка парсинга JSON-ответа"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = sample_recipe_data
        mock_requests.get.return_value = mock_response
        
        result = get_recipe("pasta")
        
        assert result is not None
        assert isinstance(result, dict)
        assert result["strMeal"] == "Spaghetti Carbonara"


class TestOR24_ErrorHandlingComplete:
    """ОР 2.4: Реализовывать обработку ошибок запросов"""
    
    def test_value_error_handled(self, mock_requests):
        """Проверка обработки ValueError"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.side_effect = ValueError("Invalid data")
        mock_requests.get.return_value = mock_response
        
        result = get_recipe("pasta")
        
        assert result is None

