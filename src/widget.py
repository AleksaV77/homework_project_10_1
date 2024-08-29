import re
from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(number_card_or_account: str) -> str | None:
    """Обрабатывает информацию о картах и счетах"""

    if "Счет" in number_card_or_account:
        return "Счет " + get_mask_account(number_card_or_account)
    else:
        return number_card_or_account[0:-16] + get_mask_card_number(number_card_or_account)


def get_date(date: str) -> str | None:
    """возвращает строку с датой в формате "ДД.ММ.ГГГГ ("11.03.2024")"""

    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
