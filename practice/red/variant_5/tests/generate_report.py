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
    "1": 10,  # Основы клиент-серверной архитектуры
    "2": 15,  # Знакомство с FastAPI
    "3": 25,  # Работа с данными и настройка API
    "4": 20,  # Интеграция HTML-шаблонов и статики
    "5": 15,  # Обработка форм и передача данных
    "6": 15,  # Обработка ошибок и обеспечение стабильности
}

def map_tests_to_ors(test_results: dict) -> dict:
    """Маппинг результатов тестов на образовательные результаты"""
    or_results = {
        "1.1": {"name": "Анализировать клиент-серверное взаимодействие", "tests": [], "passed": 0, "failed": 0, "points": 0, "max_points": 0},
        "1.2": {"name": "Определять роль API в архитектуре", "tests": [], "passed": 0, "failed": 0, "points": 0, "max_points": 0},
        "2.1": {"name": "Создавать базовые эндпоинты", "tests": [], "passed": 0, "failed": 0, "points": 0, "max_points": 0},
        "2.2": {"name": "Работать с path parameters", "tests": [], "passed": 0, "failed": 0, "points": 0, "max_points": 0},
        "3.1": {"name": "Использовать Pydantic для валидации", "tests": [], "passed": 0, "failed": 0, "points": 0, "max_points": 0},
        "3.2": {"name": "Работать с данными в памяти", "tests": [], "passed": 0, "failed": 0, "points": 0, "max_points": 0},
        "3.3": {"name": "Создавать эндпоинты для CRUD", "tests": [], "passed": 0, "failed": 0, "points": 0, "max_points": 0},
        "4.1": {"name": "Настроить работу с HTML-шаблонами", "tests": [], "passed": 0, "failed": 0, "points": 0, "max_points": 0},
        "4.2": {"name": "Организовывать маршруты для статики", "tests": [], "passed": 0, "failed": 0, "points": 0, "max_points": 0},
        "5.1": {"name": "Создавать эндпоинты для обработки форм", "tests": [], "passed": 0, "failed": 0, "points": 0, "max_points": 0},
        "5.2": {"name": "Реализовывать валидацию входных данных", "tests": [], "passed": 0, "failed": 0, "points": 0, "max_points": 0},
        "6.1": {"name": "Создавать кастомные обработчики ошибок", "tests": [], "passed": 0, "failed": 0, "points": 0, "max_points": 0},
        "6.2": {"name": "Настраивать статусы ответов", "tests": [], "passed": 0, "failed": 0, "points": 0, "max_points": 0},
    }
    
    # Маппинг тестов на ОРы по названиям классов
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
        elif "OR61" in test_name or "TestOR61" in test_name:
            or_key = "6.1"
        elif "OR62" in test_name or "TestOR62" in test_name:
            or_key = "6.2"
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
    # Сначала определяем, какие ОРы проверяются тестами
    or_groups_with_tests = {}
    for or_key, or_data in or_results.items():
        or_group = or_key.split(".")[0]
        total_tests = or_data["passed"] + or_data["failed"]
        if total_tests > 0:
            if or_group not in or_groups_with_tests:
                or_groups_with_tests[or_group] = []
            or_groups_with_tests[or_group].append(or_key)
    
    # Считаем общее количество баллов проверяемых групп
    total_checked_points = 0
    for or_group, or_keys in or_groups_with_tests.items():
        if len(or_keys) > 0:
            total_checked_points += OR_POINTS.get(or_group, 0)
    
    # Считаем общее количество баллов не проверяемых групп
    total_unchecked_points = 0
    for or_group in OR_POINTS.keys():
        if or_group not in or_groups_with_tests or len(or_groups_with_tests.get(or_group, [])) == 0:
            total_unchecked_points += OR_POINTS.get(or_group, 0)
    
    # Перераспределяем баллы не проверяемых групп между проверяемыми пропорционально
    redistribution_factor = 1.0
    if total_checked_points > 0:
        # Добавляем не проверяемые баллы к проверяемым
        redistribution_factor = (total_checked_points + total_unchecked_points) / total_checked_points if total_checked_points > 0 else 1.0
    
    # Рассчитываем баллы для каждого ОРа
    for or_key, or_data in or_results.items():
        total_tests = or_data["passed"] + or_data["failed"]
        or_group = or_key.split(".")[0]
        max_group_points = OR_POINTS.get(or_group, 0)
        
        if total_tests == 0:
            # ОР не проверяется тестами - не получает баллы
            or_data["max_points"] = 0
            or_data["points"] = 0
        else:
            # ОР проверяется тестами
            ors_with_tests_in_group = len(or_groups_with_tests.get(or_group, []))
            
            if ors_with_tests_in_group == 0:
                or_data["max_points"] = 0
                or_data["points"] = 0
            else:
                # Баллы группы распределяются только между проверяемыми ОРами
                # Если в группе есть не проверяемые ОРы, их баллы перераспределяются
                points_per_or = max_group_points / ors_with_tests_in_group if ors_with_tests_in_group > 0 else 0
                # Применяем перераспределение не проверяемых баллов
                points_per_or *= redistribution_factor
                pass_rate = or_data["passed"] / total_tests if total_tests > 0 else 0
                or_data["max_points"] = round(points_per_or, 1)
                or_data["points"] = round(points_per_or * pass_rate, 1)
    
    return or_results


def generate_markdown_report(or_results: dict, summary: dict) -> str:
    """Генерация Markdown отчета"""
    report = f"""# Отчет о выполнении практической части контрольной работы
## Вариант 5. Красный трек

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
    
    or_groups = {}
    for or_key in sorted(or_results.keys()):
        or_group = or_key.split(".")[0]
        if or_group not in or_groups:
            or_groups[or_group] = []
        or_groups[or_group].append(or_key)
    
    for or_group in sorted(or_groups.keys()):
        group_name = {
            "1": "Основы клиент-серверной архитектуры",
            "2": "Знакомство с FastAPI",
            "3": "Работа с данными и настройка API",
            "4": "Интеграция HTML-шаблонов и статики",
            "5": "Обработка форм и передача данных",
            "6": "Обработка ошибок и обеспечение стабильности"
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
    
    # Максимальный балл всегда 100 (из OR_POINTS)
    # Если какие-то ОРы не проверяются тестами, их баллы перераспределяются между проверяемыми ОРами в той же группе
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

**Примечание:** Максимальный балл за работу составляет 100 баллов (из OR_POINTS). Если какие-то ОРы не проверяются тестами, их баллы перераспределяются между проверяемыми ОРами в той же группе. Баллы рассчитываются пропорционально проценту пройденных тестов для каждого ОРа.

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
    json_file = Path("test_results.json")
    
    if not json_file.exists():
        print("Ошибка: файл test_results.json не найден.")
        print("Запустите тесты с флагом --json-report:")
        print("pytest --json-report --json-report-file=test_results.json")
        sys.exit(1)
    
    test_results = parse_pytest_json(json_file)
    or_results = map_tests_to_ors(test_results)
    
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
    
    report = generate_markdown_report(or_results, summary)
    
    report_file = Path("TEST_REPORT.md")
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report)
    
    total_points = sum(or_data.get("points", 0) for or_data in or_results.values())
    # Максимальный балл всегда 100 (из OR_POINTS)
    # Если какие-то ОРы не проверяются тестами, их баллы перераспределяются между проверяемыми ОРами в той же группе
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

