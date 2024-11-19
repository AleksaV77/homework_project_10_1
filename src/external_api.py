import os

import requests
from dotenv import load_dotenv

from src.utils import list_financial_transactions


def sum_transaction(transaction: dict[str | float]) -> float:
    """возвращает сумму транзакции в рублях"""
    load_dotenv(".env")
    apikey = os.getenv("API_KEY")
    headers = {"apikey": apikey}

    for i in transaction:
        amount_transaction = float(i["operationAmount"]["amount"])
        if i["operationAmount"]["currency"]["code"] == "RUB":
            return amount_transaction
        elif i["operationAmount"]["currency"]["code"] != "RUB":
            url = f"https://api.apilayer.com/exchangerates_data/convert?from=USD&to=RUB&amount={amount_transaction}"
            response = requests.get(url, headers=headers)
            json_result = response.json()
            return float(json_result["result"])


if __name__ == "__main__":
    file = "C:/Users/asurk/PycharmProjects/Homework_Project1/data/operations_3.json"
    json_file = list_financial_transactions(file)
    print(sum_transaction(json_file))
