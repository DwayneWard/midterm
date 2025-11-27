"""
Тесты для storage.py
Проверяют ОРы: 3.2 (работа с данными в памяти)
"""
import pytest
from datetime import datetime

try:
    from storage import (
        get_all_articles,
        get_article_by_id,
        create_article,
        update_article,
        delete_article
    )
    from models import Article, ArticleCreate
except ImportError:
    pytest.skip("storage module not available", allow_module_level=True)


class TestOR32_DataStorage:
    """ОР 3.2: Работать с данными в памяти"""
    
    def test_get_all_articles_returns_list(self):
        """Проверка получения всех статей"""
        articles = get_all_articles()
        assert isinstance(articles, list)
        assert len(articles) > 0
    
    def test_get_article_by_id_exists(self):
        """Проверка получения статьи по существующему ID"""
        # Создаем статью для гарантии, что она существует
        new_article = ArticleCreate(
            title="Тестовая статья для проверки",
            content="Содержание",
            author="Автор",
            category="tech"
        )
        created = create_article(new_article)
        article_id = created.id
        
        # Проверяем получение статьи
        article = get_article_by_id(article_id)
        assert article is not None
        assert article.id == article_id
    
    def test_get_article_by_id_not_exists(self):
        """Проверка получения статьи по несуществующему ID"""
        article = get_article_by_id(99999)
        assert article is None
    
    def test_create_article_adds_to_storage(self):
        """Проверка создания новой статьи"""
        initial_count = len(get_all_articles())
        new_article = ArticleCreate(
            title="Новая тестовая статья",
            content="Содержание новой статьи",
            author="Новый автор",
            category="science"
        )
        created = create_article(new_article)
        assert created.id is not None
        assert created.created_at is not None
        assert len(get_all_articles()) == initial_count + 1
    
    def test_update_article_exists(self):
        """Проверка обновления существующей статьи"""
        # Создаем статью для обновления
        new_article = ArticleCreate(
            title="Статья для обновления",
            content="Содержание",
            author="Автор",
            category="business"
        )
        created = create_article(new_article)
        
        # Обновляем статью
        from models import ArticleUpdate
        updated_data = ArticleUpdate(title="Обновленное название")
        updated = update_article(created.id, updated_data)
        assert updated is not None
        assert updated.title == "Обновленное название"
    
    def test_delete_article_exists(self):
        """Проверка удаления существующей статьи"""
        # Создаем статью для удаления
        new_article = ArticleCreate(
            title="Статья для удаления",
            content="Содержание",
            author="Автор",
            category="tech"
        )
        created = create_article(new_article)
        article_id = created.id
        
        # Удаляем статью
        result = delete_article(article_id)
        assert result is True
        assert get_article_by_id(article_id) is None

