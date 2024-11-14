checklist = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "AUTHORIZATION", "date": "2018-10-14T08:21:33.419441"},
    {"id": 615064591, "state": "EXECUTED", "date": "2019.08.18T08:21:33.419441"},
    {"id": 615064591, "state": "CANCELED", "date": "2017-05-10T08:21:33.419441"},
    {"id": 615064591, "state": "CANCELED", "date": "2017-05-10T08:21:33.419441"},
    {"id": 615064591, "state": "PROCESSING", "date": "2017/05/10T08:21:33.419441"},
]


def filter_by_state(dictionaries, state="EXECUTED"):
    """Функция возвращает новый список словарей у которых ключ state соответствует указанному значению"""

    new_dictionaries = [i for i in dictionaries if i["state"] == state]

    return new_dictionaries


print(filter_by_state(checklist, "AUTHORIZATION"))


def sort_by_date(my_lists, sort_date=True):
    """Функция возвращает новый список, отсортированный по дате"""

    new_list = [sorted(my_lists, key=lambda x: x["date"], reverse=sort_date)]

    return new_list


print(sort_by_date(checklist, sort_date=True))
