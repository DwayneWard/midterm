from typing import List, Optional
from models import Book, BookCreate, BookUpdate


# Хранилище книг в памяти
books_db: List[Book] = [
    Book(id=1, title="Война и мир", author="Лев Толстой", year=1869, description="Эпический роман о России эпохи Наполеоновских войн"),
    Book(id=2, title="Преступление и наказание", author="Фёдор Достоевский", year=1866, description="Психологический роман о студенте Раскольникове"),
    Book(id=3, title="Мастер и Маргарита", author="Михаил Булгаков", year=1967, description="Мистический роман о дьяволе в Москве"),
]


def get_all_books() -> List[Book]:
    """
    Получить все книги
    
    Returns:
        Список всех книг
    """
    return books_db


def get_book_by_id(book_id: int) -> Optional[Book]:
    """
    Получить книгу по ID
    
    Args:
        book_id: ID книги
        
    Returns:
        Книга или None, если книга не найдена
        
    TODO: Реализовать функцию:
    1. Пройтись по списку books_db
    2. Найти книгу с указанным id
    3. Вернуть книгу или None, если не найдена
    """
    pass


def create_book(book_data: BookCreate) -> Book:
    """
    Создать новую книгу
    
    Args:
        book_data: Данные новой книги (без id)
        
    Returns:
        Созданная книга с присвоенным id
        
    TODO: Реализовать функцию:
    1. Определить новый id (максимальный id в books_db + 1, или 1 если список пуст)
    2. Создать объект Book с новым id и данными из book_data
    3. Добавить книгу в books_db
    4. Вернуть созданную книгу
    """
    pass


def update_book(book_id: int, book_data: BookUpdate) -> Optional[Book]:
    """
    Обновить книгу
    
    Args:
        book_id: ID книги для обновления
        book_data: Новые данные книги
        
    Returns:
        Обновленная книга или None, если книга не найдена
        
    TODO: Реализовать функцию:
    1. Найти книгу с указанным id в books_db
    2. Если книга не найдена, вернуть None
    3. Обновить поля книги данными из book_data (только те поля, которые не None)
       Используй: book.field = book_data.field if book_data.field is not None else book.field
    4. Вернуть обновленную книгу
    """
    pass


def delete_book(book_id: int) -> bool:
    """
    Удалить книгу
    
    Args:
        book_id: ID книги для удаления
        
    Returns:
        True, если книга удалена, False если не найдена
        
    TODO: Реализовать функцию:
    1. Найти книгу с указанным id в books_db
    2. Если книга не найдена, вернуть False
    3. Удалить книгу из books_db
    4. Вернуть True
    """
    pass

