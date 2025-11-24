import requests
from typing import Dict, Optional

from config import EXCHANGE_API_URL

def get_exchange_rates(base_currency: str) -> Optional[Dict]:
    """
    Получить актуальные курсы валют относительно базовой валюты.
    
    Args:
        base_currency: Код базовой валюты (например, "USD", "EUR", "RUB")
        
    Returns:
        Словарь с данными о курсах валют или None в случае ошибки
        
    TODO: Реализовать функцию согласно требованиям:
    1. Сформировать HTTP GET-запрос к EXCHANGE_API_URL с параметром базовой валюты
       URL должен быть: f"{EXCHANGE_API_URL}/{base_currency}"
       Например: "https://api.exchangerate-api.com/v4/latest/USD"
    
    2. Выполнить запрос используя библиотеку requests
    
    3. Проверить статус-код ответа:
       - Если статус 200: распарсить JSON-ответ и вернуть словарь
       - Если статус 404: вернуть None
       - Если статус не 200 и не 404: вернуть None
    
    4. Обработать возможные исключения:
       - requests.exceptions.Timeout: вернуть None
       - requests.exceptions.RequestException: вернуть None
       - ValueError/JSONDecodeError: вернуть None
    
    Пример успешного ответа API:
    {
        "base": "USD",
        "date": "2024-01-15",
        "rates": {
            "EUR": 0.92,
            "RUB": 90.5,
            "GBP": 0.79
        }
    }
    """
    pass

