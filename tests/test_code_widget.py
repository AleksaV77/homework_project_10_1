import pytest

from src.widget import mask_account_card, get_date
from src.masks import get_mask_account, get_mask_card_number

@pytest.mark.parametrize("string, expected_result", [
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("Maestro 15968378687051", "Не правильный номер"),
    ("Visa Electron 4277255555555555", "Visa Electron 4277 25** **** 5555"),
    ("Visa Electron 4277255555555555456", "Не правильный номер"),
    ("Visa Electron ", "Нет номера карты или счета"),
    ("Счет 64686473678894779589", "Счет **9589"),
    ("Счет 64686473678894779", "Не правильный номер"),
    ("Счет ", "Нет номера карты или счета"),
    (" ", "Нет номера карты или счета"),
    ("", "Нет номера карты или счета")
])


def test_mask_account_card(string, expected_result):
    """Тест на тип маскировки карты или счета и некорректных входных данных"""

    assert mask_account_card(string) == expected_result


def test_get_date(test_no_date):
    """Тестирование правильности преобразования и отсутствие даты"""

    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("") == test_no_date