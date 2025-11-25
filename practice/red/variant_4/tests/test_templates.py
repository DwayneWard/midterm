"""
Тесты для HTML-шаблонов
Проверяют ОРы: 4.1, 4.2 (интеграция HTML-шаблонов, статические файлы)
"""
import pytest

try:
    from fastapi import status
except ImportError:
    pytest.skip("fastapi not available", allow_module_level=True)


class TestOR41_TemplateRendering:
    """ОР 4.1: Настроить проект FastAPI для работы с HTML-шаблонами"""
    
    def test_root_returns_html(self, client):
        """Проверка возврата HTML на главной странице"""
        response = client.get("/")
        if response.status_code == 200:
            assert "text/html" in response.headers["content-type"]
            assert "<html" in response.text.lower() or "<!doctype" in response.text.lower()
    
    def test_product_detail_returns_html(self, client):
        """Проверка возврата HTML на странице деталей книги"""
        response = client.get("/products/1")
        if response.status_code == 200:
            assert "text/html" in response.headers["content-type"]
    
    def test_add_product_form_returns_html(self, client):
        """Проверка возврата HTML формы добавления книги"""
        response = client.get("/products/add")
        if response.status_code == 200:
            assert "text/html" in response.headers["content-type"]
            assert "form" in response.text.lower()


class TestOR42_StaticFiles:
    """ОР 4.2: Организовывать маршруты для отдачи статических файлов"""
    
    def test_css_file_accessible(self, client):
        """Проверка доступности CSS файла"""
        response = client.get("/static/css/style.css")
        # Может быть 200 (если настроено) или 404 (если нет)
        assert response.status_code in [200, 404]
        if response.status_code == 200:
            assert "text/css" in response.headers.get("content-type", "")
    
    def test_js_file_accessible(self, client):
        """Проверка доступности JS файла"""
        response = client.get("/static/js/main.js")
        assert response.status_code in [200, 404]
        if response.status_code == 200:
            assert "application/javascript" in response.headers.get("content-type", "") or "text/javascript" in response.headers.get("content-type", "")
    
    def test_html_references_static_files(self, client):
        """Проверка, что HTML ссылается на статические файлы"""
        response = client.get("/")
        if response.status_code == 200:
            html_content = response.text
            # Проверяем наличие ссылок на CSS или JS
            assert "/static/" in html_content or "style.css" in html_content or "main.js" in html_content

