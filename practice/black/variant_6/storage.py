from typing import List, Optional
from datetime import datetime
from models import Article, ArticleCreate, ArticleUpdate


# Хранилище статей в памяти
articles_db: List[Article] = [
    Article(id=1, title="Введение в FastAPI", content="FastAPI - современный веб-фреймворк", author="Иван Иванов", category="tech", published=True, created_at=datetime.now()),
    Article(id=2, title="Квантовая физика", content="Основы квантовой механики", author="Мария Петрова", category="science", published=False, created_at=datetime.now()),
    Article(id=3, title="Стратегии бизнеса", content="Как построить успешный бизнес", author="Петр Сидоров", category="business", published=True, created_at=datetime.now()),
]


def get_all_articles() -> List[Article]:
    """
    Получить все статьи
    
    Returns:
        Список всех статей
    """
    return articles_db


def get_article_by_id(article_id: int) -> Optional[Article]:
    """
    Получить статью по ID
    
    Args:
        article_id: ID статьи
        
    Returns:
        Статья или None, если статья не найдена
        
    TODO: Реализовать функцию:
    1. Пройтись по списку articles_db
    2. Найти статью с указанным id
    3. Вернуть статью или None, если не найдена
    """
    pass


def create_article(article_data: ArticleCreate) -> Article:
    """
    Создать новую статью
    
    Args:
        article_data: Данные новой статьи (без id и created_at)
        
    Returns:
        Созданная статья с присвоенным id и created_at
        
    TODO: Реализовать функцию:
    1. Определить новый id (максимальный id в articles_db + 1, или 1 если список пуст)
    2. Создать объект Article с новым id, created_at=datetime.now() и данными из article_data
    3. Добавить статью в articles_db
    4. Вернуть созданную статью
    """
    pass


def update_article(article_id: int, article_data: ArticleUpdate) -> Optional[Article]:
    """
    Обновить статью
    
    Args:
        article_id: ID статьи для обновления
        article_data: Новые данные статьи
        
    Returns:
        Обновленная статья или None, если статья не найдена
        
    TODO: Реализовать функцию:
    1. Найти статью с указанным id в articles_db
    2. Если статья не найдена, вернуть None
    3. Обновить поля статьи данными из article_data (только те поля, которые не None)
       Используй: article.field = article_data.field if article_data.field is not None else article.field
    4. Вернуть обновленную статью
    """
    pass


def delete_article(article_id: int) -> bool:
    """
    Удалить статью
    
    Args:
        article_id: ID статьи для удаления
        
    Returns:
        True, если статья удалена, False если не найдена
        
    TODO: Реализовать функцию:
    1. Найти статью с указанным id в articles_db
    2. Если статья не найдена, вернуть False
    3. Удалить статью из articles_db
    4. Вернуть True
    """
    pass

