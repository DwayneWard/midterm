#!/bin/bash
# Скрипт для запуска тестов и генерации отчета

echo "Запуск тестов..."

# Запускаем тесты с генерацией JSON отчета
pytest tests/ \
    --json-report \
    --json-report-file=test_results.json \
    --tb=short \
    -v

# Проверяем код возврата
if [ $? -eq 0 ]; then
    echo ""
    echo "Тесты завершены успешно"
else
    echo ""
    echo "Некоторые тесты провалились"
fi

# Генерируем отчет
echo ""
echo "Генерация отчета..."
python tests/generate_report.py

echo ""
echo "Готово! Проверьте файл TEST_REPORT.md"
