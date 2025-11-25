from typing import List, Optional
from models import Recipe, RecipeCreate, RecipeUpdate


# Хранилище рецептов в памяти
recipes_db: List[Recipe] = [
    Recipe(id=1, name="Борщ", description="Традиционный украинский суп", ingredients="Свекла, капуста, морковь, мясо, лук", cooking_time=120, difficulty="medium"),
    Recipe(id=2, name="Омлет", description="Простой завтрак", ingredients="Яйца, молоко, соль", cooking_time=10, difficulty="easy"),
    Recipe(id=3, name="Тирамису", description="Итальянский десерт", ingredients="Печенье, кофе, сыр маскарпоне, какао", cooking_time=180, difficulty="hard"),
]


def get_all_recipes() -> List[Recipe]:
    """
    Получить все рецепты
    
    Returns:
        Список всех рецептов
    """
    return recipes_db


def get_recipe_by_id(recipe_id: int) -> Optional[Recipe]:
    """
    Получить рецепт по ID
    
    Args:
        recipe_id: ID рецепта
        
    Returns:
        Рецепт или None, если рецепт не найден
        
    TODO: Реализовать функцию:
    1. Пройтись по списку recipes_db
    2. Найти рецепт с указанным id
    3. Вернуть рецепт или None, если не найден
    """
    pass


def create_recipe(recipe_data: RecipeCreate) -> Recipe:
    """
    Создать новый рецепт
    
    Args:
        recipe_data: Данные нового рецепта (без id)
        
    Returns:
        Созданный рецепт с присвоенным id
        
    TODO: Реализовать функцию:
    1. Определить новый id (максимальный id в recipes_db + 1, или 1 если список пуст)
    2. Создать объект Recipe с новым id и данными из recipe_data
    3. Добавить рецепт в recipes_db
    4. Вернуть созданный рецепт
    """
    pass


def update_recipe(recipe_id: int, recipe_data: RecipeUpdate) -> Optional[Recipe]:
    """
    Обновить рецепт
    
    Args:
        recipe_id: ID рецепта для обновления
        recipe_data: Новые данные рецепта
        
    Returns:
        Обновленный рецепт или None, если рецепт не найден
        
    TODO: Реализовать функцию:
    1. Найти рецепт с указанным id в recipes_db
    2. Если рецепт не найден, вернуть None
    3. Обновить поля рецепта данными из recipe_data (только те поля, которые не None)
       Используй: recipe.field = recipe_data.field if recipe_data.field is not None else recipe.field
    4. Вернуть обновленный рецепт
    """
    pass


def delete_recipe(recipe_id: int) -> bool:
    """
    Удалить рецепт
    
    Args:
        recipe_id: ID рецепта для удаления
        
    Returns:
        True, если рецепт удален, False если не найден
        
    TODO: Реализовать функцию:
    1. Найти рецепт с указанным id в recipes_db
    2. Если рецепт не найден, вернуть False
    3. Удалить рецепт из recipes_db
    4. Вернуть True
    """
    pass

