"""
Тесты для storage.py
Проверяют ОРы: 3.2 (работа с данными в памяти)
"""
import pytest
from datetime import datetime, date

try:
    from storage import (
        get_all_events,
        get_event_by_id,
        create_event,
        update_event,
        delete_event
    )
    from models import Event, EventCreate
except ImportError:
    pytest.skip("storage module not available", allow_module_level=True)


class TestOR32_DataStorage:
    """ОР 3.2: Работать с данными в памяти"""
    
    def test_get_all_events_returns_list(self):
        """Проверка получения всех событий"""
        events = get_all_events()
        assert isinstance(events, list)
        assert len(events) > 0
    
    def test_get_event_by_id_exists(self):
        """Проверка получения события по существующему ID"""
        # Создаем событие для гарантии, что оно существует
        new_event = EventCreate(
            title="Тестовое событие для проверки",
            event_date=date(2024, 12, 25),
            location="Москва",
            category="conference"
        )
        created = create_event(new_event)
        event_id = created.id
        
        # Проверяем получение события
        event = get_event_by_id(event_id)
        assert event is not None
        assert event.id == event_id
    
    def test_get_event_by_id_not_exists(self):
        """Проверка получения события по несуществующему ID"""
        event = get_event_by_id(99999)
        assert event is None
    
    def test_create_event_adds_to_storage(self):
        """Проверка создания нового события"""
        initial_count = len(get_all_events())
        new_event = EventCreate(
            title="Новое тестовое событие",
            event_date=date(2024, 12, 30),
            location="Санкт-Петербург",
            category="workshop"
        )
        created = create_event(new_event)
        assert created.id is not None
        assert created.created_at is not None
        assert len(get_all_events()) == initial_count + 1
    
    def test_update_event_exists(self):
        """Проверка обновления существующего события"""
        # Создаем событие для обновления
        new_event = EventCreate(
            title="Событие для обновления",
            event_date=date(2024, 12, 20),
            location="Москва",
            category="meeting"
        )
        created = create_event(new_event)
        
        # Обновляем событие
        from models import EventUpdate
        updated_data = EventUpdate(title="Обновленное название")
        updated = update_event(created.id, updated_data)
        assert updated is not None
        assert updated.title == "Обновленное название"
    
    def test_delete_event_exists(self):
        """Проверка удаления существующего события"""
        # Создаем событие для удаления
        new_event = EventCreate(
            title="Событие для удаления",
            event_date=date(2024, 12, 25),
            location="Москва",
            category="conference"
        )
        created = create_event(new_event)
        event_id = created.id
        
        # Удаляем событие
        result = delete_event(event_id)
        assert result is True
        assert get_event_by_id(event_id) is None

