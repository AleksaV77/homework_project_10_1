from typing import Union


def get_mask_card_number(user_card_number: Union[int, str]) -> Union[int, str]:
    """Маскировка номера банковской карты"""

    user_card_number = str(user_card_number)

    return f"{user_card_number[-16:-12]} {user_card_number[-12:-10]}** **** {user_card_number[-4:]}"


def get_mask_account(user_account_number: Union[int, str]) -> Union[int, str]:
    """Маскировки номера банковского счета"""

    user_account_number = str(user_account_number)

    return f"**{user_account_number[-4:]}"
