from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import List

from models import Note, NoteCreate, NoteUpdate
from storage import get_all_notes, get_note_by_id, create_note, update_note, delete_note

# Создание экземпляра FastAPI приложения
app = FastAPI(title="Заметки", description="Система управления заметками")

# Настройка шаблонов
# TODO: Инициализировать Jinja2Templates с указанием директории 'templates'
templates = None

# Подключение статических файлов
# TODO: Подключить статические файлы из директории 'static' с помощью app.mount()
# Используй: app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Главная страница - список всех заметок
    
    TODO: Реализовать функцию:
    1. Получить все заметки через get_all_notes()
    2. Вернуть HTML-страницу используя templates.TemplateResponse()
       - Шаблон: "index.html"
       - Контекст: {"request": request, "notes": notes}
    """
    pass


@app.get("/notes/add", response_class=HTMLResponse)
async def add_note_form(request: Request):
    """
    Форма для добавления новой заметки
    
    TODO: Реализовать функцию:
    1. Вернуть HTML-страницу используя templates.TemplateResponse()
       - Шаблон: "note_form.html"
       - Контекст: {"request": request, "note": None, "action": "add"}
    """
    pass


@app.get("/notes/{note_id}", response_class=HTMLResponse)
async def read_note(request: Request, note_id: int):
    """
    Страница с детальной информацией о заметке
    
    Args:
        request: Объект запроса FastAPI
        note_id: ID заметки (path parameter)
        
    TODO: Реализовать функцию:
    1. Получить заметку по ID через get_note_by_id(note_id)
    2. Если заметка не найдена (None), вызвать HTTPException со статусом 404
       Используй: raise HTTPException(status_code=404, detail="Заметка не найдена")
    3. Вернуть HTML-страницу используя templates.TemplateResponse()
       - Шаблон: "note_detail.html"
       - Контекст: {"request": request, "note": note}
    """
    pass



@app.post("/notes/add", response_class=HTMLResponse)
async def create_note_post(request: Request):
    """
    Обработка POST-запроса для создания новой заметки
    
    TODO: Реализовать функцию:
    1. Получить данные формы из request.form()
       Используй: form_data = await request.form()
    2. Создать объект NoteCreate из данных формы:
       - title = form_data.get("title")
       - content = form_data.get("content")
       - tags = form_data.get("tags") или None
       - is_pinned = form_data.get("is_pinned") == "on" если есть, иначе False
    3. Валидировать данные (Pydantic сделает это автоматически при создании NoteCreate)
    4. Создать заметку через create_note()
    5. Перенаправить на главную страницу "/"
       Используй: from fastapi.responses import RedirectResponse
       return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
    6. Обработать возможные ошибки валидации (HTTPException со статусом 400)
    """
    pass


@app.get("/notes/{note_id}/edit", response_class=HTMLResponse)
async def edit_note_form(request: Request, note_id: int):
    """
    Форма для редактирования заметки
    
    Args:
        request: Объект запроса FastAPI
        note_id: ID заметки (path parameter)
        
    TODO: Реализовать функцию:
    1. Получить заметку по ID через get_note_by_id(note_id)
    2. Если заметка не найдена, вызвать HTTPException со статусом 404
    3. Вернуть HTML-страницу используя templates.TemplateResponse()
       - Шаблон: "note_form.html"
       - Контекст: {"request": request, "note": note, "action": "edit"}
    """
    pass


@app.post("/notes/{note_id}/edit", response_class=HTMLResponse)
async def update_note_post(request: Request, note_id: int):
    """
    Обработка POST-запроса для обновления заметки
    
    Args:
        request: Объект запроса FastAPI
        note_id: ID заметки (path parameter)
        
    TODO: Реализовать функцию:
    1. Получить данные формы из request.form()
       Используй: form_data = await request.form()
    2. Создать объект NoteUpdate из данных формы (все поля могут быть None):
       - title = form_data.get("title") или None
       - content = form_data.get("content") или None
       - tags = form_data.get("tags") или None
       - is_pinned = form_data.get("is_pinned") == "on" если есть, иначе None
    3. Обновить заметку через update_note(note_id, note_data)
    4. Если заметка не найдена (None), вызвать HTTPException со статусом 404
    5. Перенаправить на страницу заметки "/notes/{note_id}"
       Используй: from fastapi.responses import RedirectResponse
       return RedirectResponse(url=f"/notes/{note_id}", status_code=status.HTTP_303_SEE_OTHER)
    6. Обработать возможные ошибки валидации (HTTPException со статусом 400)
    """
    pass


@app.post("/notes/{note_id}/delete")
async def delete_note_post(note_id: int):
    """
    Удаление заметки
    
    Args:
        note_id: ID заметки (path parameter)
        
    TODO: Реализовать функцию:
    1. Удалить заметку через delete_note(note_id)
    2. Если заметка не найдена (False), вызвать HTTPException со статусом 404
    3. Вернуть JSON-ответ со статусом 200 и сообщением об успехе
       Используй: from fastapi.responses import JSONResponse
       return JSONResponse(content={"message": "Заметка удалена"}, status_code=200)
    """
    pass


# API эндпоинты для работы с JSON (для тестирования)

@app.get("/api/notes", response_model=List[Note])
async def get_notes_api():
    """
    API эндпоинт для получения всех заметок в формате JSON
    
    TODO: Реализовать функцию:
    1. Получить все заметки через get_all_notes()
    2. Вернуть список заметок (FastAPI автоматически преобразует в JSON)
    """
    pass


@app.get("/api/notes/{note_id}", response_model=Note)
async def get_note_api(note_id: int):
    """
    API эндпоинт для получения заметки по ID в формате JSON
    
    Args:
        note_id: ID заметки (path parameter)
        
    TODO: Реализовать функцию:
    1. Получить заметку по ID через get_note_by_id(note_id)
    2. Если заметка не найдена, вызвать HTTPException со статусом 404
    3. Вернуть заметку (FastAPI автоматически преобразует в JSON)
    """
    pass


@app.post("/api/notes", response_model=Note, status_code=status.HTTP_201_CREATED)
async def create_note_api(note: NoteCreate):
    """
    API эндпоинт для создания новой заметки через JSON
    
    Args:
        note: Данные новой заметки (из тела запроса)
        
    TODO: Реализовать функцию:
    1. Создать заметку через create_note(note)
    2. Вернуть созданную заметку со статусом 201
    """
    pass


@app.put("/api/notes/{note_id}", response_model=Note)
async def update_note_api(note_id: int, note: NoteUpdate):
    """
    API эндпоинт для обновления заметки через JSON
    
    Args:
        note_id: ID заметки (path parameter)
        note: Новые данные заметки (из тела запроса)
        
    TODO: Реализовать функцию:
    1. Обновить заметку через update_note(note_id, note)
    2. Если заметка не найдена, вызвать HTTPException со статусом 404
    3. Вернуть обновленную заметку
    """
    pass


@app.delete("/api/notes/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_note_api(note_id: int):
    """
    API эндпоинт для удаления заметки
    
    Args:
        note_id: ID заметки (path parameter)
        
    TODO: Реализовать функцию:
    1. Удалить заметку через delete_note(note_id)
    2. Если заметка не найдена, вызвать HTTPException со статусом 404
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

