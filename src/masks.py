def get_mask_card(card_number: str) -> str:
    """функция, маскировки номера карты"""
    new_list = list()
    new_list.append(card_number[0:4])
    new_list.append(card_number[4:6] + "**")
    new_list.append("****")
    new_list.append(card_number[12:])
    return "".join(new_list)


def get_mask_account(acc_number: str) -> str:
    """функция, маскировки номера счета"""
    new_list = list()
    new_list.append("**" + acc_number[-4:])
    return "".join(new_list)


# client_acc_number = 73654108430135874305
# client_card_number = 7000792289606361
# print(get_mask_account(str(client_acc_number)))
# print(get_mask_card(str(client_card_number)))
