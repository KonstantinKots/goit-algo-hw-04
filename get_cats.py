from pathlib import Path

def get_cats_info(path):
    """
    Зчитує інформацію про котів із текстового файлу.

    Формат кожного рядка файлу: id,name,age

    Параметри: path (str): шлях до файлу.
    Повертає: list[dict]: список словників у форматі:{"id": str, "name": str, "age": str}
    При помилці читання — повертається порожній список.
    """
    path_file = Path(path)
    cats_info = []
    if not path_file.is_file():
        print(f"Файл {path} не знайдено")
        return []
    try:
        with open(path_file, "r", encoding = "utf-8") as file:
            for line in file:
                line = line.strip().split(",")
                if len(line) == 3:
                    cats_info.append({"id":line[0], "name":line[1], "age":line[2]})
    except Exception as e:
        print(f"Сталась помилка {e}")
        return []
    return cats_info

def main():
    """
    Точка входу в програму.
    Викликає функцію зчитування файлу та повертає результат
    """
    cats_info = get_cats_info("cats_file.txt")
    print(cats_info)
    
if __name__ == "__main__":
    main()
