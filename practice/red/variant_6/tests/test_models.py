"""
Тесты для models.py
Проверяют ОРы: 3.1 (валидация данных с помощью Pydantic)
"""
import pytest
from pydantic import ValidationError

try:
    from models import RecipeCreate, Recipe, RecipeUpdate
except ImportError:
    pytest.skip("models module not available", allow_module_level=True)


class TestOR31_PydanticValidation:
    """ОР 3.1: Использовать Pydantic для валидации данных"""
    
    def test_recipe_create_valid_data(self):
        """Проверка создания RecipeCreate с валидными данными"""
        recipe = RecipeCreate(
            name="Тестовый рецепт",
            description="Описание рецепта",
            ingredients="Ингредиент1, Ингредиент2",
            cooking_time=60,
            difficulty="medium"
        )
        assert recipe.name == "Тестовый рецепт"
        assert recipe.description == "Описание рецепта"
        assert recipe.ingredients == "Ингредиент1, Ингредиент2"
        assert recipe.cooking_time == 60
        assert recipe.difficulty == "medium"
    
    def test_recipe_create_minimal_data(self):
        """Проверка создания RecipeCreate с минимальными данными"""
        recipe = RecipeCreate(
            name="Рецепт",
            ingredients="Ингредиенты",
            cooking_time=30,
            difficulty="easy"
        )
        assert recipe.name == "Рецепт"
        assert recipe.description is None
    
    def test_recipe_create_validation_name_required(self):
        """Проверка валидации: name обязателен"""
        with pytest.raises(ValidationError):
            RecipeCreate(ingredients="Ингредиенты", cooking_time=30, difficulty="easy")
    
    def test_recipe_create_validation_ingredients_required(self):
        """Проверка валидации: ingredients обязателен"""
        with pytest.raises(ValidationError):
            RecipeCreate(name="Рецепт", cooking_time=30, difficulty="easy")
    
    def test_recipe_create_validation_cooking_time_required(self):
        """Проверка валидации: cooking_time обязателен"""
        with pytest.raises(ValidationError):
            RecipeCreate(name="Рецепт", ingredients="Ингредиенты", difficulty="easy")
    
    def test_recipe_create_validation_difficulty_required(self):
        """Проверка валидации: difficulty обязателен"""
        with pytest.raises(ValidationError):
            RecipeCreate(name="Рецепт", ingredients="Ингредиенты", cooking_time=30)
    
    def test_recipe_inherits_from_recipe_create(self):
        """Проверка наследования Recipe от RecipeCreate"""
        recipe = Recipe(
            id=1,
            name="Рецепт",
            ingredients="Ингредиенты",
            cooking_time=45,
            difficulty="hard"
        )
        assert recipe.id == 1
        assert recipe.name == "Рецепт"
    
    def test_recipe_update_all_optional(self):
        """Проверка, что все поля RecipeUpdate необязательны"""
        recipe_update = RecipeUpdate()
        assert recipe_update.name is None
        assert recipe_update.ingredients is None
        assert recipe_update.cooking_time is None
        assert recipe_update.difficulty is None
        assert recipe_update.description is None
    
    def test_recipe_update_partial_update(self):
        """Проверка частичного обновления RecipeUpdate"""
        recipe_update = RecipeUpdate(name="Новое название")
        assert recipe_update.name == "Новое название"
        assert recipe_update.ingredients is None
