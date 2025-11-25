"""
Тесты для storage.py
Проверяют ОРы: 3.2 (работа с данными в памяти)
"""
import pytest

try:
    from storage import (
        get_all_books,
        get_book_by_id,
        create_book,
        update_book,
        delete_book
    )
    from models import Book, BookCreate
except ImportError:
    pytest.skip("storage module not available", allow_module_level=True)


class TestOR32_DataStorage:
    """ОР 3.2: Работать с данными в памяти"""
    
    def test_get_all_books_returns_list(self):
        """Проверка получения всех книг"""
        books = get_all_books()
        assert isinstance(books, list)
        assert len(books) > 0
    
    def test_get_book_by_id_exists(self):
        """Проверка получения книги по существующему ID"""
        # Создаем книгу для гарантии, что она существует
        new_book = BookCreate(
            title="Тестовая книга для проверки",
            author="Тестовый автор",
            year=2024
        )
        created = create_book(new_book)
        book_id = created.id
        
        # Проверяем получение книги
        book = get_book_by_id(book_id)
        assert book is not None
        assert book.id == book_id
    
    def test_get_book_by_id_not_exists(self):
        """Проверка получения книги по несуществующему ID"""
        book = get_book_by_id(99999)
        assert book is None
    
    def test_create_book_adds_to_storage(self):
        """Проверка создания новой книги"""
        initial_count = len(get_all_books())
        new_book = BookCreate(
            title="Новая тестовая книга",
            author="Тестовый автор",
            year=2024
        )
        created = create_book(new_book)
        assert created.id is not None
        assert created.title == "Новая тестовая книга"
        assert len(get_all_books()) == initial_count + 1
    
    def test_update_book_exists(self):
        """Проверка обновления существующей книги"""
        # Создаем книгу для обновления
        new_book = BookCreate(
            title="Книга для обновления",
            author="Автор",
            year=2020
        )
        created = create_book(new_book)
        
        # Обновляем книгу
        updated_data = Book(
            id=created.id,
            title="Обновленное название",
            author=created.author,
            year=created.year,
            description=created.description
        )
        updated = update_book(created.id, updated_data)
        assert updated is not None
        assert updated.title == "Обновленное название"
    
    def test_update_book_not_exists(self):
        """Проверка обновления несуществующей книги"""
        updated_data = Book(
            id=99999,
            title="Тест",
            author="Автор",
            year=2000
        )
        result = update_book(99999, updated_data)
        assert result is None
    
    def test_delete_book_exists(self):
        """Проверка удаления существующей книги"""
        # Создаем книгу для удаления
        new_book = BookCreate(
            title="Книга для удаления",
            author="Автор",
            year=2020
        )
        created = create_book(new_book)
        book_id = created.id
        
        # Удаляем книгу
        result = delete_book(book_id)
        assert result is True
        assert get_book_by_id(book_id) is None
    
    def test_delete_book_not_exists(self):
        """Проверка удаления несуществующей книги"""
        result = delete_book(99999)
        assert result is False

