def get_mask_card_number(card: str) -> str:
    """Функция возвращает мсакировку банковской карты"""
    if card.isdigit() and len(card) == 16:
        return f"{card[:4]} {card[4:6]}{"*" * 2} {"*" * 4} {card[12:]}"
    else:
        return ""


if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))


def get_mask_account(acc: str) -> str:
    """Функция возвращает маскировку номера счета"""
    if acc.isdigit() and len(acc) == 20:
        return f"{'*' * 2}{acc[-4::]}"
    else:
        return ""


if __name__ == "__main__":
    print(get_mask_account("73654108430135874305"))
