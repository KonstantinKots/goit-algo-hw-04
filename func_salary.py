from pathlib import Path

#функція для розрахунку загальної та середньої зп
def total_salary(path: Path):
    path = Path(path)
    if not path.exists():
            return (f"Файл {path} не знайдено")
    else:
        salaryes = []
        with open (path, 'r', encoding = "utf-8") as file:
            for line in file:
                salary_line = line.split(",")
                salaryes.append(float(salary_line[1].strip()))
        total = sum(salaryes)
        average = total/len(salaryes)
        return total, average

if __name__ == "__main__":
    total, average = total_salary("salary_file.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
