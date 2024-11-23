from unittest.mock import patch

import pandas as pd

from src.utils_excel import list_financial_transactions_excel


@patch("src.utils_excel.pd.read_excel")
def test_list_financial_transactions_excel(mock_file):
    """Тестирование чтения существующего файла"""
    df = [{"id": 650703.0}]
    value = pd.DataFrame(df)
    mock_file.return_value = value
    result = "C:/Users/asurk/PycharmProjects/Homework_Project1/data/transactions_excel.xlsx"

    assert list_financial_transactions_excel(result) == df


@patch("src.utils_excel.list_financial_transactions_excel")
def test_list_financial_transactions_excel_2(mock_file):
    """Тестирование чтения при отсутствии файла"""
    df = []
    value = pd.DataFrame(df)
    mock_file.return_value = value
    result = "C:/Users/asurk/PycharmProjects/Homework_Project1/data/tran_excel.xlsx"
    assert list_financial_transactions_excel(result) == f"файл {result} не найден"


@patch("src.utils_excel.list_financial_transactions_excel")
def test_list_financial_transactions_not_excel(mock_file):
    """Тестирование чтения пустого файла"""
    df = []
    value = pd.DataFrame(df)
    mock_file.return_value = value
    assert list_financial_transactions_excel([]) == []
