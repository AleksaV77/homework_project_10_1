from unittest.mock import patch

from dotenv import load_dotenv

from src.external_api import sum_transaction


@patch("src.external_api.sum_transaction")
def test_sum_transaction_rub(mock_val):

    mock_val.return_value.json.return_value = 31957.58, 8221.37
    file = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
    ]

    assert sum_transaction(file) == 31957.58, 8221.37


@patch("src.external_api.requests.get")
def test_sum_transaction_usd(mock_vals):
    load_dotenv(".env")
    mock_vals.return_value.json.return_value = {"result": 828243.989842}
    files = [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        }
    ]

    assert sum_transaction(files) == 828243.989842
