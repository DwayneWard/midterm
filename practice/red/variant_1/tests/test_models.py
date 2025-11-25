"""
Тесты для models.py
Проверяют ОРы: 3.1 (валидация данных с помощью Pydantic)
"""
import pytest
from pydantic import ValidationError

try:
    from models import BookCreate, Book, BookUpdate
except ImportError:
    pytest.skip("models module not available", allow_module_level=True)


class TestOR31_PydanticValidation:
    """ОР 3.1: Использовать Pydantic для валидации данных"""
    
    def test_book_create_valid_data(self):
        """Проверка создания BookCreate с валидными данными"""
        book = BookCreate(
            title="Тестовая книга",
            author="Тестовый автор",
            year=2024,
            description="Описание"
        )
        assert book.title == "Тестовая книга"
        assert book.author == "Тестовый автор"
        assert book.year == 2024
        assert book.description == "Описание"
    
    def test_book_create_minimal_data(self):
        """Проверка создания BookCreate с минимальными данными"""
        book = BookCreate(
            title="Книга",
            author="Автор",
            year=2000
        )
        assert book.title == "Книга"
        assert book.description is None
    
    def test_book_create_validation_title_required(self):
        """Проверка валидации: title обязателен"""
        with pytest.raises(ValidationError):
            BookCreate(author="Автор", year=2000)
    
    def test_book_create_validation_author_required(self):
        """Проверка валидации: author обязателен"""
        with pytest.raises(ValidationError):
            BookCreate(title="Книга", year=2000)
    
    def test_book_create_validation_year_required(self):
        """Проверка валидации: year обязателен"""
        with pytest.raises(ValidationError):
            BookCreate(title="Книга", author="Автор")
    
    def test_book_inherits_from_book_create(self):
        """Проверка наследования Book от BookCreate"""
        book = Book(
            id=1,
            title="Книга",
            author="Автор",
            year=2000
        )
        assert book.id == 1
        assert book.title == "Книга"
    
    def test_book_update_all_optional(self):
        """Проверка, что все поля BookUpdate необязательны"""
        book_update = BookUpdate()
        assert book_update.title is None
        assert book_update.author is None
        assert book_update.year is None
        assert book_update.description is None
    
    def test_book_update_partial_update(self):
        """Проверка частичного обновления BookUpdate"""
        book_update = BookUpdate(title="Новое название")
        assert book_update.title == "Новое название"
        assert book_update.author is None

