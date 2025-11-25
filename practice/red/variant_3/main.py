from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import List
from datetime import date

from models import Event, EventCreate, EventUpdate
from storage import get_all_events, get_event_by_id, create_event, update_event, delete_event

# Создание экземпляра FastAPI приложения
app = FastAPI(title="Календарь событий", description="Система управления событиями/мероприятиями")

# Настройка шаблонов
# TODO: Инициализировать Jinja2Templates с указанием директории 'templates'
templates = None

# Подключение статических файлов
# TODO: Подключить статические файлы из директории 'static' с помощью app.mount()
# Используй: app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Главная страница - список всех событий
    
    TODO: Реализовать функцию:
    1. Получить все события через get_all_events()
    2. Вернуть HTML-страницу используя templates.TemplateResponse()
       - Шаблон: "index.html"
       - Контекст: {"request": request, "events": events}
    """
    pass


@app.get("/events/add", response_class=HTMLResponse)
async def add_event_form(request: Request):
    """
    Форма для добавления нового события
    
    TODO: Реализовать функцию:
    1. Вернуть HTML-страницу используя templates.TemplateResponse()
       - Шаблон: "event_form.html"
       - Контекст: {"request": request, "event": None, "action": "add"}
    """
    pass


@app.get("/events/{event_id}", response_class=HTMLResponse)
async def read_event(request: Request, event_id: int):
    """
    Страница с детальной информацией о событии
    
    Args:
        request: Объект запроса FastAPI
        event_id: ID события (path parameter)
        
    TODO: Реализовать функцию:
    1. Получить событие по ID через get_event_by_id(event_id)
    2. Если событие не найдено (None), вызвать HTTPException со статусом 404
       Используй: raise HTTPException(status_code=404, detail="Событие не найдено")
    3. Вернуть HTML-страницу используя templates.TemplateResponse()
       - Шаблон: "event_detail.html"
       - Контекст: {"request": request, "event": event}
    """
    pass



@app.post("/events/add", response_class=HTMLResponse)
async def create_event_post(request: Request):
    """
    Обработка POST-запроса для создания нового события
    
    TODO: Реализовать функцию:
    1. Получить данные формы из request.form()
       Используй: form_data = await request.form()
    2. Создать объект EventCreate из данных формы:
       - title = form_data.get("title")
       - description = form_data.get("description") или None
       - event_date = date.fromisoformat(form_data.get("event_date"))  # Преобразовать строку в date
       - location = form_data.get("location")
       - category = form_data.get("category")  # "work", "personal" или "other"
    3. Валидировать данные (Pydantic сделает это автоматически при создании EventCreate)
    4. Создать событие через create_event()
    5. Перенаправить на главную страницу "/"
       Используй: from fastapi.responses import RedirectResponse
       return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
    6. Обработать возможные ошибки валидации (HTTPException со статусом 400)
    """
    pass


@app.get("/events/{event_id}/edit", response_class=HTMLResponse)
async def edit_event_form(request: Request, event_id: int):
    """
    Форма для редактирования события
    
    Args:
        request: Объект запроса FastAPI
        event_id: ID события (path parameter)
        
    TODO: Реализовать функцию:
    1. Получить событие по ID через get_event_by_id(event_id)
    2. Если событие не найдено, вызвать HTTPException со статусом 404
    3. Вернуть HTML-страницу используя templates.TemplateResponse()
       - Шаблон: "event_form.html"
       - Контекст: {"request": request, "event": event, "action": "edit"}
    """
    pass


@app.post("/events/{event_id}/edit", response_class=HTMLResponse)
async def update_event_post(request: Request, event_id: int):
    """
    Обработка POST-запроса для обновления события
    
    Args:
        request: Объект запроса FastAPI
        event_id: ID события (path parameter)
        
    TODO: Реализовать функцию:
    1. Получить данные формы из request.form()
       Используй: form_data = await request.form()
    2. Создать объект EventUpdate из данных формы (все поля могут быть None):
       - title = form_data.get("title") или None
       - description = form_data.get("description") или None
       - event_date = date.fromisoformat(form_data.get("event_date")) если form_data.get("event_date") не пусто, иначе None
       - location = form_data.get("location") или None
       - category = form_data.get("category") или None
    3. Обновить событие через update_event(event_id, event_data)
    4. Если событие не найдено (None), вызвать HTTPException со статусом 404
    5. Перенаправить на страницу события "/events/{event_id}"
       Используй: from fastapi.responses import RedirectResponse
       return RedirectResponse(url=f"/events/{event_id}", status_code=status.HTTP_303_SEE_OTHER)
    6. Обработать возможные ошибки валидации (HTTPException со статусом 400)
    """
    pass


@app.post("/events/{event_id}/delete")
async def delete_event_post(event_id: int):
    """
    Удаление события
    
    Args:
        event_id: ID события (path parameter)
        
    TODO: Реализовать функцию:
    1. Удалить событие через delete_event(event_id)
    2. Если событие не найдено (False), вызвать HTTPException со статусом 404
    3. Вернуть JSON-ответ со статусом 200 и сообщением об успехе
       Используй: from fastapi.responses import JSONResponse
       return JSONResponse(content={"message": "Событие удалено"}, status_code=200)
    """
    pass


# API эндпоинты для работы с JSON (для тестирования)

@app.get("/api/events", response_model=List[Event])
async def get_events_api():
    """
    API эндпоинт для получения всех событий в формате JSON
    
    TODO: Реализовать функцию:
    1. Получить все события через get_all_events()
    2. Вернуть список событий (FastAPI автоматически преобразует в JSON)
    """
    pass


@app.get("/api/events/{event_id}", response_model=Event)
async def get_event_api(event_id: int):
    """
    API эндпоинт для получения события по ID в формате JSON
    
    Args:
        event_id: ID события (path parameter)
        
    TODO: Реализовать функцию:
    1. Получить событие по ID через get_event_by_id(event_id)
    2. Если событие не найдено, вызвать HTTPException со статусом 404
    3. Вернуть событие (FastAPI автоматически преобразует в JSON)
    """
    pass


@app.post("/api/events", response_model=Event, status_code=status.HTTP_201_CREATED)
async def create_event_api(event: EventCreate):
    """
    API эндпоинт для создания нового события через JSON
    
    Args:
        event: Данные нового события (из тела запроса)
        
    TODO: Реализовать функцию:
    1. Создать событие через create_event(event)
    2. Вернуть созданное событие со статусом 201
    """
    pass


@app.put("/api/events/{event_id}", response_model=Event)
async def update_event_api(event_id: int, event: EventUpdate):
    """
    API эндпоинт для обновления события через JSON
    
    Args:
        event_id: ID события (path parameter)
        event: Новые данные события (из тела запроса)
        
    TODO: Реализовать функцию:
    1. Обновить событие через update_event(event_id, event)
    2. Если событие не найдено, вызвать HTTPException со статусом 404
    3. Вернуть обновленное событие
    """
    pass


@app.delete("/api/events/{event_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_event_api(event_id: int):
    """
    API эндпоинт для удаления события
    
    Args:
        event_id: ID события (path parameter)
        
    TODO: Реализовать функцию:
    1. Удалить событие через delete_event(event_id)
    2. Если событие не найдено, вызвать HTTPException со статусом 404
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

