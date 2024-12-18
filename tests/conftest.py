import pytest


@pytest.fixture
def test_no_date():
    return "Отсутствует дата"


@pytest.fixture
def test_by_state_1():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 615064591, "state": "EXECUTED", "date": "2019.08.18T08:21:33.419441"},
    ]


@pytest.fixture
def test_by_state_2():
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2017-05-10T08:21:33.419441"},
        {"id": 615064591, "state": "CANCELED", "date": "2017-05-10T08:21:33.419441"},
    ]


@pytest.fixture
def test_by_state_3():
    return [{"id": 615064591, "state": "PROCESSING", "date": "2017/05/10T08:21:33.419441"}]


@pytest.fixture
def test_by_state_4():
    return [{"id": 615064591, "state": "AUTHORIZATION", "date": "2018-10-14T08:21:33.419441"}]


@pytest.fixture
def test_no_by_state():
    return []


@pytest.fixture
def test_sort_date_wane():
    return [
        {"id": 615064591, "state": "EXECUTED", "date": "2019.08.18T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "AUTHORIZATION", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 615064591, "state": "PROCESSING", "date": "2017/05/10T08:21:33.419441"},
        {"id": 615064591, "state": "CANCELED", "date": "2017-05-10T08:21:33.419441"},
        {"id": 615064591, "state": "CANCELED", "date": "2017-05-10T08:21:33.419441"},
    ]


@pytest.fixture
def test_sort_date_rise():
    return [
        {"id": 615064591, "state": "CANCELED", "date": "2017-05-10T08:21:33.419441"},
        {"id": 615064591, "state": "CANCELED", "date": "2017-05-10T08:21:33.419441"},
        {"id": 615064591, "state": "PROCESSING", "date": "2017/05/10T08:21:33.419441"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "AUTHORIZATION", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "EXECUTED", "date": "2019.08.18T08:21:33.419441"},
    ]


@pytest.fixture
def usd_transactions():
    return [
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
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
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
    ]


@pytest.fixture
def rub_transactions():
    return [
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
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def eur_transactions():
    return [
        {
            "id": 939719777,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
    ]


@pytest.fixture
def cny_transactions():
    return [
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


@pytest.fixture
def test_financial():
    return [
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
    ]


@pytest.fixture
def test_financial_1():
    return [
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
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def test_financial_2():
    return [
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
    ]


@pytest.fixture
def test_financial_3():
    return [
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        }
    ]


@pytest.fixture
def test_categories():
    res = {"Перевод организации": 2, "Перевод со счета на счет": 2, "Перевод с карты на карту": 1}
    return res


@pytest.fixture
def test_categories_2():
    res = {"Перевод со счета на счет": 2}
    return res


@pytest.fixture
def test_categories_3():
    return {
        "Перевод с карты на карту": 587,
        "Открытие вклада": 185,
        "Перевод организации": 117,
        "Перевод со счета на счет": 110,
    }


@pytest.fixture
def test_main_file_xlsx_csv():
    return [
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


@pytest.fixture
def test_main_file_json():
    return [
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
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431",
        },
    ]


@pytest.fixture
def test_main_trans_rub():
    return [
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


@pytest.fixture
def test_main_date_sort():
    return [
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


@pytest.fixture
def test_main_date_sort_2():
    return [
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
    ]
