"""
Скрипт для генерации отчета по результатам тестов.
"""
import json
import sys
from pathlib import Path
from datetime import datetime
import re


def parse_pytest_json(json_file: Path) -> dict:
    """Парсинг JSON отчета pytest"""
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"Ошибка: файл {json_file} не найден")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Ошибка: файл {json_file} содержит невалидный JSON")
        sys.exit(1)


# Распределение баллов по ОРам (максимальные баллы)
OR_POINTS = {
    "1": 20,  # Протокол HTTP и REST API
    "2": 25,  # Работа с библиотекой requests и JSON
    "3": 15,  # Модульный код и разделение логики
    "4": 25,  # Основы Telegram Bot API
    "5": 15,  # Инлайн-кнопки и продвинутые обработчики
}

def map_tests_to_ors(test_results: dict) -> dict:
    """Маппинг результатов тестов на образовательные результаты"""
    or_results = {
        "1.1": {"name": "Сформировать HTTP-запрос", "tests": [], "passed": 0, "failed": 0, "points": 0, "max_points": 0},
        "1.2": {"name": "Анализировать статус-коды", "tests": [], "passed": 0, "failed": 0, "points": 0, "max_points": 0},
        "2.1": {"name": "Использовать requests", "tests": [], "passed": 0, "failed": 0, "points": 0, "max_points": 0},
        "2.2": {"name": "Обработка ошибок запросов", "tests": [], "passed": 0, "failed": 0, "points": 0, "max_points": 0},
        "2.3": {"name": "Преобразование JSON", "tests": [], "passed": 0, "failed": 0, "points": 0, "max_points": 0},
        "2.4": {"name": "Обработка ошибок запросов (полная)", "tests": [], "passed": 0, "failed": 0, "points": 0, "max_points": 0},
        "3.1": {"name": "Разделение на модули", "tests": [], "passed": 0, "failed": 0, "points": 0, "max_points": 0},
        "3.2": {"name": "Правильные импорты", "tests": [], "passed": 0, "failed": 0, "points": 0, "max_points": 0},
        "3.3": {"name": "Структурирование проекта", "tests": [], "passed": 0, "failed": 0, "points": 0, "max_points": 0},
        "4.1": {"name": "Настройка и запуск бота", "tests": [], "passed": 0, "failed": 0, "points": 0, "max_points": 0},
        "4.2": {"name": "Обработка команд и сообщений", "tests": [], "passed": 0, "failed": 0, "points": 0, "max_points": 0},
        "5.1": {"name": "Inline-кнопки и клавиатуры", "tests": [], "passed": 0, "failed": 0, "points": 0, "max_points": 0},
        "5.2": {"name": "Обработка callback-запросов", "tests": [], "passed": 0, "failed": 0, "points": 0, "max_points": 0},
    }
    
    # Маппинг тестов на ОРы по названиям классов
    # pytest-json-report может иметь разную структуру
    tests_list = test_results.get("tests", [])
    if not tests_list and "report" in test_results:
        tests_list = test_results["report"].get("tests", [])
    
    for test in tests_list:
        test_name = test.get("nodeid", "") or test.get("name", "")
        
        # Определяем ОР по названию теста
        if "OR11" in test_name or "TestOR11" in test_name:
            or_key = "1.1"
        elif "OR12" in test_name or "TestOR12" in test_name:
            or_key = "1.2"
        elif "OR21" in test_name or "TestOR21" in test_name:
            or_key = "2.1"
        elif "OR22" in test_name or "TestOR22" in test_name:
            or_key = "2.2"
        elif "OR23" in test_name or "TestOR23" in test_name:
            or_key = "2.3"
        elif "OR24" in test_name or "TestOR24" in test_name:
            or_key = "2.4"
        elif "OR31" in test_name or "TestOR31" in test_name:
            or_key = "3.1"
        elif "OR32" in test_name or "TestOR32" in test_name:
            or_key = "3.2"
        elif "OR33" in test_name or "TestOR33" in test_name:
            or_key = "3.3"
        elif "OR41" in test_name or "TestOR41" in test_name:
            or_key = "4.1"
        elif "OR42" in test_name or "TestOR42" in test_name:
            or_key = "4.2"
        elif "OR51" in test_name or "TestOR51" in test_name:
            or_key = "5.1"
        elif "OR52" in test_name or "TestOR52" in test_name:
            or_key = "5.2"
        else:
            continue  # Пропускаем тесты без явного ОРа
        
        or_results[or_key]["tests"].append({
            "name": test_name.split("::")[-1],
            "status": test.get("outcome", "unknown"),
            "duration": test.get("duration", 0)
        })
        
        if test.get("outcome") == "passed":
            or_results[or_key]["passed"] += 1
        elif test.get("outcome") == "failed":
            or_results[or_key]["failed"] += 1
    
    # Рассчитываем баллы для каждого ОРа
    # Баллы распределяются пропорционально проценту пройденных тестов
    # Сначала определяем, сколько под-ОРов в каждой группе имеют тесты
    or_groups_with_tests = {}
    for or_key, or_data in or_results.items():
        or_group = or_key.split(".")[0]
        total_tests = or_data["passed"] + or_data["failed"]
        if total_tests > 0:
            if or_group not in or_groups_with_tests:
                or_groups_with_tests[or_group] = []
            or_groups_with_tests[or_group].append(or_key)
    
    # Теперь рассчитываем баллы
    for or_key, or_data in or_results.items():
        total_tests = or_data["passed"] + or_data["failed"]
        or_group = or_key.split(".")[0]
        max_group_points = OR_POINTS.get(or_group, 0)
        
        if total_tests == 0:
            # Если тестов нет, баллы не начисляются
            or_data["max_points"] = 0
            or_data["points"] = 0
        else:
            # Считаем количество под-ОРов в группе, у которых есть тесты
            ors_with_tests_in_group = len(or_groups_with_tests.get(or_group, []))
            
            if ors_with_tests_in_group == 0:
                or_data["max_points"] = 0
                or_data["points"] = 0
            else:
                # Распределяем баллы группы равномерно между под-ОРами, у которых есть тесты
                points_per_or = max_group_points / ors_with_tests_in_group if ors_with_tests_in_group > 0 else 0
                
                # Баллы начисляются пропорционально проценту пройденных тестов
                pass_rate = or_data["passed"] / total_tests if total_tests > 0 else 0
                or_data["max_points"] = round(points_per_or, 1)
                or_data["points"] = round(points_per_or * pass_rate, 1)
    
    return or_results


def generate_markdown_report(or_results: dict, summary: dict) -> str:
    """Генерация Markdown отчета"""
    report = f"""# Отчет о выполнении практической части контрольной работы
## Вариант 1. Основной трек

**Дата выполнения:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Общая статистика

- **Всего тестов:** {summary.get('total', 0)}
- **Пройдено:** {summary.get('passed', 0)}
- **Провалено:** {summary.get('failed', 0)}
- **Пропущено:** {summary.get('skipped', 0)}
- **Время выполнения:** {summary.get('duration', 0):.2f} секунд

## Результаты по образовательным результатам (ОРы)

"""
    
    total_or_passed = 0
    total_or_failed = 0
    total_points = 0.0
    total_max_points = 0.0
    
    # Группируем ОРы по группам для отображения
    or_groups = {}
    for or_key in sorted(or_results.keys()):
        or_group = or_key.split(".")[0]
        if or_group not in or_groups:
            or_groups[or_group] = []
        or_groups[or_group].append(or_key)
    
    for or_group in sorted(or_groups.keys()):
        group_name = {
            "1": "Протокол HTTP и REST API",
            "2": "Работа с библиотекой requests и JSON",
            "3": "Модульный код и разделение логики",
            "4": "Основы Telegram Bot API",
            "5": "Инлайн-кнопки и продвинутые обработчики"
        }.get(or_group, f"ОР группа {or_group}")
        
        group_max_points = OR_POINTS.get(or_group, 0)
        group_points = 0.0
        
        report += f"""### {group_name} (максимум {group_max_points} баллов)

"""
        
        for or_key in sorted(or_groups[or_group]):
            or_data = or_results[or_key]
            total_tests = or_data["passed"] + or_data["failed"]
            
            if total_tests == 0:
                status = "⚠️ Не проверено"
            elif or_data["failed"] == 0:
                status = "✅ Выполнено"
                total_or_passed += 1
            else:
                status = "❌ Есть ошибки"
                total_or_failed += 1
            
            points = or_data["points"]
            max_points = or_data["max_points"]
            group_points += points
            total_points += points
            total_max_points += max_points
            
            report += f"""#### ОР {or_key}: {or_data['name']}
**Статус:** {status} | **Баллы:** {points:.1f} / {max_points:.1f}

- Тестов: {total_tests}
- Пройдено: {or_data['passed']}
- Провалено: {or_data['failed']}

"""
            
            if or_data["tests"]:
                report += "**Детали тестов:**\n\n"
                for test in or_data["tests"]:
                    test_status = "✅" if test["status"] == "passed" else "❌"
                    report += f"- {test_status} {test['name']} ({test.get('duration', 0):.3f}s)\n"
                report += "\n"
        
        report += f"**Итого по группе:** {group_points:.1f} / {group_max_points} баллов\n\n"
    
    # Определяем оценку
    # Максимальный балл всегда 100 (даже если не все ОРы проверяются тестами)
    MAX_TOTAL_POINTS = 100.0
    percentage = (total_points / MAX_TOTAL_POINTS * 100) if MAX_TOTAL_POINTS > 0 else 0
    if percentage >= 90:
        grade = "Отлично"
    elif percentage >= 75:
        grade = "Хорошо"
    elif percentage >= 60:
        grade = "Удовлетворительно"
    else:
        grade = "Неудовлетворительно"
    
    report += f"""## Итоговая оценка

### Баллы

- **Набрано баллов:** {total_points:.1f} / {MAX_TOTAL_POINTS:.1f}
- **Процент выполнения:** {percentage:.1f}%
- **Оценка:** **{grade}**

**Примечание:** Максимальный балл за работу составляет 100 баллов. Баллы начисляются только за те ОРы, которые проверяются тестами.

### Статистика по ОРам

- **ОРов выполнено полностью:** {total_or_passed}
- **ОРов с ошибками:** {total_or_failed}
- **ОРов не проверено:** {len(or_results) - total_or_passed - total_or_failed}

## Примечания

Этот отчет автоматически сгенерирован на основе результатов выполнения автотестов.
Каждый образовательный результат проверяется набором тестов, которые проверяют соответствие реализации требованиям.

**Важно:** Баллы рассчитываются пропорционально проценту пройденных тестов для каждого ОРа.
Максимальный балл за работу: 100 баллов.

"""
    
    return report


def main():
    """Главная функция генерации отчета"""
    # Путь к JSON файлу с результатами pytest
    json_file = Path("test_results.json")
    
    if not json_file.exists():
        print("Ошибка: файл test_results.json не найден.")
        print("Запустите тесты с флагом --json-report:")
        print("pytest --json-report --json-report-file=test_results.json")
        sys.exit(1)
    
    # Парсим результаты
    test_results = parse_pytest_json(json_file)
    
    # Маппим на ОРы
    or_results = map_tests_to_ors(test_results)
    
    # Формируем summary
    # pytest-json-report может иметь summary в разных местах
    summary_data = test_results.get("summary", {})
    if not summary_data and "report" in test_results:
        summary_data = test_results["report"].get("summary", {})
    
    summary = {
        "total": summary_data.get("total", 0),
        "passed": summary_data.get("passed", 0),
        "failed": summary_data.get("failed", 0),
        "skipped": summary_data.get("skipped", 0),
        "duration": test_results.get("duration", 0) or test_results.get("report", {}).get("duration", 0)
    }
    
    # Генерируем отчет
    report = generate_markdown_report(or_results, summary)
    
    # Сохраняем отчет
    report_file = Path("TEST_REPORT.md")
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report)
    
    # Рассчитываем итоговые баллы для вывода
    total_points = sum(or_data.get("points", 0) for or_data in or_results.values())
    MAX_TOTAL_POINTS = 100.0
    percentage = (total_points / MAX_TOTAL_POINTS * 100) if MAX_TOTAL_POINTS > 0 else 0
    
    if percentage >= 90:
        grade = "Отлично"
    elif percentage >= 75:
        grade = "Хорошо"
    elif percentage >= 60:
        grade = "Удовлетворительно"
    else:
        grade = "Неудовлетворительно"
    
    print(f"Отчет сохранен в файл: {report_file}")
    print(f"\nСтатистика:")
    print(f"  Всего тестов: {summary['total']}")
    print(f"  Пройдено: {summary['passed']}")
    print(f"  Провалено: {summary['failed']}")
    print(f"\nБаллы:")
    print(f"  Набрано: {total_points:.1f} / {MAX_TOTAL_POINTS:.1f} баллов")
    print(f"  Процент: {percentage:.1f}%")
    print(f"  Оценка: {grade}")


if __name__ == "__main__":
    main()

