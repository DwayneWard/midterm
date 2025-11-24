"""
Тесты для api_client.py
Проверяют ОРы: 1.1, 1.2, 2.1, 2.2, 2.3, 2.4
"""
import pytest
import requests
from requests.exceptions import Timeout, RequestException
from unittest.mock import Mock, patch
import json

from api_client import get_todos


class TestOR11_HTTPRequest:
    """ОР 1.1: Сформировать HTTP-запрос с нужным методом и необходимыми заголовками"""
    
    def test_get_request_formed_correctly(self, mock_requests, sample_todos_data):
        """Проверка формирования GET-запроса с правильным URL"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = sample_todos_data
        mock_requests.get.return_value = mock_response
        
        get_todos(1)
        
        mock_requests.get.assert_called_once()
        call_args = mock_requests.get.call_args
        assert "jsonplaceholder.typicode.com" in call_args[0][0] or "userId" in str(call_args)


class TestOR12_StatusCodeHandling:
    """ОР 1.2: Анализировать ответ сервера, интерпретировать статус-коды"""
    
    def test_status_200_returns_data(self, mock_requests, sample_todos_data):
        """Проверка обработки статус-кода 200"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = sample_todos_data
        mock_requests.get.return_value = mock_response
        
        result = get_todos(1)
        
        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0
    
    def test_status_404_returns_none(self, mock_requests):
        """Проверка обработки статус-кода 404"""
        mock_response = Mock()
        mock_response.status_code = 404
        mock_requests.get.return_value = mock_response
        
        result = get_todos(999)
        
        assert result is None


class TestOR21_RequestsUsage:
    """ОР 2.1: Использовать requests для отправки HTTP-запросов"""
    
    def test_uses_requests_get(self, mock_requests, sample_todos_data):
        """Проверка использования requests.get()"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = sample_todos_data
        mock_requests.get.return_value = mock_response
        
        get_todos(1)
        
        mock_requests.get.assert_called_once()


class TestOR22_ErrorHandling:
    """ОР 2.2: Реализовывать обработку ошибок в запросах"""
    
    def test_timeout_exception_handled(self, mock_requests):
        """Проверка обработки Timeout"""
        mock_requests.get.side_effect = Timeout()
        
        result = get_todos(1)
        
        assert result is None
    
    def test_request_exception_handled(self, mock_requests):
        """Проверка обработки RequestException"""
        mock_requests.get.side_effect = RequestException()
        
        result = get_todos(1)
        
        assert result is None


class TestOR23_JSONParsing:
    """ОР 2.3: Преобразовывать данные из формата JSON в объекты Python"""
    
    def test_json_response_parsed(self, mock_requests, sample_todos_data):
        """Проверка парсинга JSON-ответа"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = sample_todos_data
        mock_requests.get.return_value = mock_response
        
        result = get_todos(1)
        
        assert result is not None
        assert isinstance(result, list)
        assert "title" in result[0]


class TestOR24_ErrorHandlingComplete:
    """ОР 2.4: Реализовывать обработку ошибок запросов"""
    
    def test_value_error_handled(self, mock_requests):
        """Проверка обработки ValueError"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.side_effect = ValueError("Invalid data")
        mock_requests.get.return_value = mock_response
        
        result = get_todos(1)
        
        assert result is None

