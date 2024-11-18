import pytest

from src.generators import (
    filter_by_currency,
    transaction_descriptions,
    card_number_generator, transactions
)

def test_filter_by_currency(usd_transactions, rub_transactions, eur_transactions, cny_transactions):

    assert list(filter_by_currency(transactions, "USD")) == usd_transactions
    assert list(filter_by_currency(transactions, "RUB")) == rub_transactions
    assert list(filter_by_currency(transactions, "EUR")) == eur_transactions
    assert list(filter_by_currency(transactions, "CNY")) == cny_transactions
    with pytest.raises(AssertionError):
        assert filter_by_currency([], "EUR") == "Нет списка транзакции"


def test_transaction_descriptions():

    des = transaction_descriptions(transactions)
    assert next(des) == "Перевод организации"
    assert next(des) == "Перевод организации"
    assert next(des) == "Перевод со счета на счет"
    assert next(des) == "Перевод со счета на счет"
    assert next(des) == "Перевод с карты на карту"
    assert next(des) == "Перевод организации"
    assert next(des) == "Перевод с карты на карту"
    with pytest.raises(AssertionError):
        assert transaction_descriptions([]) == "Нет операций"


@pytest.mark.parametrize("start, end", [(9999999999999998, 9999999999999999)])
def test_card_number_generator(start, end):

    gen = card_number_generator(start, end)
    assert next(gen) == "9999 9999 9999 9998"
    assert next(gen) == "9999 9999 9999 9999"

    gen_2 = card_number_generator(0, 3)
    assert next(gen_2) == "0000 0000 0000 0000"
    assert next(gen_2) == "0000 0000 0000 0001"
    assert next(gen_2) == "0000 0000 0000 0002"
    assert next(gen_2) == "0000 0000 0000 0003"

    with pytest.raises(BaseException):
        assert card_number_generator(11111111111111111, 11111111111111112) == "Недопустимое значение"
