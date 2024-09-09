import pytest

from src.masks import get_mask_account, get_mask_card_number

def test_mask_card_number(test_no_number, test_wrong_number):
    """Тестирование правильности маскирования, отсутствуетвия и  нестандартные длины номеров карты"""

    assert get_mask_card_number(7000792289606361) == "7000 79** **** 6361"
    assert get_mask_card_number(700079228960636) == test_wrong_number
    assert get_mask_card_number(" ") == test_no_number
    assert get_mask_card_number("") == test_no_number


def test_mask_account(test_no_number, test_wrong_number):
    """Тестирование правильности маскирования, отсутствуетвия и  нестандартные длины номеров счета"""

    assert get_mask_account(73654108430135874305) == "**4305"
    assert get_mask_account(73654108430135874305755) == test_wrong_number
    assert get_mask_account(" ") == test_no_number
    assert get_mask_account("") == test_no_number