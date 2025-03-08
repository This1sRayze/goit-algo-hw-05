import sys
import os
from collections import defaultdict

def parse_log_line(line: str) -> dict:
    parts = line.splt(' ', 3)
    return {'date':parts[0], 'time':parts[1], 'level':parts[2], 'message':parts[3].strip()} if len(parts) == 4 else None

def load_logs(file_path: str) -> list:
    if not os.path.exists(file_path):
        print(f"Файл {file_path} не знайдено"); sys.exit(1)
    with open(file_path, 'r', encoding="utf-8") as file:
        return [log for line in file if (log := parse_log_line(line))]
    
def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level'].upper() == level.upper]

def count_logs_by_level(logs: list) -> dict:
    counts = defaultdict(int)
    for log in logs: counts[log['level']] +=1
    return counts

def display_log_counts(counts: dict):
    print("\nСтатистика логів:\n" + "-" * 30)
    for level, count in sorted(counts.items()): print(f"{level}: {count}")
    print("-" * 30)

def main():
    if len(sys.argv) < 2:
        print("Використання: python script.py <файл> [рівень]"); sys.exit(1)
    logs = load_logs(sys.argv[1])
    if len(sys.argv) > 2:
        filtered_logs = filter_logs_by_level(logs, sys.argv[2])
        print(f"\nЗаписи {sys.argv[2]}:")
        print("\n".join(f"{log['date']} {log['time']} {log['level']} {log['message']}" for log in filtered_logs) or "Немає записів.")
    else:
        display_log_counts(count_logs_by_level(logs))

if __name__ == "__main__":
    main()

