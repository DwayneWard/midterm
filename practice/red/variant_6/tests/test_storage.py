"""
Тесты для storage.py
Проверяют ОРы: 3.2 (работа с данными в памяти)
"""
import pytest

try:
    from storage import (
        get_all_recipes,
        get_recipe_by_id,
        create_recipe,
        update_recipe,
        delete_recipe
    )
    from models import Recipe, RecipeCreate
except ImportError:
    pytest.skip("storage module not available", allow_module_level=True)


class TestOR32_DataStorage:
    """ОР 3.2: Работать с данными в памяти"""
    
    def test_get_all_recipes_returns_list(self):
        """Проверка получения всех рецептов"""
        recipes = get_all_recipes()
        assert isinstance(recipes, list)
        assert len(recipes) > 0
    
    def test_get_recipe_by_id_exists(self):
        """Проверка получения рецепта по существующему ID"""
        # Создаем рецепт для гарантии, что он существует
        new_recipe = RecipeCreate(
            name="Тестовый рецепт для проверки",
            ingredients="Ингредиенты",
            cooking_time=30,
            difficulty="easy"
        )
        created = create_recipe(new_recipe)
        recipe_id = created.id
        
        # Проверяем получение рецепта
        recipe = get_recipe_by_id(recipe_id)
        assert recipe is not None
        assert recipe.id == recipe_id
    
    def test_get_recipe_by_id_not_exists(self):
        """Проверка получения рецепта по несуществующему ID"""
        recipe = get_recipe_by_id(99999)
        assert recipe is None
    
    def test_create_recipe_adds_to_storage(self):
        """Проверка создания нового рецепта"""
        initial_count = len(get_all_recipes())
        new_recipe = RecipeCreate(
            name="Новый тестовый рецепт",
            ingredients="Новые ингредиенты",
            cooking_time=90,
            difficulty="hard"
        )
        created = create_recipe(new_recipe)
        assert created.id is not None
        assert created.name == "Новый тестовый рецепт"
        assert len(get_all_recipes()) == initial_count + 1
    
    def test_update_recipe_exists(self):
        """Проверка обновления существующего рецепта"""
        # Создаем рецепт для обновления
        new_recipe = RecipeCreate(
            name="Рецепт для обновления",
            ingredients="Ингредиенты",
            cooking_time=45,
            difficulty="medium"
        )
        created = create_recipe(new_recipe)
        
        # Обновляем рецепт
        from models import RecipeUpdate
        updated_data = RecipeUpdate(name="Обновленное название")
        updated = update_recipe(created.id, updated_data)
        assert updated is not None
        assert updated.name == "Обновленное название"
    
    def test_update_recipe_not_exists(self):
        """Проверка обновления несуществующего рецепта"""
        from models import RecipeUpdate
        updated_data = RecipeUpdate(name="Тест")
        result = update_recipe(99999, updated_data)
        assert result is None
    
    def test_delete_recipe_exists(self):
        """Проверка удаления существующего рецепта"""
        # Создаем рецепт для удаления
        new_recipe = RecipeCreate(
            name="Рецепт для удаления",
            ingredients="Ингредиенты",
            cooking_time=20,
            difficulty="easy"
        )
        created = create_recipe(new_recipe)
        recipe_id = created.id
        
        # Удаляем рецепт
        result = delete_recipe(recipe_id)
        assert result is True
        assert get_recipe_by_id(recipe_id) is None
    
    def test_delete_recipe_not_exists(self):
        """Проверка удаления несуществующего рецепта"""
        result = delete_recipe(99999)
        assert result is False
