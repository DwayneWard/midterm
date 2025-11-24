import requests
from typing import Dict, Optional, List

from config import TODOS_API_URL

def get_todos(user_id: int = 1) -> Optional[List[Dict]]:
    """
    Получить список задач для пользователя.
    
    Args:
        user_id: ID пользователя (по умолчанию 1)
        
    Returns:
        Список словарей с задачами или None в случае ошибки
        
    TODO: Реализовать функцию согласно требованиям:
    1. Сформировать HTTP GET-запрос к TODOS_API_URL с параметром userId
       URL должен быть: f"{TODOS_API_URL}?userId={user_id}"
       Например: "https://jsonplaceholder.typicode.com/todos?userId=1"
    
    2. Выполнить запрос используя библиотеку requests
    
    3. Проверить статус-код ответа:
       - Если статус 200: распарсить JSON-ответ (это массив задач) и вернуть список
       - Если статус 404: вернуть None
       - Если статус не 200 и не 404: вернуть None
    
    4. Обработать возможные исключения:
       - requests.exceptions.Timeout: вернуть None
       - requests.exceptions.RequestException: вернуть None
       - ValueError/JSONDecodeError: вернуть None
    
    Пример успешного ответа API:
    [
        {
            "userId": 1,
            "id": 1,
            "title": "delectus aut autem",
            "completed": false
        },
        {
            "userId": 1,
            "id": 2,
            "title": "quis ut nam facilis",
            "completed": true
        }
    ]
    """
    pass

