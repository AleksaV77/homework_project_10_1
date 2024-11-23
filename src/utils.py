import json
import logging
from json import JSONDecodeError

logger = logging.getLogger()
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s: %(filename)s: %(levelname)s: %(message)s",
    filename="../logs/utils.log",
    encoding="utf-8",
    filemode="w",
)


def list_financial_transactions(file):
    """возвращает список словарей с данными о финансовых транзакциях"""

    with open(file, "r", encoding="utf-8") as f:
        try:
            operations = json.load(f)
            logging.info("Список словарей с данными о финансовых транзакциях")
            return operations
        except JSONDecodeError:
            logging.error("Пустой список")
            return []


file_operation = list_financial_transactions("C:/Users/asurk/PycharmProjects/Homework_Project1/data/operations_3.json")
print(file_operation)
