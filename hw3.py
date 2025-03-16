import sys
import os
from collections import defaultdict

# Парсинг рядка логу
def parse_log_line(line: str) -> dict:
    parts = line.split(' ', 3)  # Розбиваємо рядок на компоненти: дата, час, рівень, повідомлення
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': parts[3].strip()
    } if len(parts) == 4 else None

# Завантаження логів з файлу
def load_logs(file_path: str) -> list:
    if not os.path.exists(file_path):
        print(f"Файл {file_path} не знайдено.")
        sys.exit(1)
    with open(file_path, 'r', encoding="utf-8") as file:
        return [log for line in file if (log := parse_log_line(line))]

# Фільтрація логів за рівнем
def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level'].upper() == level.upper()]

# Підрахунок записів за рівнем
def count_logs_by_level(logs: list) -> dict:
    counts = defaultdict(int)
    for log in logs:
        counts[log['level'].upper()] += 1
    return counts

# Виведення статистики по логах
def display_log_counts(counts: dict):
    print(f"\n{'Рівень логування':<15} | {'Кількість'}")
    print('-' * 30)
    for level, count in sorted(counts.items()):
        print(f"{level:<15} | {count}")
    print('-' * 30)

# Основна функція
def main():
    if len(sys.argv) < 2:
        print(f"Використання: python {sys.argv[0]} <шлях до файлу> [рівень]")
        sys.exit(1)

    log_file = sys.argv[1]  # Шлях до файлу логів
    logs = load_logs(log_file)

    # Якщо є другий аргумент, фільтруємо за рівнем
    if len(sys.argv) > 2:
        level = sys.argv[2].upper()
        filtered_logs = filter_logs_by_level(logs, level)
        print(f"\nДеталі логів для рівня '{level}':")
        if filtered_logs:
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
        else:
            print("Немає записів для цього рівня.")
    else:
        # Якщо другого аргументу немає, просто виводимо статистику
        display_log_counts(count_logs_by_level(logs))

if __name__ == "__main__":
    main()
