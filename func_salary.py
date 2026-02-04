from pathlib import Path

#функція для розрахунку загальної та середньої зп
def total_salary(path: str | Path):
    '''Функція розраховує загальну сумму заробітної плати
    та середню із списка у форматі (ФІО, ЗП)
    :param date: шлях до файлу з (ФІО, ЗП)
    :type date: str | Path
    :return: загальну (total) та середню (average) ЗП
    :rtype: tuple[float, float]
    '''
    path = Path(path)
    salaries: list[float] = []
    #перевіряємо наявність файлу
    if not path.exists():
        print (f"Файл {path} не знайдено")
        return 0, 0
    else:
        #відкриваємо файл для читання з врахуванням кодування
        with open (path, 'r', encoding = "utf-8") as file:
            for line in file:
                #перевіряємо строки на наявність коми
                if "," in line:
                    #розбиваємо строку по роздільнику ","
                    salary_line = line.split(",")
                    #знаходимо необхідний елемент за індексом, очищаємо від зайвих символів,
                    #перетворюємо у float, додаємо до списку salaries
                    salaries.append(float(salary_line[1].strip()))
    #розраховуємо загальну ЗП
    total = sum(salaries)
    #розраховуємо середню ЗП
    average = total/len(salaries) if salaries else 0
    return total, average

def main() -> None:
    total, average = total_salary("salary_file.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

if __name__ == "__main__":
    main()
