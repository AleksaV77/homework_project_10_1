from typing import Union

from src.processing import filter_by_state, sort_by_date, checklist


def test_filter_by_state(test_by_state_1, test_by_state_2, test_no_by_state, test_by_state_3, test_by_state_4):
    """Тестирование фильтрации списка по заданному статусу state, отсутствие статуса, различные значения статуса"""

    assert filter_by_state(checklist, "EXECUTED") == test_by_state_1
    assert filter_by_state(checklist, "CANCELED") == test_by_state_2
    assert filter_by_state(checklist, "PROCESSING") == test_by_state_3
    assert filter_by_state(checklist, "AUTHORIZATION") == test_by_state_4
    assert filter_by_state(checklist, "CANCELE") == test_no_by_state


def test_sort_by_date(test_sort_date_wane: list[list[dict[str, str | int]]], test_sort_date_rise: list[list[dict[str, str | int]]]) -> list[list[dict[str, str | int]]]:
    """Тестирование сортировки списка по датам в по убыванию, возрастанию, одинаковые даты"""

    assert sort_by_date(checklist, sort_date=True) == test_sort_date_wane
    assert sort_by_date(checklist, sort_date=False) == test_sort_date_rise
