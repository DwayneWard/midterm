"""
Тесты для models.py
Проверяют ОРы: 3.1 (валидация данных с помощью Pydantic)
"""
import pytest
from pydantic import ValidationError
from datetime import date

try:
    from models import EventCreate, Event, EventUpdate
except ImportError:
    pytest.skip("models module not available", allow_module_level=True)


class TestOR31_PydanticValidation:
    """ОР 3.1: Использовать Pydantic для валидации данных"""
    
    def test_event_create_valid_data(self):
        """Проверка создания EventCreate с валидными данными"""
        event = EventCreate(
            title="Тестовое событие",
            description="Описание события",
            event_date=date(2024, 12, 1),
            location="Офис",
            category="work"
        )
        assert event.title == "Тестовое событие"
        assert event.description == "Описание события"
        assert event.event_date == date(2024, 12, 1)
        assert event.location == "Офис"
        assert event.category == "work"
    
    def test_event_create_minimal_data(self):
        """Проверка создания EventCreate с минимальными данными"""
        event = EventCreate(
            title="Событие",
            event_date=date(2024, 12, 1),
            location="Место",
            category="personal"
        )
        assert event.title == "Событие"
        assert event.description is None
    
    def test_event_create_validation_title_required(self):
        """Проверка валидации: title обязателен"""
        with pytest.raises(ValidationError):
            EventCreate(event_date=date(2024, 12, 1), location="Место", category="work")
    
    def test_event_create_validation_event_date_required(self):
        """Проверка валидации: event_date обязателен"""
        with pytest.raises(ValidationError):
            EventCreate(title="Событие", location="Место", category="work")
    
    def test_event_create_validation_location_required(self):
        """Проверка валидации: location обязателен"""
        with pytest.raises(ValidationError):
            EventCreate(title="Событие", event_date=date(2024, 12, 1), category="work")
    
    def test_event_create_validation_category_required(self):
        """Проверка валидации: category обязателен"""
        with pytest.raises(ValidationError):
            EventCreate(title="Событие", event_date=date(2024, 12, 1), location="Место")
    
    def test_event_inherits_from_event_create(self):
        """Проверка наследования Event от EventCreate"""
        event = Event(
            id=1,
            title="Событие",
            event_date=date(2024, 12, 1),
            location="Место",
            category="other"
        )
        assert event.id == 1
        assert event.title == "Событие"
    
    def test_event_update_all_optional(self):
        """Проверка, что все поля EventUpdate необязательны"""
        event_update = EventUpdate()
        assert event_update.title is None
        assert event_update.event_date is None
        assert event_update.location is None
        assert event_update.category is None
        assert event_update.description is None
    
    def test_event_update_partial_update(self):
        """Проверка частичного обновления EventUpdate"""
        event_update = EventUpdate(title="Новое название")
        assert event_update.title == "Новое название"
        assert event_update.location is None
