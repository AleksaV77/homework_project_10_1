import re
from src.masks import get_mask_card_number, get_mask_account

def mask_account_card(number_card_or_account):
    """Обрабатывает информацию о картах и счетах"""

    if "Счет" in number_card_or_account:
        return "Счет " + get_mask_account(number_card_or_account)
    else:
        return number_card_or_account[0:-16] + get_mask_card_number(number_card_or_account)

result = mask_account_card("Счет 35383033474447895560")
result_2 = mask_account_card("Visa Gold 5999414228426353")

print(result)
print(result_2)