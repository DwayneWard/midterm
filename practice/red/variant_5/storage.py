from typing import List, Optional
from models import Note, NoteCreate, NoteUpdate


# Хранилище заметок в памяти
notes_db: List[Note] = [
    Note(id=1, title="Важные дела", content="Купить продукты, заплатить за квартиру", tags="важное, дела", is_pinned=True),
    Note(id=2, title="Идеи для проекта", content="Добавить авторизацию, улучшить UI", tags="проект, идеи", is_pinned=False),
    Note(id=3, title="Рецепт пирога", content="Мука, яйца, сахар, масло. Выпекать 30 минут при 180°C", tags="рецепты, еда", is_pinned=False),
]


def get_all_notes() -> List[Note]:
    """
    Получить все заметки
    
    Returns:
        Список всех заметок
    """
    return notes_db


def get_note_by_id(note_id: int) -> Optional[Note]:
    """
    Получить заметку по ID
    
    Args:
        note_id: ID заметки
        
    Returns:
        Заметка или None, если заметка не найдена
        
    TODO: Реализовать функцию:
    1. Пройтись по списку notes_db
    2. Найти заметку с указанным id
    3. Вернуть заметку или None, если не найдена
    """
    pass


def create_note(note_data: NoteCreate) -> Note:
    """
    Создать новую заметку
    
    Args:
        note_data: Данные новой заметки (без id)
        
    Returns:
        Созданная заметка с присвоенным id
        
    TODO: Реализовать функцию:
    1. Определить новый id (максимальный id в notes_db + 1, или 1 если список пуст)
    2. Создать объект Note с новым id и данными из note_data
    3. Добавить заметку в notes_db
    4. Вернуть созданную заметку
    """
    pass


def update_note(note_id: int, note_data: NoteUpdate) -> Optional[Note]:
    """
    Обновить заметку
    
    Args:
        note_id: ID заметки для обновления
        note_data: Новые данные заметки
        
    Returns:
        Обновленная заметка или None, если заметка не найдена
        
    TODO: Реализовать функцию:
    1. Найти заметку с указанным id в notes_db
    2. Если заметка не найдена, вернуть None
    3. Обновить поля заметки данными из note_data (только те поля, которые не None)
       Используй: note.field = note_data.field if note_data.field is not None else note.field
    4. Вернуть обновленную заметку
    """
    pass


def delete_note(note_id: int) -> bool:
    """
    Удалить заметку
    
    Args:
        note_id: ID заметки для удаления
        
    Returns:
        True, если заметка удалена, False если не найдена
        
    TODO: Реализовать функцию:
    1. Найти заметку с указанным id в notes_db
    2. Если заметка не найдена, вернуть False
    3. Удалить заметку из notes_db
    4. Вернуть True
    """
    pass

