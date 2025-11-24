@echo off
REM Скрипт для запуска тестов и генерации отчета (Windows)

echo Запуск тестов...

REM Запускаем тесты с генерацией JSON отчета
pytest tests\ ^
    --json-report ^
    --json-report-file=test_results.json ^
    --tb=short ^
    -v

REM Проверяем код возврата
if %ERRORLEVEL% EQU 0 (
    echo.
    echo Тесты завершены успешно
) else (
    echo.
    echo Некоторые тесты провалились
)

REM Генерируем отчет
echo.
echo Генерация отчета...
python tests\generate_report.py

echo.
echo Готово! Проверьте файл TEST_REPORT.md
