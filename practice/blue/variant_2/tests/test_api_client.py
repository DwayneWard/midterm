"""
Тесты для api_client.py
Проверяют ОРы: 1.1, 1.2, 2.1, 2.2, 2.3, 2.4
"""
import pytest
import requests
from requests.exceptions import Timeout, RequestException
from unittest.mock import Mock, patch
import json

from api_client import get_exchange_rates


class TestOR11_HTTPRequest:
    """ОР 1.1: Сформировать HTTP-запрос с нужным методом и необходимыми заголовками"""
    
    def test_get_request_formed_correctly(self, mock_requests, sample_exchange_data):
        """Проверка формирования GET-запроса с правильным URL"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = sample_exchange_data
        mock_requests.get.return_value = mock_response
        
        get_exchange_rates("USD")
        
        mock_requests.get.assert_called_once()
        call_args = mock_requests.get.call_args
        assert "exchangerate-api.com" in call_args[0][0] or "USD" in call_args[0][0]


class TestOR12_StatusCodeHandling:
    """ОР 1.2: Анализировать ответ сервера, интерпретировать статус-коды"""
    
    def test_status_200_returns_data(self, mock_requests, sample_exchange_data):
        """Проверка обработки статус-кода 200"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = sample_exchange_data
        mock_requests.get.return_value = mock_response
        
        result = get_exchange_rates("USD")
        
        assert result is not None
        assert isinstance(result, dict)
        assert "base" in result
        assert "rates" in result
    
    def test_status_404_returns_none(self, mock_requests):
        """Проверка обработки статус-кода 404"""
        mock_response = Mock()
        mock_response.status_code = 404
        mock_requests.get.return_value = mock_response
        
        result = get_exchange_rates("XXX")
        
        assert result is None
    
    def test_other_status_codes_return_none(self, mock_requests):
        """Проверка обработки других статус-кодов"""
        for status_code in [400, 500, 503]:
            mock_response = Mock()
            mock_response.status_code = status_code
            mock_requests.get.return_value = mock_response
            
            result = get_exchange_rates("USD")
            
            assert result is None, f"Status {status_code} should return None"


class TestOR21_RequestsUsage:
    """ОР 2.1: Использовать requests для отправки HTTP-запросов"""
    
    def test_uses_requests_get(self, mock_requests, sample_exchange_data):
        """Проверка использования requests.get()"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = sample_exchange_data
        mock_requests.get.return_value = mock_response
        
        get_exchange_rates("USD")
        
        mock_requests.get.assert_called_once()


class TestOR22_ErrorHandling:
    """ОР 2.2: Реализовывать обработку ошибок в запросах"""
    
    def test_timeout_exception_handled(self, mock_requests):
        """Проверка обработки Timeout"""
        mock_requests.get.side_effect = Timeout()
        
        result = get_exchange_rates("USD")
        
        assert result is None
    
    def test_request_exception_handled(self, mock_requests):
        """Проверка обработки RequestException"""
        mock_requests.get.side_effect = RequestException()
        
        result = get_exchange_rates("USD")
        
        assert result is None


class TestOR23_JSONParsing:
    """ОР 2.3: Преобразовывать данные из формата JSON в объекты Python"""
    
    def test_json_response_parsed(self, mock_requests, sample_exchange_data):
        """Проверка парсинга JSON-ответа"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = sample_exchange_data
        mock_requests.get.return_value = mock_response
        
        result = get_exchange_rates("USD")
        
        assert result is not None
        assert isinstance(result, dict)
        assert result["base"] == "USD"
        assert "EUR" in result["rates"]
    
    def test_json_decode_error_handled(self, mock_requests):
        """Проверка обработки ошибки парсинга JSON"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.side_effect = json.JSONDecodeError("Error", "", 0)
        mock_requests.get.return_value = mock_response
        
        result = get_exchange_rates("USD")
        
        assert result is None


class TestOR24_ErrorHandlingComplete:
    """ОР 2.4: Реализовывать обработку ошибок запросов"""
    
    def test_value_error_handled(self, mock_requests):
        """Проверка обработки ValueError"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.side_effect = ValueError("Invalid data")
        mock_requests.get.return_value = mock_response
        
        result = get_exchange_rates("USD")
        
        assert result is None

