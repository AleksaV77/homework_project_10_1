import logging
from typing import Union

logger = logging.getLogger()
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s: %(filename)s: %(levelname)s: %(message)s",
    filename="..//logs//masks.log",
    encoding="utf-8",
    filemode="w",
)


def get_mask_card_number(user_card_number: Union[int, str]) -> Union[int, str]:
    """Маскировка номера банковской карты"""

    user_card_number_str = str(user_card_number)
    new_user_card_number = ""

    if len(user_card_number_str) == 16:
        logging.info("Маскировка номера банковской карты")
        return f"{user_card_number_str[-16:-12]} {user_card_number_str[-12:-10]}** **** {user_card_number_str[-4:]}"
    elif user_card_number_str == "" or user_card_number_str == " ":
        logging.error("Нет номера карты или счета")
        return "Нет номера карты или счета"
    elif len(user_card_number_str) < 16 or len(user_card_number_str) > 16:
        logging.error("Не правильный номер")
        return "Не правильный номер"

    return new_user_card_number


def get_mask_account(user_account_number: Union[int, str]) -> Union[int, str]:
    """Маскировки номера банковского счета"""

    user_account_number = str(user_account_number)
    new_user_account_number = ""

    if len(user_account_number) == 20:

        logging.info("Маскировка номера банковского счета")
        return f"**{user_account_number[-4:]}"
    elif user_account_number == "" or user_account_number == " ":
        logging.error("Нет номера карты или счета")
        return "Нет номера карты или счета"
    elif len(user_account_number) < 20 or len(user_account_number) > 20:
        logging.error("Не правильный номер")
        return "Не правильный номер"

    return new_user_account_number


if __name__ == "__main__":
    print(get_mask_card_number("599941422842635"))
    print(get_mask_account("73654108430135874305"))
