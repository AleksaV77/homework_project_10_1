from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number_card_or_account: str) -> str | None:
    """Обрабатывает информацию о картах и счетах"""

    card_or_account_info = number_card_or_account.split(" ")

    if "Счет" in card_or_account_info:
        if len(card_or_account_info[-1]) == 20:
            return f"{" ".join(card_or_account_info[:-1])} {get_mask_account(card_or_account_info[-1])}"
        else:
            return f"{get_mask_account(card_or_account_info[-1])}"
    elif "Счет" not in card_or_account_info:
        if len(card_or_account_info[-1]) == 16:
            return f"{" ".join(card_or_account_info[:-1])} {get_mask_card_number(card_or_account_info[-1])}"
        else:
            return f"{get_mask_card_number(card_or_account_info[-1])}"


print(mask_account_card("567"))


def get_date(date: str) -> str | None:
    """возвращает строку с датой в формате "ДД.ММ.ГГГГ ("11.03.2024")"""

    if date == "":
        return "Отсутствует дата"
    else:
        return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"


print(get_date("2024-03-11T02:26:18.671407"))
