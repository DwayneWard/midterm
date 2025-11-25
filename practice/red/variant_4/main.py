from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import List

from models import Product, ProductCreate, ProductUpdate
from storage import get_all_products, get_product_by_id, create_product, update_product, delete_product

# Создание экземпляра FastAPI приложения
app = FastAPI(title="Каталог продуктов", description="Система управления продуктами/товарами")

# Настройка шаблонов
# TODO: Инициализировать Jinja2Templates с указанием директории 'templates'
templates = None

# Подключение статических файлов
# TODO: Подключить статические файлы из директории 'static' с помощью app.mount()
# Используй: app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Главная страница - список всех продуктов
    
    TODO: Реализовать функцию:
    1. Получить все продукты через get_all_products()
    2. Вернуть HTML-страницу используя templates.TemplateResponse()
       - Шаблон: "index.html"
       - Контекст: {"request": request, "products": products}
    """
    pass


@app.get("/products/add", response_class=HTMLResponse)
async def add_product_form(request: Request):
    """
    Форма для добавления нового продукта
    
    TODO: Реализовать функцию:
    1. Вернуть HTML-страницу используя templates.TemplateResponse()
       - Шаблон: "product_form.html"
       - Контекст: {"request": request, "product": None, "action": "add"}
    """
    pass


@app.get("/products/{product_id}", response_class=HTMLResponse)
async def read_product(request: Request, product_id: int):
    """
    Страница с детальной информацией о продукте
    
    Args:
        request: Объект запроса FastAPI
        product_id: ID продукта (path parameter)
        
    TODO: Реализовать функцию:
    1. Получить продукт по ID через get_product_by_id(product_id)
    2. Если продукт не найден (None), вызвать HTTPException со статусом 404
       Используй: raise HTTPException(status_code=404, detail="Продукт не найден")
    3. Вернуть HTML-страницу используя templates.TemplateResponse()
       - Шаблон: "product_detail.html"
       - Контекст: {"request": request, "product": product}
    """
    pass



@app.post("/products/add", response_class=HTMLResponse)
async def create_product_post(request: Request):
    """
    Обработка POST-запроса для создания нового продукта
    
    TODO: Реализовать функцию:
    1. Получить данные формы из request.form()
       Используй: form_data = await request.form()
    2. Создать объект ProductCreate из данных формы:
       - name = form_data.get("name")
       - description = form_data.get("description") или None
       - price = float(form_data.get("price"))  # Преобразовать строку в float
       - category = form_data.get("category")  # "electronics", "clothing", "food" или "other"
       - stock = int(form_data.get("stock"))  # Преобразовать строку в int
    3. Валидировать данные (Pydantic сделает это автоматически при создании ProductCreate)
    4. Создать продукт через create_product()
    5. Перенаправить на главную страницу "/"
       Используй: from fastapi.responses import RedirectResponse
       return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
    6. Обработать возможные ошибки валидации (HTTPException со статусом 400)
    """
    pass


@app.get("/products/{product_id}/edit", response_class=HTMLResponse)
async def edit_product_form(request: Request, product_id: int):
    """
    Форма для редактирования продукта
    
    Args:
        request: Объект запроса FastAPI
        product_id: ID продукта (path parameter)
        
    TODO: Реализовать функцию:
    1. Получить продукт по ID через get_product_by_id(product_id)
    2. Если продукт не найден, вызвать HTTPException со статусом 404
    3. Вернуть HTML-страницу используя templates.TemplateResponse()
       - Шаблон: "product_form.html"
       - Контекст: {"request": request, "product": product, "action": "edit"}
    """
    pass


@app.post("/products/{product_id}/edit", response_class=HTMLResponse)
async def update_product_post(request: Request, product_id: int):
    """
    Обработка POST-запроса для обновления продукта
    
    Args:
        request: Объект запроса FastAPI
        product_id: ID продукта (path parameter)
        
    TODO: Реализовать функцию:
    1. Получить данные формы из request.form()
       Используй: form_data = await request.form()
    2. Создать объект ProductUpdate из данных формы (все поля могут быть None):
       - name = form_data.get("name") или None
       - description = form_data.get("description") или None
       - price = float(form_data.get("price")) если form_data.get("price") не пусто, иначе None
       - category = form_data.get("category") или None
       - stock = int(form_data.get("stock")) если form_data.get("stock") не пусто, иначе None
    3. Обновить продукт через update_product(product_id, product_data)
    4. Если продукт не найден (None), вызвать HTTPException со статусом 404
    5. Перенаправить на страницу продукта "/products/{product_id}"
       Используй: from fastapi.responses import RedirectResponse
       return RedirectResponse(url=f"/products/{product_id}", status_code=status.HTTP_303_SEE_OTHER)
    6. Обработать возможные ошибки валидации (HTTPException со статусом 400)
    """
    pass


@app.post("/products/{product_id}/delete")
async def delete_product_post(product_id: int):
    """
    Удаление продукта
    
    Args:
        product_id: ID продукта (path parameter)
        
    TODO: Реализовать функцию:
    1. Удалить продукт через delete_product(product_id)
    2. Если продукт не найден (False), вызвать HTTPException со статусом 404
    3. Вернуть JSON-ответ со статусом 200 и сообщением об успехе
       Используй: from fastapi.responses import JSONResponse
       return JSONResponse(content={"message": "Продукт удален"}, status_code=200)
    """
    pass


# API эндпоинты для работы с JSON (для тестирования)

@app.get("/api/products", response_model=List[Product])
async def get_products_api():
    """
    API эндпоинт для получения всех продуктов в формате JSON
    
    TODO: Реализовать функцию:
    1. Получить все продукты через get_all_products()
    2. Вернуть список продуктов (FastAPI автоматически преобразует в JSON)
    """
    pass


@app.get("/api/products/{product_id}", response_model=Product)
async def get_product_api(product_id: int):
    """
    API эндпоинт для получения продукта по ID в формате JSON
    
    Args:
        product_id: ID продукта (path parameter)
        
    TODO: Реализовать функцию:
    1. Получить продукт по ID через get_product_by_id(product_id)
    2. Если продукт не найден, вызвать HTTPException со статусом 404
    3. Вернуть продукт (FastAPI автоматически преобразует в JSON)
    """
    pass


@app.post("/api/products", response_model=Product, status_code=status.HTTP_201_CREATED)
async def create_product_api(product: ProductCreate):
    """
    API эндпоинт для создания нового продукта через JSON
    
    Args:
        product: Данные нового продукта (из тела запроса)
        
    TODO: Реализовать функцию:
    1. Создать продукт через create_product(product)
    2. Вернуть созданный продукт со статусом 201
    """
    pass


@app.put("/api/products/{product_id}", response_model=Product)
async def update_product_api(product_id: int, product: ProductUpdate):
    """
    API эндпоинт для обновления продукта через JSON
    
    Args:
        product_id: ID продукта (path parameter)
        product: Новые данные продукта (из тела запроса)
        
    TODO: Реализовать функцию:
    1. Обновить продукт через update_product(product_id, product)
    2. Если продукт не найден, вызвать HTTPException со статусом 404
    3. Вернуть обновленный продукт
    """
    pass


@app.delete("/api/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product_api(product_id: int):
    """
    API эндпоинт для удаления продукта
    
    Args:
        product_id: ID продукта (path parameter)
        
    TODO: Реализовать функцию:
    1. Удалить продукт через delete_product(product_id)
    2. Если продукт не найден, вызвать HTTPException со статусом 404
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

