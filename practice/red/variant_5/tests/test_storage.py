"""
Тесты для storage.py
Проверяют ОРы: 3.2 (работа с данными в памяти)
"""
import pytest

try:
    from storage import (
        get_all_notes,
        get_note_by_id,
        create_note,
        update_note,
        delete_note
    )
    from models import Note, NoteCreate
except ImportError:
    pytest.skip("storage module not available", allow_module_level=True)


class TestOR32_DataStorage:
    """ОР 3.2: Работать с данными в памяти"""
    
    def test_get_all_notes_returns_list(self):
        """Проверка получения всех заметок"""
        notes = get_all_notes()
        assert isinstance(notes, list)
        assert len(notes) > 0
    
    def test_get_note_by_id_exists(self):
        """Проверка получения заметки по существующему ID"""
        # Создаем заметку для гарантии, что она существует
        new_note = NoteCreate(
            title="Тестовая заметка для проверки",
            content="Содержание заметки",
            tags="тест"
        )
        created = create_note(new_note)
        note_id = created.id
        
        # Проверяем получение заметки
        note = get_note_by_id(note_id)
        assert note is not None
        assert note.id == note_id
    
    def test_get_note_by_id_not_exists(self):
        """Проверка получения заметки по несуществующему ID"""
        note = get_note_by_id(99999)
        assert note is None
    
    def test_create_note_adds_to_storage(self):
        """Проверка создания новой заметки"""
        initial_count = len(get_all_notes())
        new_note = NoteCreate(
            title="Новая тестовая заметка",
            content="Содержание новой заметки",
            tags="новая, тест"
        )
        created = create_note(new_note)
        assert created.id is not None
        assert created.title == "Новая тестовая заметка"
        assert len(get_all_notes()) == initial_count + 1
    
    def test_update_note_exists(self):
        """Проверка обновления существующей заметки"""
        # Создаем заметку для обновления
        new_note = NoteCreate(
            title="Заметка для обновления",
            content="Содержание",
            tags="обновление"
        )
        created = create_note(new_note)
        
        # Обновляем заметку
        from models import NoteUpdate
        updated_data = NoteUpdate(title="Обновленное название")
        updated = update_note(created.id, updated_data)
        assert updated is not None
        assert updated.title == "Обновленное название"
    
    def test_update_note_not_exists(self):
        """Проверка обновления несуществующей заметки"""
        from models import NoteUpdate
        updated_data = NoteUpdate(title="Тест")
        result = update_note(99999, updated_data)
        assert result is None
    
    def test_delete_note_exists(self):
        """Проверка удаления существующей заметки"""
        # Создаем заметку для удаления
        new_note = NoteCreate(
            title="Заметка для удаления",
            content="Содержание",
            tags="удаление"
        )
        created = create_note(new_note)
        note_id = created.id
        
        # Удаляем заметку
        result = delete_note(note_id)
        assert result is True
        assert get_note_by_id(note_id) is None
    
    def test_delete_note_not_exists(self):
        """Проверка удаления несуществующей заметки"""
        result = delete_note(99999)
        assert result is False
