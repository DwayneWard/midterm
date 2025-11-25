from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import List

from models import Book, BookCreate, BookUpdate
from storage import get_all_books, get_book_by_id, create_book, update_book, delete_book

# Создание экземпляра FastAPI приложения
app = FastAPI(title="Библиотека книг", description="Система управления библиотекой книг")

# Настройка шаблонов
# TODO: Инициализировать Jinja2Templates с указанием директории 'templates'
templates = None

# Подключение статических файлов
# TODO: Подключить статические файлы из директории 'static' с помощью app.mount()
# Используй: app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Главная страница - список всех книг
    
    TODO: Реализовать функцию:
    1. Получить все книги через get_all_books()
    2. Вернуть HTML-страницу используя templates.TemplateResponse()
       - Шаблон: "index.html"
       - Контекст: {"request": request, "books": books}
    """
    pass


@app.get("/books/add", response_class=HTMLResponse)
async def add_book_form(request: Request):
    """
    Форма для добавления новой книги
    
    TODO: Реализовать функцию:
    1. Вернуть HTML-страницу используя templates.TemplateResponse()
       - Шаблон: "book_form.html"
       - Контекст: {"request": request, "book": None, "action": "add"}
    """
    pass


@app.get("/books/{book_id}", response_class=HTMLResponse)
async def read_book(request: Request, book_id: int):
    """
    Страница с детальной информацией о книге
    
    Args:
        request: Объект запроса FastAPI
        book_id: ID книги (path parameter)
        
    TODO: Реализовать функцию:
    1. Получить книгу по ID через get_book_by_id(book_id)
    2. Если книга не найдена (None), вызвать HTTPException со статусом 404
       Используй: raise HTTPException(status_code=404, detail="Книга не найдена")
    3. Вернуть HTML-страницу используя templates.TemplateResponse()
       - Шаблон: "book_detail.html"
       - Контекст: {"request": request, "book": book}
    """
    pass



@app.post("/books/add", response_class=HTMLResponse)
async def create_book_post(request: Request):
    """
    Обработка POST-запроса для создания новой книги
    
    TODO: Реализовать функцию:
    1. Получить данные формы из request.form()
       Используй: form_data = await request.form()
    2. Создать объект BookCreate из данных формы:
       - title = form_data.get("title")
       - author = form_data.get("author")
       - year = int(form_data.get("year"))
       - description = form_data.get("description") или None
    3. Валидировать данные (Pydantic сделает это автоматически при создании BookCreate)
    4. Создать книгу через create_book()
    5. Перенаправить на главную страницу "/"
       Используй: from fastapi.responses import RedirectResponse
       return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
    6. Обработать возможные ошибки валидации (HTTPException со статусом 400)
    """
    pass


@app.get("/books/{book_id}/edit", response_class=HTMLResponse)
async def edit_book_form(request: Request, book_id: int):
    """
    Форма для редактирования книги
    
    Args:
        request: Объект запроса FastAPI
        book_id: ID книги (path parameter)
        
    TODO: Реализовать функцию:
    1. Получить книгу по ID через get_book_by_id(book_id)
    2. Если книга не найдена, вызвать HTTPException со статусом 404
    3. Вернуть HTML-страницу используя templates.TemplateResponse()
       - Шаблон: "book_form.html"
       - Контекст: {"request": request, "book": book, "action": "edit"}
    """
    pass


@app.post("/books/{book_id}/edit", response_class=HTMLResponse)
async def update_book_post(request: Request, book_id: int):
    """
    Обработка POST-запроса для обновления книги
    
    Args:
        request: Объект запроса FastAPI
        book_id: ID книги (path parameter)
        
    TODO: Реализовать функцию:
    1. Получить данные формы из request.form()
       Используй: form_data = await request.form()
    2. Создать объект BookUpdate из данных формы (все поля могут быть None):
       - title = form_data.get("title") или None
       - author = form_data.get("author") или None
       - year = int(form_data.get("year")) если form_data.get("year") не пусто, иначе None
       - description = form_data.get("description") или None
    3. Обновить книгу через update_book(book_id, book_data)
    4. Если книга не найдена (None), вызвать HTTPException со статусом 404
    5. Перенаправить на страницу книги "/books/{book_id}"
       Используй: from fastapi.responses import RedirectResponse
       return RedirectResponse(url=f"/books/{book_id}", status_code=status.HTTP_303_SEE_OTHER)
    6. Обработать возможные ошибки валидации (HTTPException со статусом 400)
    """
    pass


@app.post("/books/{book_id}/delete")
async def delete_book_post(book_id: int):
    """
    Удаление книги
    
    Args:
        book_id: ID книги (path parameter)
        
    TODO: Реализовать функцию:
    1. Удалить книгу через delete_book(book_id)
    2. Если книга не найдена (False), вызвать HTTPException со статусом 404
    3. Вернуть JSON-ответ со статусом 200 и сообщением об успехе
       Используй: from fastapi.responses import JSONResponse
       return JSONResponse(content={"message": "Книга удалена"}, status_code=200)
    """
    pass


# API эндпоинты для работы с JSON (для тестирования)

@app.get("/api/books", response_model=List[Book])
async def get_books_api():
    """
    API эндпоинт для получения всех книг в формате JSON
    
    TODO: Реализовать функцию:
    1. Получить все книги через get_all_books()
    2. Вернуть список книг (FastAPI автоматически преобразует в JSON)
    """
    pass


@app.get("/api/books/{book_id}", response_model=Book)
async def get_book_api(book_id: int):
    """
    API эндпоинт для получения книги по ID в формате JSON
    
    Args:
        book_id: ID книги (path parameter)
        
    TODO: Реализовать функцию:
    1. Получить книгу по ID через get_book_by_id(book_id)
    2. Если книга не найдена, вызвать HTTPException со статусом 404
    3. Вернуть книгу (FastAPI автоматически преобразует в JSON)
    """
    pass


@app.post("/api/books", response_model=Book, status_code=status.HTTP_201_CREATED)
async def create_book_api(book: BookCreate):
    """
    API эндпоинт для создания новой книги через JSON
    
    Args:
        book: Данные новой книги (из тела запроса)
        
    TODO: Реализовать функцию:
    1. Создать книгу через create_book(book)
    2. Вернуть созданную книгу со статусом 201
    """
    pass


@app.put("/api/books/{book_id}", response_model=Book)
async def update_book_api(book_id: int, book: BookUpdate):
    """
    API эндпоинт для обновления книги через JSON
    
    Args:
        book_id: ID книги (path parameter)
        book: Новые данные книги (из тела запроса)
        
    TODO: Реализовать функцию:
    1. Обновить книгу через update_book(book_id, book)
    2. Если книга не найдена, вызвать HTTPException со статусом 404
    3. Вернуть обновленную книгу
    """
    pass


@app.delete("/api/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book_api(book_id: int):
    """
    API эндпоинт для удаления книги
    
    Args:
        book_id: ID книги (path parameter)
        
    TODO: Реализовать функцию:
    1. Удалить книгу через delete_book(book_id)
    2. Если книга не найдена, вызвать HTTPException со статусом 404
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

