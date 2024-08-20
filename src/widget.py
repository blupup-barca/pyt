from masks import get_mask_account, get_mask_account


#Примеры входных данных для проверки функции:
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
    """Функция принимает тип и номер карты или номер счета и выводит их замаскированными"""
   split_numbers_card = type_and_number_card.split()
   new_list = []
   name_and_number = []
   for numb_or_name in split_numbers_card:
       if numb_or_name.isalpha():
           name_and_number.append(numb_or_name)
       elif numb_or_name.isdigit():
           if len(numb_or_name) == 16:
               masks_numb_card = get_mask_account(numb_or_name)
               name_and_number.append(masks_numb_card)
               new_list.append(name_and_number)
               name_and_number = list()
           elif len(numb_or_name) == 20:
               masks_numb_account = get_mask_account(numb_or_name)
               name_and_number.append(masks_numb_account)
               new_list.append(name_and_number)
               name_and_number = list()
       else:
           continue
   ready_date = ""
   for values_card in new_list:
       translate_into_a_line = " ".join(values_card)
       ready_date += (translate_into_a_line + "\n")
   return ready_date


def get_data(raw_date: str) -> str:
    """Функиця принимает данные о дате и выводит её"""
    slice_date = raw_date[:10]
    date_clear = ""
    for one_symbol in range(len(slice_date)):
        if slice_date[one_symbol].isdigit():
            date_clear += slice_date[one_symbol]
        else:
            date_clear += " "
    date_clear_split = date_clear_split()
    split_date = date_clear_split[::-1]
    final_result = ".".join(split_date)
    return final_result


if __name__ == "__main__":
    print(mask_account_card(card_and_account_numbers))
    print(get_data())