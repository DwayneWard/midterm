"""
Тесты для models.py
Проверяют ОРы: 3.1 (валидация данных с помощью Pydantic)
"""
import pytest
from pydantic import ValidationError

try:
    from models import NoteCreate, Note, NoteUpdate
except ImportError:
    pytest.skip("models module not available", allow_module_level=True)


class TestOR31_PydanticValidation:
    """ОР 3.1: Использовать Pydantic для валидации данных"""
    
    def test_note_create_valid_data(self):
        """Проверка создания NoteCreate с валидными данными"""
        note = NoteCreate(
            title="Тестовая заметка",
            content="Содержание заметки",
            tags="тег1, тег2",
            is_pinned=True
        )
        assert note.title == "Тестовая заметка"
        assert note.content == "Содержание заметки"
        assert note.tags == "тег1, тег2"
        assert note.is_pinned == True
    
    def test_note_create_minimal_data(self):
        """Проверка создания NoteCreate с минимальными данными"""
        note = NoteCreate(
            title="Заметка",
            content="Содержание"
        )
        assert note.title == "Заметка"
        assert note.tags is None
        assert note.is_pinned == False
    
    def test_note_create_validation_title_required(self):
        """Проверка валидации: title обязателен"""
        with pytest.raises(ValidationError):
            NoteCreate(content="Содержание")
    
    def test_note_create_validation_content_required(self):
        """Проверка валидации: content обязателен"""
        with pytest.raises(ValidationError):
            NoteCreate(title="Заметка")
    
    def test_note_inherits_from_note_create(self):
        """Проверка наследования Note от NoteCreate"""
        note = Note(
            id=1,
            title="Заметка",
            content="Содержание",
            is_pinned=False
        )
        assert note.id == 1
        assert note.title == "Заметка"
    
    def test_note_update_all_optional(self):
        """Проверка, что все поля NoteUpdate необязательны"""
        note_update = NoteUpdate()
        assert note_update.title is None
        assert note_update.content is None
        assert note_update.tags is None
        assert note_update.is_pinned is None
    
    def test_note_update_partial_update(self):
        """Проверка частичного обновления NoteUpdate"""
        note_update = NoteUpdate(title="Новое название")
        assert note_update.title == "Новое название"
        assert note_update.content is None
