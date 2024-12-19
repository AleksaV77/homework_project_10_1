import re
from collections import Counter

from src.utils import list_financial_transactions

categories_operations = [
    "Перевод организации",
    "Перевод с карты на карту",
    "Перевод с карты на счет",
    "Перевод со счета на счет",
    "Открытие вклада",
]


def list_financial_transactions_line(file: list[dict], line: str) -> list[dict]:
    """Функция возвращает список словарей у которых есть определенное слово в описании"""

    new_file = []
    for i in file:
        if re.findall(line.lower(), str(i.get("description")).lower()):
            new_file.append(i)
    return new_file


def categories_transactions(file: list[dict], category: list) -> dict:
    """Функция возвращает словарь, в котором ключ - это название категории,
    а значение - количество операций в каждой категории"""

    categories = [i["description"] for i in file if "description" in i and i["description"] in category]

    return Counter(categories)


if __name__ == "__main__":
    files = "C:/Users/asurk/PycharmProjects/Homework_Project1/data/operations.json"
    func = list_financial_transactions(files)
    search_string = "Открытие"

    print(list_financial_transactions_line(func, "с карты"))
    print(categories_transactions(func, categories_operations))
