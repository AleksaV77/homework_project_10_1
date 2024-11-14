import json
from json import JSONDecodeError


def list_financial_transactions(file):
    """возвращает список словарей с данными о финансовых транзакциях"""

    with open(file, "r", encoding="utf-8") as f:
        try:
            operations = json.load(f)
            return operations
        except JSONDecodeError:
            return []


file_operation = list_financial_transactions("C:/Users/asurk/PycharmProjects/Homework_Project1/data/operations_3.json")
print(file_operation)
