from src.search_transactions import categories_operations, categories_transactions, list_financial_transactions_line


def test_list_financial(test_financial, test_financial_1, test_financial_2, test_financial_3):
    assert list_financial_transactions_line(test_financial, "организации") == test_financial_1
    assert list_financial_transactions_line(test_financial, "со счета") == test_financial_2
    assert list_financial_transactions_line(test_financial, "gthtdjl") == []
    assert list_financial_transactions_line(test_financial, "с карты") == test_financial_3


def test_categories_transactions(test_financial, test_categories, test_categories_2, test_categories_3):
    assert categories_transactions(test_financial, categories_operations) == test_categories
    assert categories_transactions(test_financial, ["Перевод со счета на счет"]) == test_categories_2
    assert categories_transactions(test_financial, []) == {}
    assert categories_transactions(test_financial, ["Перевод с карты на карту"]) == {"Перевод с карты на карту": 1}
