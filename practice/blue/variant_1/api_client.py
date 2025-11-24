import requests
from typing import Dict, Optional

def get_country_info(country_name: str) -> Optional[Dict]:
    """
    Получить информацию о стране по её названию.
    
    Args:
        country_name: Название страны (на английском или русском)
        
    Returns:
        Словарь с данными о стране или None в случае ошибки
        
    TODO: Реализовать функцию согласно требованиям:
    1. Сформировать HTTP GET-запрос к COUNTRIES_API_URL с параметром названия страны
       URL должен быть: f"{COUNTRIES_API_URL}/{country_name}"
       Например: "https://restcountries.com/v3.1/name/russia"
    
    2. Выполнить запрос используя библиотеку requests
    
    3. Проверить статус-код ответа:
       - Если статус 200: распарсить JSON-ответ (это массив стран, взять первый элемент [0])
       - Если статус 404: вернуть None
       - Если статус не 200 и не 404: вернуть None
    
    4. Обработать возможные исключения:
       - requests.exceptions.Timeout: вернуть None
       - requests.exceptions.RequestException: вернуть None
       - ValueError/JSONDecodeError: вернуть None
       - IndexError: если массив пустой, вернуть None
    
    Пример успешного ответа API (первый элемент массива):
    {
        "name": {"common": "Russia", "official": "Russian Federation"},
        "capital": ["Moscow"],
        "population": 144104080,
        "currencies": {"RUB": {"name": "Russian ruble", "symbol": "₽"}},
        "languages": {"rus": "Russian"},
        "region": "Europe"
    }
    """
    pass
