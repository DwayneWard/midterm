import requests
from typing import Dict, Optional

from config import RECIPES_API_URL

def get_recipe(meal_name: str) -> Optional[Dict]:
    """
    Получить рецепт блюда по названию.
    
    Args:
        meal_name: Название блюда
        
    Returns:
        Словарь с данными о рецепте или None в случае ошибки
        
    TODO: Реализовать функцию согласно требованиям:
    1. Сформировать HTTP GET-запрос к RECIPES_API_URL с параметром s (название блюда)
       URL должен быть: f"{RECIPES_API_URL}?s={meal_name}"
       Например: "https://www.themealdb.com/api/json/v1/1/search.php?s=pasta"
    
    2. Выполнить запрос используя библиотеку requests
    
    3. Проверить статус-код ответа:
       - Если статус 200: распарсить JSON-ответ и проверить наличие meals
       - Если meals не None и не пустой: вернуть первый элемент массива meals[0]
       - Если meals None или пустой: вернуть None
       - Если статус не 200: вернуть None
    
    4. Обработать возможные исключения:
       - requests.exceptions.Timeout: вернуть None
       - requests.exceptions.RequestException: вернуть None
       - ValueError/JSONDecodeError: вернуть None
       - IndexError: если массив пустой, вернуть None
    
    Пример успешного ответа API (первый элемент meals):
    {
        "idMeal": "52771",
        "strMeal": "Spaghetti Carbonara",
        "strCategory": "Pasta",
        "strArea": "Italian",
        "strInstructions": "Инструкции по приготовлению...",
        "strMealThumb": "https://...",
        "strIngredient1": "Spaghetti",
        "strMeasure1": "400g",
        ...
    }
    """
    pass

