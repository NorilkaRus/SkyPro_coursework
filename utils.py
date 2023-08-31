import json
from heapq import nlargest

# Здесь функции для чтения файла и нахождения 5 последних операций
def read_all_operations(operations):
    """
    Принимает файл с операциями и возвращает все операции из файла
    :param operations: JSON-файл с операциями
    :return: читабельный для Python список операций
    """
    with open(operations) as file:
        file_readed = file.read()
        result = json.loads(file_readed)
        return result


def date_to_number(date):
    """
    Принимает строку, которой обозначается дата, и возвращает целое число
    :param date: "2019-08-26T10:50:58.294041"
    :return: 20190826
    """
    date = date.split("T")
    number = date[0].replace("-", "")
    return int(number)


def check_executing(operation):
    """
    Принимает операцию и возвращает True или False в зависимости о того, была ли операция выполнена
    :param operation: словарь с параметрами операции
    :return: True или False
    """
    if operation["state"] == "EXECUTED":
        return True
    return False


def make_dict_of_dates(operations):
    """
    Принимает файл с операциями и возвращает словарь
    с датами исполненных операций в исходном виде и в виде чисел
    :param operations: "operations.json"
    :return: {'2019-08-26T10:50:58.294041': 20190826, '2019-07-03T18:35:29.512364': 20190703, ...}
    """
    dict_of_dates = {}
    operations = read_all_operations(operations)
    for item in operations:
        if 'date' in item and check_executing(item) == True:
            dict_of_dates[item['date']] = date_to_number(item['date'])
    return dict_of_dates


def dict_to_list(dict):
    """
    Принимает словарь с датами операций и возвращает список из чисел
    :param dict: {'2019-08-26T10:50:58.294041': 20190826, '2019-07-03T18:35:29.512364': 20190703, ...}
    :return: [20190826, 20190703,...]
    """
    list_of_dates = []
    for key, value in dict.items():
        list_of_dates.append(value)
    return list_of_dates


def find_operation(date, operations):
    """
    Принимает дату и файл с операциями и возвращает операцию с выбранной датой
    :param date: "2019-08-26T10:50:58.294041", "operations.json"
    :param operations: {'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', ...}
    :return:
    """
    for item in read_all_operations(operations):
        if 'date' in item and date == item['date']:
            return item
    return "None"


def show_last_operatons(operations, count):
    """
    Принимает файл с операциями и число и возвращает список с последними 5 исполненными операциями
    :param operations: "operations.json", 5
    :return: [{'id': 863064926, 'state':...}, {...}, ...]
    """
    dict_of_dates = make_dict_of_dates(operations)
    list_of_dates = dict_to_list(dict_of_dates)
    last_five_dates = nlargest(count, list_of_dates)
    last_five_operations = []
    for date, number in dict_of_dates.items():
        if number in last_five_dates:
            last_five_dates.remove(number)
            last_five_operations.append(find_operation(date, operations))
    return last_five_operations


# Здесь функции для правильного отображения операций
def display_correct_date(date):
    """
    Принимает дату из файла и возвращает читабельную дату в формате "дд.мм.гггг"
    :param numeric: "2019-08-26T10:50:58.294041"
    :return: 26.08.2019
    """
    numeric = str(date_to_number(date))
    year = numeric[:4]
    month = numeric[4:6]
    day = numeric[6:]
    return f"{day}.{month}.{year}"


def hide_card_number(card_info):
    """
    Принимает данные о карте и возвращает номер карты в формате XXXX XX** **** XXXX
    :param card_info: "Maestro 1596837868705199"
    :return: "Maestro 1596 83** **** 5199"
    """
    card_info = card_info.split(" ")
    card_number = card_info[-1]
    card_number = f"{''.join(card_info[:-1])} {card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    return card_number


def hide_count_number(count_info):
    """
    Принимает данные о счете и возвращает номер счета в формате **XXXX
    :param count_info: "Счет 64686473678894779589"
    :return: "**9589"
    """
    count_info = count_info.split(" ")
    count_number = count_info[1]
    count_number = f"{count_info[0]} **{count_number[-4:]}"
    return count_number


def display_operation(operation):
    """
    Принимает словарь с операцией и возвращает человекочитаемый текст
    :param operation: {"id": 939719570, "state": "EXECUTED", ...}
    :return: 14.10.2018 Перевод организации
    Visa Platinum 700079 ** ** ** 6361 -> Счет ** 9638
    82771.72 руб.
    """
    date = display_correct_date(operation['date'])
    description = operation['description']
    from_exist = operation.get('from', "dont")
    if from_exist != "dont":
        if 'Счет' in operation['from']:
            wherefrom = hide_count_number(operation['from'])
        else:
            wherefrom = hide_card_number(operation['from'])
    else:
        wherefrom = ""

    to_exist = operation.get('to', "dont")
    if to_exist != "dont":
        if 'Счет' in operation['to']:
            wherever = hide_count_number(operation['to'])
        else:
            wherever = hide_card_number(operation['to'])
    else:
        wherever = ""

    amount = operation['operationAmount']['amount']
    currency = operation['operationAmount']['currency']['name']

    return f"""{date} {description}
{wherefrom} -> {wherever}
{amount} {currency}
"""

