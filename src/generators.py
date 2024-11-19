from typing import Generator, Iterator, List

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 939719777,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "EUR", "code": "EUR"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
    {
        "id": 763226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "юа́нь", "code": "CNY"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def filter_by_currency(transaction: List[dict], code: str) -> Iterator:
    """Функция выдает список транзакций, где валюта операции соответствует заданной"""

    if len(transaction) > 0:
        for i in transaction:
            if i["operationAmount"]["currency"]["code"] == code:
                yield i
    elif len(transaction) < 0:
        raise StopIteration("Нет списка транзакции")
    elif transaction == list():
        raise AssertionError("Нет списка транзакции")


usd_transactions = filter_by_currency(transactions, "USD")
rub_transactions = filter_by_currency(transactions, "RUB")
eur_transactions = filter_by_currency(transactions, "EUR")
cny_transactions = filter_by_currency(transactions, "CNY")

for _ in range(1):
    print(next(cny_transactions))


def transaction_descriptions(transaction: List[dict]) -> Iterator:
    """Функция возвращает описание каждой операции"""

    if len(transaction) > 0:
        for i in transaction:
            if i["description"] != "":
                yield i["description"]
    elif len(transaction) < 0:
        raise StopIteration("Нет операций")
    elif transaction == list():
        raise AssertionError("Нет операций")


descriptions = transaction_descriptions(transactions)

print(next(descriptions))
print(next(descriptions))
print(next(descriptions))
print(next(descriptions))
print(next(descriptions))
print(next(descriptions))
print(next(descriptions))


def card_number_generator(start: int, end: int) -> Generator:
    """Функция генерирует номера карт"""

    for number in range(start, end + 1):
        number_card = str(number)
        if len(number_card) > 16:
            raise BaseException("Недопустимое значение")
        while len(number_card) < 16:
            number_card = "0" + number_card

        formatted_number_card = f"{number_card[:4]} {number_card[4:8]} {number_card[8:12]} {number_card[12:]}"

        yield formatted_number_card


for card_number in card_number_generator(0, 3):
    print(card_number)
