@echo off
REM Скрипт для запуска тестов и генерации отчета

echo Запуск тестов...

REM Запуск pytest с генерацией JSON отчета
pytest tests/ --json-report --json-report-file=test_results.json -v

REM Генерация отчета
echo.
echo Генерация отчета...
python tests/generate_report.py

echo.
echo Готово! Отчет сохранен в TEST_REPORT.md

pause

