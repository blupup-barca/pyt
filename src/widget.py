from masks import mask_account, mask_card


def mask_account_card(cards_number: str) -> str:
    """Функция, маскировки карты"""
    if "Счет" in cards_number:
        return str(mask_account(cards_number))
    else:
        cards = mask_card(cards_number[-16:])
        get_mask_card: str = cards_number.replace(cards_number[-16:], cards)
        return get_mask_card


print(mask_account_card("Maestro 1596837868705199"))


def get_date(date: str) -> str:
    """Функция, перобразования даты"""

    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"


print(get_date("2024-03-11T02:26:18.671407"))
