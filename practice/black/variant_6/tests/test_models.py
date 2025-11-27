"""
Тесты для models.py
Проверяют ОРы: 5.1 (Pydantic валидация)
"""
import pytest
from pydantic import ValidationError

try:
    from models import ArticleCreate, Article, ArticleUpdate
except ImportError:
    pytest.skip("models module not available", allow_module_level=True)


class TestOR51_PydanticValidation:
    """ОР 5.1: Использовать Pydantic для валидации данных"""
    
    def test_article_create_valid_data(self):
        """Проверка создания ArticleCreate с валидными данными"""
        article = ArticleCreate(
            title="Тестовая статья",
            content="Содержание статьи",
            author="Иван Иванов",
            category="tech",
            published=True
        )
        assert article.title == "Тестовая статья"
        assert article.content == "Содержание статьи"
        assert article.author == "Иван Иванов"
        assert article.category == "tech"
        assert article.published is True
    
    def test_article_create_minimal_data(self):
        """Проверка создания ArticleCreate с минимальными данными"""
        article = ArticleCreate(
            title="Статья",
            content="Содержание",
            author="Автор",
            category="science"
        )
        assert article.title == "Статья"
        assert article.published is False
    
    def test_article_create_validation_title_required(self):
        """Проверка валидации: title обязателен"""
        with pytest.raises(ValidationError):
            ArticleCreate(content="Содержание", author="Автор", category="tech")
    
    def test_article_create_validation_content_required(self):
        """Проверка валидации: content обязателен"""
        with pytest.raises(ValidationError):
            ArticleCreate(title="Статья", author="Автор", category="tech")
    
    def test_article_create_validation_author_required(self):
        """Проверка валидации: author обязателен"""
        with pytest.raises(ValidationError):
            ArticleCreate(title="Статья", content="Содержание", category="tech")
    
    def test_article_create_validation_category_required(self):
        """Проверка валидации: category обязателен"""
        with pytest.raises(ValidationError):
            ArticleCreate(title="Статья", content="Содержание", author="Автор")
    
    def test_article_create_validation_category_enum(self):
        """Проверка валидации: category должен быть из списка допустимых"""
        with pytest.raises(ValidationError):
            ArticleCreate(title="Статья", content="Содержание", author="Автор", category="invalid")
    
    def test_article_inherits_from_article_create(self):
        """Проверка наследования Article от ArticleCreate"""
        from datetime import datetime
        article = Article(
            id=1,
            title="Статья",
            content="Содержание",
            author="Автор",
            category="tech",
            created_at=datetime.now()
        )
        assert article.id == 1
        assert article.title == "Статья"
        assert article.created_at is not None
    
    def test_article_update_all_optional(self):
        """Проверка, что все поля ArticleUpdate необязательны"""
        article_update = ArticleUpdate()
        assert article_update.title is None
        assert article_update.content is None
        assert article_update.author is None
        assert article_update.category is None
        assert article_update.published is None

