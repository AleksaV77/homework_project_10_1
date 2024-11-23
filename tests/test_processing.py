from src.processing import checklist, filter_by_state, sort_by_date


def test_filter_by_state(test_by_state_1, test_by_state_2, test_no_by_state, test_by_state_3, test_by_state_4):
    """Тестирование фильтрации списка словарей по заданному статусу state"""

    assert filter_by_state(checklist, "EXECUTED") == test_by_state_1
    assert filter_by_state(checklist, "CANCELED") == test_by_state_2
    assert filter_by_state(checklist, "PROCESSING") == test_by_state_3
    assert filter_by_state(checklist, "AUTHORIZATION") == test_by_state_4
    assert filter_by_state(checklist, "CANCELE") == test_no_by_state


def test_sort_by_date(test_sort_date_wane, test_sort_date_rise):
    """Тестирование сортировки списка словарей по датам в порядке убывания и возрастания, сортировка одинаковых дат"""

    assert sort_by_date(checklist, sort_date=True) == test_sort_date_wane
    assert sort_by_date(checklist, sort_date=False) == test_sort_date_rise
