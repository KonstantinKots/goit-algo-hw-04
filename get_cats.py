from pathlib import Path


def get_cats_info(path):
    path_file = Path(path)
    cats_info = []
    if not path_file.is_file():
        print(f"Файл {path} не знайдено")
        return []

    try:
        with open(path, "r", encoding = "utf-8") as file:
            for line in file:
                line = line.strip().split(",")
                if len(line) == 3:
                    cats_info.append({"id":line[0], "name":line[1], "age":line[2]})
            return cats_info
    except Exception as e:
        print(f"Сталась помилка {e}")
        return []

def main():
    cats_info = get_cats_info("cats_file.txt")
    print(cats_info)
    
if __name__ == "__main__":
    main()
