import os

from src.processing import filter_by_state, sort_by_date
from src.search_transactions import list_financial_transactions_line
from src.utils import list_financial_transactions
from src.utils_csv import list_financial_transactions_csv
from src.utils_excel import list_financial_transactions_excel
from src.widget import get_date, mask_account_card


def select_option():
    """Выбор файла с данными о финансовых транзакциях"""
    bank_transactions = []
    while True:
        print(
            """Привет! Добро пожаловать в программу работы с банковскими транзакциями.
        Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла\n"""
        )

        user_input = input().strip()
        if user_input == "1":
            print("\nДля обработки выбран JSON-файл.")
            bank_transactions = list_financial_transactions(os.path.join("data/operations_3.json"))
            break
        elif user_input == "2":
            print("\nДля обработки выбран CSV-файл.")
            bank_transactions = list_financial_transactions_csv(os.path.join("data/transactions.csv"))
            break
        elif user_input == "3":
            print("\nДля обработки выбран XLSX-файл.")
            bank_transactions = list_financial_transactions_excel(os.path.join("data/transactions_excel.xlsx"))
            break
        else:
            print("\nНекорректный пункт меню.\n")
            continue
    return bank_transactions, user_input


def status_sort_option(bank_transactions):
    """Сортировка по статусу"""
    while True:
        status = ", ".join(["CANCELED", "PENDING", "EXECUTED"])
        print(
            "\nВведите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: CANCELED, PENDING, EXECUTED: "
        )
        user_sort_state = input().upper()
        if user_sort_state not in status:
            print(f"\nСтатус операции {user_sort_state} недоступен.")
            continue
        print(f"\nОперации отфильтрованы по статусу {user_sort_state}")
        bank_transactions = filter_by_state(bank_transactions, user_sort_state)
        break
    return bank_transactions


def date_sort_option(bank_transactions):
    """Сортировка по дате (по убыванию или возрастанию)"""
    while True:
        print("\nОтсортировать операции по дате? Да/Нет: ")
        user_sort_order = input().lower()
        if user_sort_order != "да" and user_sort_order != "нет":
            print("\nВведен некорректный ответ.\n")
            continue
        elif user_sort_order == "да":
            while True:
                user_sort_order = input("\nОтсортировать по возрастанию или по убыванию?: ").lower()
                if user_sort_order == "по возрастанию":
                    bank_transactions = sort_by_date(bank_transactions, False)
                    break
                elif user_sort_order == "по убыванию":
                    bank_transactions = sort_by_date(bank_transactions, True)
                    break
                else:
                    print("\nНекорректное значение")
                    continue
            break
        elif user_sort_order == "нет":
            break
        break
    return bank_transactions


def trans_sort_option(bank_transactions, user_input):
    """Выбор сортировки рублевых тразакций или всех"""
    while True:
        print("\nВыводить только рублевые тразакции? Да/Нет:")
        user_sort_transaction = input().lower()
        if user_sort_transaction != "да" and user_sort_transaction != "нет":
            print("\nВведен некорректный ответ.\n")
            continue
        elif user_sort_transaction == "да":
            if user_input == "1":
                bank_transactions = [i for i in bank_transactions if i["operationAmount"]["currency"]["code"] == "RUB"]
                break
            else:
                bank_transactions = [i for i in bank_transactions if i["currency_code"] == "RUB"]
                break
        elif user_sort_transaction == "нет":
            break
    return bank_transactions


def sort_word_option(bank_transactions):
    """Выбор сортировки по определенному слову в описании или всех"""
    while True:
        print("\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет: ")
        user_sort_word = input().lower()
        if user_sort_word == "да":
            user_by_word = input("Введите слово для фильтрации: ")
            bank_transactions = list_financial_transactions_line(bank_transactions, user_by_word)
            break
        elif user_sort_word == "нет":
            for word in bank_transactions:
                bank_transactions.append(word)
                break
            break
        elif len(user_sort_word) == 0:
            print("\nВведен некорректный ответ.\n")
            continue
    return bank_transactions


def result_transaction(bank_transactions, user_input):
    """Ввод итогового спика"""

    print("\nРаспечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(bank_transactions)}\n")

    for i in bank_transactions:
        description = str(i["description"])
        print(get_date(i["date"]), description)
        if user_input == "1":
            amount = i["operationAmount"]["amount"]
            if description == "Открытие вклада":
                print(f"{mask_account_card(str(i["to"]))}")
            else:
                print(f"{mask_account_card(str(i["from"]))} -> {mask_account_card(str(i["to"]))}")
            print(f"{amount} {i["operationAmount"]["currency"]["name"]}\n")
        else:
            amount = int(i["amount"])
            if description == "Открытие вклада":
                print(f"{mask_account_card(str(i["to"]))}")
            else:
                print(f"{mask_account_card(i["from"])} -> {mask_account_card(str(i["to"]))}")
            print(f"{amount} {i["currency_code"]}\n")


def main():
    """Основная логика проекта"""
    bank_transactions, user_input = select_option()
    bank_transactions = status_sort_option(bank_transactions)
    bank_transactions = date_sort_option(bank_transactions)
    bank_transactions = trans_sort_option(bank_transactions, user_input)
    bank_transactions = sort_word_option(bank_transactions)
    result_transaction(bank_transactions, user_input)


if __name__ == "__main__":
    main()
