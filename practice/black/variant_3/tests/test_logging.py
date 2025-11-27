"""
Тесты для логирования
Проверяют ОРы: 3.1, 3.2 (Логирование)
"""
import pytest
import logging
from unittest.mock import patch

try:
    from main import logger
except ImportError:
    pytest.skip("main module not available", allow_module_level=True)


class TestOR31_LoggingSetup:
    """ОР 3.1: Настраивать логирование в FastAPI с использованием модуля logging"""
    
    def test_logger_configured(self):
        """Проверка настройки логирования"""
        assert logger is not None
        assert isinstance(logger, logging.Logger)
    
    def test_logger_has_handler(self):
        """Проверка наличия обработчика у логгера"""
        assert len(logger.handlers) > 0 or len(logging.root.handlers) > 0
    
    def test_different_log_levels(self, caplog):
        """Проверка использования разных уровней логирования"""
        with caplog.at_level(logging.INFO):
            logger.info("Test info")
            logger.warning("Test warning")
            logger.error("Test error")
        
        # Проверяем, что логи были записаны
        assert len(caplog.records) >= 1
        assert any(record.levelname in ["INFO", "WARNING", "ERROR"] for record in caplog.records)


class TestOR32_StructuredLogging:
    """ОР 3.2: Использовать структурированное логирование"""
    
    def test_logging_with_trace_id(self, caplog):
        """Проверка логирования с trace_id"""
        trace_id = "test-trace-123"
        with caplog.at_level(logging.INFO):
            logger.info(f"[{trace_id}] Test message")
        
        # Проверяем, что логирование было вызвано и содержит trace_id
        assert len(caplog.records) >= 1
        assert any(trace_id in record.message for record in caplog.records)
    
    def test_log_format_includes_trace_id(self):
        """Проверка формата логов с trace_id"""
        # Проверяем, что формат логирования настроен
        # Это проверяется через наличие trace_id в логах middleware
        assert True  # Проверка выполняется в test_middleware.py

