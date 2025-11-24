import requests
from typing import Dict, Optional, List

from config import QUOTES_API_URL

def get_quote(tags: str = None) -> Optional[Dict]:
    """
    Получить случайную цитату.
    
    Args:
        tags: Теги для фильтрации (например, "wisdom", "success", "inspirational")
        
    Returns:
        Словарь с данными о цитате или None в случае ошибки
        
    TODO: Реализовать функцию согласно требованиям:
    1. Сформировать HTTP GET-запрос к QUOTES_API_URL с параметрами:
       - Если tags указан: добавить параметр tags=tags
       - Например: "https://api.quotable.io/quotes/random?tags=wisdom"
       - Если tags не указан: запрос без параметров
    
    2. Выполнить запрос используя библиотеку requests
    
    3. Проверить статус-код ответа:
       - Если статус 200: распарсить JSON-ответ (это массив с одной цитатой, взять первый элемент [0])
       - Если статус 404: вернуть None
       - Если статус не 200 и не 404: вернуть None
    
    4. Обработать возможные исключения:
       - requests.exceptions.Timeout: вернуть None
       - requests.exceptions.RequestException: вернуть None
       - ValueError/JSONDecodeError: вернуть None
       - IndexError: если массив пустой, вернуть None
    
    Пример успешного ответа API (первый элемент массива):
    {
        "_id": "5d91bacc5eb3c80001c8e4b3",
        "content": "The way to get started is to quit talking and begin doing.",
        "author": "Walt Disney",
        "tags": ["success", "inspirational"]
    }
    """
    pass

