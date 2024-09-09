import pytest

@pytest.fixture
def test_no_number():
    return "Нет номера карты или счета"

@pytest.fixture
def test_wrong_number():
    return "Не правильный номер"

@pytest.fixture
def test_no_date():
    return "Отсутствует дата"

@pytest.fixture
def test_by_state_1():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 615064591, 'state': 'EXECUTED', 'date': '2019.08.18T08:21:33.419441'}]


@pytest.fixture
def test_by_state_2():
    return [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2017-05-10T08:21:33.419441'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2017-05-10T08:21:33.419441'}]


@pytest.fixture
def test_by_state_3():
    return [{'id': 615064591, 'state': 'PROCESSING', 'date': '2017/05/10T08:21:33.419441'}]

@pytest.fixture
def test_by_state_4():
    return [{'id': 615064591, 'state': 'AUTHORIZATION', 'date': '2018-10-14T08:21:33.419441'}]

@pytest.fixture
def test_no_by_state():
    return []

@pytest.fixture
def test_sort_date_wane():
    return [[{'id': 615064591, 'state': 'EXECUTED', 'date': '2019.08.18T08:21:33.419441'},
             {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 615064591, 'state': 'AUTHORIZATION', 'date': '2018-10-14T08:21:33.419441'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
             {'id': 615064591, 'state': 'PROCESSING', 'date': '2017/05/10T08:21:33.419441'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2017-05-10T08:21:33.419441'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2017-05-10T08:21:33.419441'}]]


@pytest.fixture
def test_sort_date_rise():
    return [[{'id': 615064591, 'state': 'CANCELED', 'date': '2017-05-10T08:21:33.419441'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2017-05-10T08:21:33.419441'},
             {'id': 615064591, 'state': 'PROCESSING', 'date': '2017/05/10T08:21:33.419441'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'AUTHORIZATION', 'date': '2018-10-14T08:21:33.419441'},
             {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 615064591, 'state': 'EXECUTED', 'date': '2019.08.18T08:21:33.419441'}]]
