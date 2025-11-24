import requests
from typing import Dict, Optional

from config import NEWS_API_URL, NEWS_API_KEY

def get_news(category: str, country: str = "us") -> Optional[Dict]:
    """
    Получить новости по категории.
    
    Args:
        category: Категория новостей (например, "technology", "business", "sports")
        country: Код страны (по умолчанию "us")
        
    Returns:
        Словарь с данными о новостях или None в случае ошибки
        
    TODO: Реализовать функцию согласно требованиям:
    1. Сформировать HTTP GET-запрос к NEWS_API_URL с параметрами:
       - category: категория новостей
       - country: код страны
       - apiKey: NEWS_API_KEY
    
    2. Выполнить запрос используя библиотеку requests
    
    3. Проверить статус-код ответа:
       - Если статус 200: распарсить JSON-ответ и вернуть словарь
       - Если статус 401: вернуть None (неверный API ключ)
       - Если статус 404: вернуть None
       - Если статус не 200 и не 404: вернуть None
    
    4. Обработать возможные исключения:
       - requests.exceptions.Timeout: вернуть None
       - requests.exceptions.RequestException: вернуть None
       - ValueError/JSONDecodeError: вернуть None
    
    Пример успешного ответа API:
    {
        "status": "ok",
        "totalResults": 10,
        "articles": [
            {
                "title": "Заголовок новости",
                "description": "Описание новости",
                "url": "https://example.com/news",
                "publishedAt": "2024-01-15T10:00:00Z"
            }
        ]
    }
    """
    pass

