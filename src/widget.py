from masks import get_mask_account

# примеры входных данных для проверки функции
card_and_account_numbers = """ Maestro 1596837868705199
Счет 64686473678894779589
MasterCard 7158300734726758
Счет 35383033474447895560
Visa Classic 6831982476737658
Visa Platinum 8990922113665229
Visa Gold 5999414228426353
Счет 73654108430135874305 """

date = "2024-03-11T02:26:18.671407"


def mask_account_card(type_and_number_card: str) -> str:
    """
    Функция принимает тип и номер карты или номер счета и выводит их замаскированными
    """
    split_account_or_card = type_and_number_card.split(" ")
    if "Счет" in split_account_or_card[0]:
        masked_number = 16
get_mask_account(split_account_or_card[-1])
    else:
        masked_number = 20
get_mask_card_number(split_account_or_card[-1])
    split_account_or_card[-1] = masked_number
    return " ".join(split_account_or_card)


def get_date(date: str) -> str:
    """
    Функиця принимает данные о дате и выводит её
    """
    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"


if __name__ == "__main__":
    print(mask_account_card(card_and_account_numbers))
    print(get_date("2024-03-11T02:26:18.671407"))
