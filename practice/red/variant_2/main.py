from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import List

from models import Task, TaskCreate, TaskUpdate
from storage import get_all_tasks, get_task_by_id, create_task, update_task, delete_task

# Создание экземпляра FastAPI приложения
app = FastAPI(title="Список задач", description="Система управления задачами (Todo List)")

# Настройка шаблонов
# TODO: Инициализировать Jinja2Templates с указанием директории 'templates'
templates = None

# Подключение статических файлов
# TODO: Подключить статические файлы из директории 'static' с помощью app.mount()
# Используй: app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Главная страница - список всех задач
    
    TODO: Реализовать функцию:
    1. Получить все задачи через get_all_tasks()
    2. Вернуть HTML-страницу используя templates.TemplateResponse()
       - Шаблон: "index.html"
       - Контекст: {"request": request, "tasks": tasks}
    """
    pass


@app.get("/tasks/add", response_class=HTMLResponse)
async def add_task_form(request: Request):
    """
    Форма для добавления новой задачи
    
    TODO: Реализовать функцию:
    1. Вернуть HTML-страницу используя templates.TemplateResponse()
       - Шаблон: "task_form.html"
       - Контекст: {"request": request, "task": None, "action": "add"}
    """
    pass


@app.get("/tasks/{task_id}", response_class=HTMLResponse)
async def read_task(request: Request, task_id: int):
    """
    Страница с детальной информацией о задаче
    
    Args:
        request: Объект запроса FastAPI
        task_id: ID задачи (path parameter)
        
    TODO: Реализовать функцию:
    1. Получить задачу по ID через get_task_by_id(task_id)
    2. Если задача не найдена (None), вызвать HTTPException со статусом 404
       Используй: raise HTTPException(status_code=404, detail="Задача не найдена")
    3. Вернуть HTML-страницу используя templates.TemplateResponse()
       - Шаблон: "task_detail.html"
       - Контекст: {"request": request, "task": task}
    """
    pass



@app.post("/tasks/add", response_class=HTMLResponse)
async def create_task_post(request: Request):
    """
    Обработка POST-запроса для создания новой задачи
    
    TODO: Реализовать функцию:
    1. Получить данные формы из request.form()
       Используй: form_data = await request.form()
    2. Создать объект TaskCreate из данных формы:
       - title = form_data.get("title")
       - description = form_data.get("description") или None
       - priority = form_data.get("priority")  # "low", "medium" или "high"
       - completed = form_data.get("completed") == "on" если есть, иначе False
    3. Валидировать данные (Pydantic сделает это автоматически при создании TaskCreate)
    4. Создать задачу через create_task()
    5. Перенаправить на главную страницу "/"
       Используй: from fastapi.responses import RedirectResponse
       return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
    6. Обработать возможные ошибки валидации (HTTPException со статусом 400)
    """
    pass


@app.get("/tasks/{task_id}/edit", response_class=HTMLResponse)
async def edit_task_form(request: Request, task_id: int):
    """
    Форма для редактирования задачи
    
    Args:
        request: Объект запроса FastAPI
        task_id: ID задачи (path parameter)
        
    TODO: Реализовать функцию:
    1. Получить задачу по ID через get_task_by_id(task_id)
    2. Если задача не найдена, вызвать HTTPException со статусом 404
    3. Вернуть HTML-страницу используя templates.TemplateResponse()
       - Шаблон: "task_form.html"
       - Контекст: {"request": request, "task": task, "action": "edit"}
    """
    pass


@app.post("/tasks/{task_id}/edit", response_class=HTMLResponse)
async def update_task_post(request: Request, task_id: int):
    """
    Обработка POST-запроса для обновления задачи
    
    Args:
        request: Объект запроса FastAPI
        task_id: ID задачи (path parameter)
        
    TODO: Реализовать функцию:
    1. Получить данные формы из request.form()
       Используй: form_data = await request.form()
    2. Создать объект TaskUpdate из данных формы (все поля могут быть None):
       - title = form_data.get("title") или None
       - description = form_data.get("description") или None
       - priority = form_data.get("priority") или None
       - completed = form_data.get("completed") == "on" если есть, иначе None
    3. Обновить задачу через update_task(task_id, task_data)
    4. Если задача не найдена (None), вызвать HTTPException со статусом 404
    5. Перенаправить на страницу задачи "/tasks/{task_id}"
       Используй: from fastapi.responses import RedirectResponse
       return RedirectResponse(url=f"/tasks/{task_id}", status_code=status.HTTP_303_SEE_OTHER)
    6. Обработать возможные ошибки валидации (HTTPException со статусом 400)
    """
    pass


@app.post("/tasks/{task_id}/delete")
async def delete_task_post(task_id: int):
    """
    Удаление задачи
    
    Args:
        task_id: ID задачи (path parameter)
        
    TODO: Реализовать функцию:
    1. Удалить задачу через delete_task(task_id)
    2. Если задача не найдена (False), вызвать HTTPException со статусом 404
    3. Вернуть JSON-ответ со статусом 200 и сообщением об успехе
       Используй: from fastapi.responses import JSONResponse
       return JSONResponse(content={"message": "Задача удалена"}, status_code=200)
    """
    pass


# API эндпоинты для работы с JSON (для тестирования)

@app.get("/api/tasks", response_model=List[Task])
async def get_tasks_api():
    """
    API эндпоинт для получения всех задач в формате JSON
    
    TODO: Реализовать функцию:
    1. Получить все задачи через get_all_tasks()
    2. Вернуть список задач (FastAPI автоматически преобразует в JSON)
    """
    pass


@app.get("/api/tasks/{task_id}", response_model=Task)
async def get_task_api(task_id: int):
    """
    API эндпоинт для получения задачи по ID в формате JSON
    
    Args:
        task_id: ID задачи (path parameter)
        
    TODO: Реализовать функцию:
    1. Получить задачу по ID через get_task_by_id(task_id)
    2. Если задача не найдена, вызвать HTTPException со статусом 404
    3. Вернуть задачу (FastAPI автоматически преобразует в JSON)
    """
    pass


@app.post("/api/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
async def create_task_api(task: TaskCreate):
    """
    API эндпоинт для создания новой задачи через JSON
    
    Args:
        task: Данные новой задачи (из тела запроса)
        
    TODO: Реализовать функцию:
    1. Создать задачу через create_task(task)
    2. Вернуть созданную задачу со статусом 201
    """
    pass


@app.put("/api/tasks/{task_id}", response_model=Task)
async def update_task_api(task_id: int, task: TaskUpdate):
    """
    API эндпоинт для обновления задачи через JSON
    
    Args:
        task_id: ID задачи (path parameter)
        task: Новые данные задачи (из тела запроса)
        
    TODO: Реализовать функцию:
    1. Обновить задачу через update_task(task_id, task)
    2. Если задача не найдена, вызвать HTTPException со статусом 404
    3. Вернуть обновленную задачу
    """
    pass


@app.delete("/api/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task_api(task_id: int):
    """
    API эндпоинт для удаления задачи
    
    Args:
        task_id: ID задачи (path parameter)
        
    TODO: Реализовать функцию:
    1. Удалить задачу через delete_task(task_id)
    2. Если задача не найдена, вызвать HTTPException со статусом 404
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

