from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import List

from models import Recipe, RecipeCreate, RecipeUpdate
from storage import get_all_recipes, get_recipe_by_id, create_recipe, update_recipe, delete_recipe

# Создание экземпляра FastAPI приложения
app = FastAPI(title="Кулинарная книга", description="Система управления рецептами")

# Настройка шаблонов
# TODO: Инициализировать Jinja2Templates с указанием директории 'templates'
templates = None

# Подключение статических файлов
# TODO: Подключить статические файлы из директории 'static' с помощью app.mount()
# Используй: app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Главная страница - список всех рецептов
    
    TODO: Реализовать функцию:
    1. Получить все рецепты через get_all_recipes()
    2. Вернуть HTML-страницу используя templates.TemplateResponse()
       - Шаблон: "index.html"
       - Контекст: {"request": request, "recipes": recipes}
    """
    pass


@app.get("/recipes/add", response_class=HTMLResponse)
async def add_recipe_form(request: Request):
    """
    Форма для добавления нового рецепта
    
    TODO: Реализовать функцию:
    1. Вернуть HTML-страницу используя templates.TemplateResponse()
       - Шаблон: "recipe_form.html"
       - Контекст: {"request": request, "recipe": None, "action": "add"}
    """
    pass


@app.get("/recipes/{recipe_id}", response_class=HTMLResponse)
async def read_recipe(request: Request, recipe_id: int):
    """
    Страница с детальной информацией о рецепте
    
    Args:
        request: Объект запроса FastAPI
        recipe_id: ID рецепта (path parameter)
        
    TODO: Реализовать функцию:
    1. Получить рецепт по ID через get_recipe_by_id(recipe_id)
    2. Если рецепт не найден (None), вызвать HTTPException со статусом 404
       Используй: raise HTTPException(status_code=404, detail="Рецепт не найден")
    3. Вернуть HTML-страницу используя templates.TemplateResponse()
       - Шаблон: "recipe_detail.html"
       - Контекст: {"request": request, "recipe": recipe}
    """
    pass



@app.post("/recipes/add", response_class=HTMLResponse)
async def create_recipe_post(request: Request):
    """
    Обработка POST-запроса для создания нового рецепта
    
    TODO: Реализовать функцию:
    1. Получить данные формы из request.form()
       Используй: form_data = await request.form()
    2. Создать объект RecipeCreate из данных формы:
       - name = form_data.get("name")
       - description = form_data.get("description") или None
       - ingredients = form_data.get("ingredients")
       - cooking_time = int(form_data.get("cooking_time"))  # Преобразовать строку в int
       - difficulty = form_data.get("difficulty")  # "easy", "medium" или "hard"
    3. Валидировать данные (Pydantic сделает это автоматически при создании RecipeCreate)
    4. Создать рецепт через create_recipe()
    5. Перенаправить на главную страницу "/"
       Используй: from fastapi.responses import RedirectResponse
       return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
    6. Обработать возможные ошибки валидации (HTTPException со статусом 400)
    """
    pass


@app.get("/recipes/{recipe_id}/edit", response_class=HTMLResponse)
async def edit_recipe_form(request: Request, recipe_id: int):
    """
    Форма для редактирования рецепта
    
    Args:
        request: Объект запроса FastAPI
        recipe_id: ID рецепта (path parameter)
        
    TODO: Реализовать функцию:
    1. Получить рецепт по ID через get_recipe_by_id(recipe_id)
    2. Если рецепт не найден, вызвать HTTPException со статусом 404
    3. Вернуть HTML-страницу используя templates.TemplateResponse()
       - Шаблон: "recipe_form.html"
       - Контекст: {"request": request, "recipe": recipe, "action": "edit"}
    """
    pass


@app.post("/recipes/{recipe_id}/edit", response_class=HTMLResponse)
async def update_recipe_post(request: Request, recipe_id: int):
    """
    Обработка POST-запроса для обновления рецепта
    
    Args:
        request: Объект запроса FastAPI
        recipe_id: ID рецепта (path parameter)
        
    TODO: Реализовать функцию:
    1. Получить данные формы из request.form()
       Используй: form_data = await request.form()
    2. Создать объект RecipeUpdate из данных формы (все поля могут быть None):
       - name = form_data.get("name") или None
       - description = form_data.get("description") или None
       - ingredients = form_data.get("ingredients") или None
       - cooking_time = int(form_data.get("cooking_time")) если form_data.get("cooking_time") не пусто, иначе None
       - difficulty = form_data.get("difficulty") или None
    3. Обновить рецепт через update_recipe(recipe_id, recipe_data)
    4. Если рецепт не найден (None), вызвать HTTPException со статусом 404
    5. Перенаправить на страницу рецепта "/recipes/{recipe_id}"
       Используй: from fastapi.responses import RedirectResponse
       return RedirectResponse(url=f"/recipes/{recipe_id}", status_code=status.HTTP_303_SEE_OTHER)
    6. Обработать возможные ошибки валидации (HTTPException со статусом 400)
    """
    pass


@app.post("/recipes/{recipe_id}/delete")
async def delete_recipe_post(recipe_id: int):
    """
    Удаление рецепта
    
    Args:
        recipe_id: ID рецепта (path parameter)
        
    TODO: Реализовать функцию:
    1. Удалить рецепт через delete_recipe(recipe_id)
    2. Если рецепт не найден (False), вызвать HTTPException со статусом 404
    3. Вернуть JSON-ответ со статусом 200 и сообщением об успехе
       Используй: from fastapi.responses import JSONResponse
       return JSONResponse(content={"message": "Рецепт удален"}, status_code=200)
    """
    pass


# API эндпоинты для работы с JSON (для тестирования)

@app.get("/api/recipes", response_model=List[Recipe])
async def get_recipes_api():
    """
    API эндпоинт для получения всех рецептов в формате JSON
    
    TODO: Реализовать функцию:
    1. Получить все рецепты через get_all_recipes()
    2. Вернуть список рецептов (FastAPI автоматически преобразует в JSON)
    """
    pass


@app.get("/api/recipes/{recipe_id}", response_model=Recipe)
async def get_recipe_api(recipe_id: int):
    """
    API эндпоинт для получения рецепта по ID в формате JSON
    
    Args:
        recipe_id: ID рецепта (path parameter)
        
    TODO: Реализовать функцию:
    1. Получить рецепт по ID через get_recipe_by_id(recipe_id)
    2. Если рецепт не найден, вызвать HTTPException со статусом 404
    3. Вернуть рецепт (FastAPI автоматически преобразует в JSON)
    """
    pass


@app.post("/api/recipes", response_model=Recipe, status_code=status.HTTP_201_CREATED)
async def create_recipe_api(recipe: RecipeCreate):
    """
    API эндпоинт для создания нового рецепта через JSON
    
    Args:
        recipe: Данные нового рецепта (из тела запроса)
        
    TODO: Реализовать функцию:
    1. Создать рецепт через create_recipe(recipe)
    2. Вернуть созданный рецепт со статусом 201
    """
    pass


@app.put("/api/recipes/{recipe_id}", response_model=Recipe)
async def update_recipe_api(recipe_id: int, recipe: RecipeUpdate):
    """
    API эндпоинт для обновления рецепта через JSON
    
    Args:
        recipe_id: ID рецепта (path parameter)
        recipe: Новые данные рецепта (из тела запроса)
        
    TODO: Реализовать функцию:
    1. Обновить рецепт через update_recipe(recipe_id, recipe)
    2. Если рецепт не найден, вызвать HTTPException со статусом 404
    3. Вернуть обновленный рецепт
    """
    pass


@app.delete("/api/recipes/{recipe_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_recipe_api(recipe_id: int):
    """
    API эндпоинт для удаления рецепта
    
    Args:
        recipe_id: ID рецепта (path parameter)
        
    TODO: Реализовать функцию:
    1. Удалить рецепт через delete_recipe(recipe_id)
    2. Если рецепт не найден, вызвать HTTPException со статусом 404
    3. Вернуть пустой ответ со статусом 204
       Используй: from fastapi.responses import Response
       return Response(status_code=status.HTTP_204_NO_CONTENT)
    """
    pass


# Обработчик ошибок 404
from starlette.exceptions import HTTPException as StarletteHTTPException

@app.exception_handler(StarletteHTTPException)
async def not_found_handler(request: Request, exc: StarletteHTTPException):
    """
    Кастомный обработчик ошибки 404
    
    TODO: Реализовать функцию:
    1. Проверить, что статус ошибки 404 (exc.status_code == 404)
    2. Вернуть HTML-страницу с сообщением об ошибке
       Используй: templates.TemplateResponse()
       - Шаблон: "404.html"
       - Контекст: {"request": request}
       - Статус: 404
    """
    if exc.status_code == 404:
        pass  # TODO: вернуть шаблон 404.html


# Обработчик общих ошибок
@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    """
    Кастомный обработчик общих ошибок (500)
    
    TODO: Реализовать функцию:
    1. Вернуть HTML-страницу с сообщением об ошибке
       Используй: templates.TemplateResponse()
       - Шаблон: "500.html"
       - Контекст: {"request": request}
       - Статус: 500
    """
    pass

