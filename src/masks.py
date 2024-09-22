from typing import Union


def get_mask_card_number(user_card_number: Union[int, str]) -> Union[int, str]:
    """Маскировка номера банковской карты"""

    user_card_number_str = str(user_card_number)
    new_user_card_number = ""

    if len(user_card_number_str) == 16:
        new_user_card_number = (
            f"{user_card_number_str[-16:-12]} {user_card_number_str[-12:-10]}** **** {user_card_number_str[-4:]}"
        )
    elif user_card_number_str == "" or user_card_number_str == " ":
        new_user_card_number = "Нет номера карты или счета"
    elif len(user_card_number_str) < 16 or len(user_card_number_str) > 16:
        new_user_card_number = "Не правильный номер"

    return new_user_card_number


print(get_mask_card_number("599941422842635"))


def get_mask_account(user_account_number: Union[int, str]) -> Union[int, str]:
    """Маскировки номера банковского счета"""

    user_account_number = str(user_account_number)
    new_user_account_number = ""

    if len(user_account_number) == 20:
        new_user_account_number = f"**{user_account_number[-4:]}"
    elif user_account_number == "" or user_account_number == " ":
        new_user_account_number = "Нет номера карты или счета"
    elif len(user_account_number) < 20 or len(user_account_number) > 20:
        new_user_account_number = "Не правильный номер"

    return new_user_account_number


print(get_mask_account("73654108430135874305"))
