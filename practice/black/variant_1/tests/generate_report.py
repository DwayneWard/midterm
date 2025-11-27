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
    "1.1": 10,  # Создавать и подключать middleware в FastAPI
    "1.2": 10,  # Реализовывать middleware для трассировки запросов с использованием UUID
    "1.3": 5,   # Использовать middleware для логирования запросов и ответов
    "2.1": 5,   # Настраивать Redis для использования в FastAPI
    "2.2": 10,  # Реализовывать базовое кеширование данных в FastAPI
    "2.3": 5,   # Настраивать TTL для кешированных данных
    "2.4": 10,  # Реализовывать стратегии инвалидации кеша
    "3.1": 5,   # Настраивать логирование в FastAPI с использованием модуля logging
    "3.2": 5,   # Использовать структурированное логирование
    "4.1": 5,   # Использовать BackgroundTasks в FastAPI
    "4.2": 10,  # Настраивать и запускать периодические задачи с помощью APScheduler
    "5.1": 10,  # Использовать Depends для внедрения зависимостей в эндпоинты
    "5.2": 10,  # Создавать собственные зависимости для подключения к базам данных, кеширования
}


def map_tests_to_ors(test_results: dict) -> dict:
    """Маппинг результатов тестов на образовательные результаты"""
    or_results = {
        "1.1": {"name": "Создавать и подключать middleware в FastAPI", "tests": [], "passed": 0, "failed": 0, "points": 0, "max_points": 0},
        "1.2": {"name": "Реализовывать middleware для трассировки запросов с использованием UUID", "tests": [], "passed": 0, "failed": 0, "points": 0, "max_points": 0},
        "1.3": {"name": "Использовать middleware для логирования запросов и ответов", "tests": [], "passed": 0, "failed": 0, "points": 0, "max_points": 0},
        "2.1": {"name": "Настраивать Redis для использования в FastAPI", "tests": [], "passed": 0, "failed": 0, "points": 0, "max_points": 0},
        "2.2": {"name": "Реализовывать базовое кеширование данных в FastAPI", "tests": [], "passed": 0, "failed": 0, "points": 0, "max_points": 0},
        "2.3": {"name": "Настраивать TTL для кешированных данных", "tests": [], "passed": 0, "failed": 0, "points": 0, "max_points": 0},
        "2.4": {"name": "Реализовывать стратегии инвалидации кеша", "tests": [], "passed": 0, "failed": 0, "points": 0, "max_points": 0},
        "3.1": {"name": "Настраивать логирование в FastAPI с использованием модуля logging", "tests": [], "passed": 0, "failed": 0, "points": 0, "max_points": 0},
        "3.2": {"name": "Использовать структурированное логирование", "tests": [], "passed": 0, "failed": 0, "points": 0, "max_points": 0},
        "4.1": {"name": "Использовать BackgroundTasks в FastAPI", "tests": [], "passed": 0, "failed": 0, "points": 0, "max_points": 0},
        "4.2": {"name": "Настраивать и запускать периодические задачи с помощью APScheduler", "tests": [], "passed": 0, "failed": 0, "points": 0, "max_points": 0},
        "5.1": {"name": "Использовать Depends для внедрения зависимостей в эндпоинты", "tests": [], "passed": 0, "failed": 0, "points": 0, "max_points": 0},
        "5.2": {"name": "Создавать собственные зависимости для подключения к базам данных, кеширования", "tests": [], "passed": 0, "failed": 0, "points": 0, "max_points": 0},
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
        elif "OR13" in test_name or "TestOR13" in test_name:
            or_key = "1.3"
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
    
    # Подсчет баллов для каждого ОРа
    for or_key, or_data in or_results.items():
        total_tests = or_data["passed"] + or_data["failed"]
        if total_tests > 0:
            or_data["max_points"] = OR_POINTS.get(or_key, 0)
            # Если все тесты прошли, начисляем полные баллы
            if or_data["failed"] == 0:
                or_data["points"] = or_data["max_points"]
            else:
                # Пропорциональное начисление баллов
                or_data["points"] = round((or_data["passed"] / total_tests) * or_data["max_points"], 1)
    
    return or_results


def generate_markdown_report(or_results: dict, test_results: dict) -> str:
    """Генерация Markdown отчета"""
    report_lines = [
        "# Отчет о результатах тестирования",
        f"**Дата:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Общая информация",
        ""
    ]
    
    # Общая статистика
    total_tests = test_results.get("summary", {}).get("total", 0)
    passed_tests = test_results.get("summary", {}).get("passed", 0)
    failed_tests = test_results.get("summary", {}).get("failed", 0)
    
    report_lines.extend([
        f"- **Всего тестов:** {total_tests}",
        f"- **Пройдено:** {passed_tests}",
        f"- **Провалено:** {failed_tests}",
        ""
    ])
    
    # Подсчет общего балла
    total_points = sum(or_data["points"] for or_data in or_results.values())
    max_total_points = sum(or_data["max_points"] for or_data in or_results.values() if or_data["max_points"] > 0)
    
    # Пересчитываем только для ОРов с тестами
    tested_ors = {k: v for k, v in or_results.items() if v["max_points"] > 0}
    if tested_ors:
        max_total_points = sum(v["max_points"] for v in tested_ors.values())
        total_points = sum(v["points"] for v in tested_ors.values())
    
    report_lines.extend([
        f"- **Набрано баллов:** {total_points:.1f} / {max_total_points:.1f}",
        ""
    ])
    
    # Определение оценки
    percentage = (total_points / max_total_points * 100) if max_total_points > 0 else 0
    if percentage >= 90:
        grade = "Отлично"
    elif percentage >= 75:
        grade = "Хорошо"
    elif percentage >= 60:
        grade = "Удовлетворительно"
    else:
        grade = "Неудовлетворительно"
    
    report_lines.extend([
        f"- **Оценка:** {grade}",
        "",
        "## Результаты по образовательным результатам",
        ""
    ])
    
    # Группировка по группам ОРов
    or_groups = {
        "1": "Middleware",
        "2": "Кеширование и Redis",
        "3": "Логирование",
        "4": "Периодические задачи",
        "5": "Dependency Injection",
    }
    
    for group_num, group_name in or_groups.items():
        report_lines.extend([
            f"### Группа {group_num}: {group_name}",
            ""
        ])
        
        group_ors = {k: v for k, v in or_results.items() if k.startswith(group_num + ".")}
        group_total = sum(v["points"] for v in group_ors.values())
        group_max = sum(v["max_points"] for v in group_ors.values() if v["max_points"] > 0)
        
        for or_key in sorted(group_ors.keys()):
            or_data = group_ors[or_key]
            if or_data["max_points"] == 0:
                continue  # Пропускаем ОРы без тестов
            
            status_icon = "✅" if or_data["failed"] == 0 else "❌"
            report_lines.extend([
                f"#### {status_icon} ОР {or_key}: {or_data['name']}",
                f"- **Баллы:** {or_data['points']:.1f} / {or_data['max_points']:.1f}",
                f"- **Тесты:** {or_data['passed']} пройдено, {or_data['failed']} провалено",
                ""
            ])
            
            if or_data["tests"]:
                report_lines.append("**Детали тестов:**")
                for test in or_data["tests"]:
                    test_status = "✅" if test["status"] == "passed" else "❌"
                    report_lines.append(f"- {test_status} {test['name']}")
                report_lines.append("")
        
        if group_max > 0:
            report_lines.extend([
                f"**Итого по группе:** {group_total:.1f} / {group_max:.1f} баллов",
                ""
            ])
    
    report_lines.extend([
        "## Итоговая оценка",
        "",
        f"**Набрано баллов:** {total_points:.1f} / {max_total_points:.1f}",
        f"**Процент выполнения:** {percentage:.1f}%",
        f"**Оценка:** {grade}",
        ""
    ])
    
    return "\n".join(report_lines)


def main():
    """Главная функция"""
    json_file = Path("test_results.json")
    if not json_file.exists():
        print(f"Ошибка: файл {json_file} не найден")
        print("Убедитесь, что вы запустили тесты с флагом --json-report")
        sys.exit(1)
    
    test_results = parse_pytest_json(json_file)
    or_results = map_tests_to_ors(test_results)
    
    report = generate_markdown_report(or_results, test_results)
    
    output_file = Path("TEST_REPORT.md")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"Отчет сохранен в файл: {output_file}")
    
    # Вывод итогового балла в консоль
    total_points = sum(or_data["points"] for or_data in or_results.values())
    max_total_points = sum(or_data["max_points"] for or_data in or_results.values() if or_data["max_points"] > 0)
    tested_ors = {k: v for k, v in or_results.items() if v["max_points"] > 0}
    if tested_ors:
        max_total_points = sum(v["max_points"] for v in tested_ors.values())
        total_points = sum(v["points"] for v in tested_ors.values())
    
    percentage = (total_points / max_total_points * 100) if max_total_points > 0 else 0
    print(f"\nИтого набрано баллов: {total_points:.1f} / {max_total_points:.1f} ({percentage:.1f}%)")


if __name__ == "__main__":
    main()

