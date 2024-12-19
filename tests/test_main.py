from unittest.mock import patch

from main import (date_sort_option, list_financial_transactions_line, result_transaction, select_option,
                  sort_word_option, status_sort_option, trans_sort_option)


@patch("main.list_financial_transactions_csv")
@patch("main.input")
def test_select_option_csv(mock_input, mock_file, test_main_file_xlsx_csv):
    mock_input.return_value = "2"
    mock_file.return_value = test_main_file_xlsx_csv
    assert select_option() == (test_main_file_xlsx_csv, "2")


@patch("main.list_financial_transactions_excel")
@patch("main.input")
def test_select_option_xlsx(mock_input, mock_file, test_main_file_xlsx_csv):
    mock_input.return_value = "3"
    mock_file.return_value = test_main_file_xlsx_csv
    assert select_option() == (test_main_file_xlsx_csv, "3")


@patch("main.list_financial_transactions")
@patch("main.input")
def test_select_option(mock_input, mock_file, test_main_file_json):
    mock_input.return_value = "1"
    mock_file.return_value = test_main_file_json
    assert select_option() == (test_main_file_json, "1")


@patch("main.input")
def test_status_sort_option(mock_input, test_main_file_xlsx_csv):
    mock_input.return_value = "PENDING"
    assert status_sort_option(test_main_file_xlsx_csv) == [
        {
            "id": 5457678.0,
            "state": "PENDING",
            "date": "2023-11-04T10:39:34Z",
            "amount": 22951.0,
            "currency_name": "Yuan Renminbi",
            "currency_code": "CNY",
            "from": "Mastercard 6219443780959412",
            "to": "Visa 4786131684105875",
            "description": "Перевод с карты на карту",
        },
        {
            "id": 1999804.0,
            "state": "PENDING",
            "date": "2023-10-28T11:17:31Z",
            "amount": 34455.0,
            "currency_name": "Ruble",
            "currency_code": "RUB",
            "from": "Счет 42109207415591580635",
            "to": "Счет 74058089109726743250",
            "description": "Перевод со счета на счет",
        },
    ]


@patch("main.input")
def test_date_sort_option(mock_input, test_main_date_sort, test_main_file_xlsx_csv):
    mock_input.side_effect = ["да", "по убыванию"]
    assert date_sort_option(test_main_file_xlsx_csv) == test_main_date_sort


@patch("main.input")
def test_date_sort_option_2(mock_input, test_main_date_sort_2, test_main_file_xlsx_csv):
    mock_input.side_effect = ["да", "по возрастанию"]
    assert date_sort_option(test_main_file_xlsx_csv) == test_main_date_sort_2


@patch("main.input")
def test_date_sort_option_3(mock_input, test_main_file_xlsx_csv):
    mock_input.return_value = "нет"
    assert date_sort_option(test_main_file_xlsx_csv) == test_main_file_xlsx_csv


@patch("main.input")
def test_trans_sort_option(mock_input, test_main_file_xlsx_csv, test_main_trans_rub):
    mock_input.return_value = "да"
    assert trans_sort_option(test_main_file_xlsx_csv, "2") == [
        {
            "id": 1999804.0,
            "state": "PENDING",
            "date": "2023-10-28T11:17:31Z",
            "amount": 34455.0,
            "currency_name": "Ruble",
            "currency_code": "RUB",
            "from": "Счет 42109207415591580635",
            "to": "Счет 74058089109726743250",
            "description": "Перевод со счета на счет",
        },
        {
            "id": 4234093.0,
            "state": "EXECUTED",
            "date": "2021-07-08T07:31:21Z",
            "amount": 23182.0,
            "currency_name": "Ruble",
            "currency_code": "RUB",
            "from": "Visa 0773092093872450",
            "to": "Discover 8602781449570491",
            "description": "Перевод с карты на карту",
        },
    ]


@patch("main.input")
def test_trans_sort_option_2(mock_input, test_main_file_xlsx_csv):
    mock_input.return_value = "нет"
    assert trans_sort_option(test_main_file_xlsx_csv, "3") == test_main_file_xlsx_csv


@patch("main.input")
def test_sort_word_option(mock_input, test_main_file_xlsx_csv):
    mock_input.side_effect = ["да", "Перевод"]
    assert list_financial_transactions_line(test_main_file_xlsx_csv, "Перевод") == test_main_file_xlsx_csv


@patch("main.input")
def test_sort_word_option_2(mock_input, test_main_file_json):
    mock_input.return_value = "нет"
    assert sort_word_option(test_main_file_json) == test_main_file_json


@patch("main.input")
def test_sort_word_option_3(mock_input, test_main_file_json):
    mock_input.side_effect = ["да", "организации"]
    assert list_financial_transactions_line(test_main_file_json, "организации") == [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
    ]


@patch("main.input")
def test_result_transaction(test_main_file_xlsx_csv):
    assert result_transaction(test_main_file_xlsx_csv, "2") is None
