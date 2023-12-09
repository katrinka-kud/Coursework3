import datetime
import json


# import utils


def load_data(filename):
    """Получает данные из списка json-файла в формате списка словарей.
    :param filename: имя файла.
    :return: список словарей."""
    with open(filename, 'r') as f:
        return json.load(f)


def get_converted_date(data, a="%Y-%m-%dT%H:%M:%S.%f"):
    """Получает дату в нужном формате ДД.ММ.ГГГГ.
    :param data: дата.
    :param a: формат даты."""
    return datetime.datetime.strptime(data, a).strftime("%d.%m.%Y")


def get_executed_transactions(data):
    """Перебирает список транзакций из списка json-файла и оставляет те, у которых
    есть значение 'from', а значение 'state' == 'EXECUTED'."""
    data_list = []
    for transaction in data:
        if 'from' not in transaction:
            continue
        elif 'state' not in transaction:
            continue
        elif transaction['state'] == 'EXECUTED':
            data_list.append(transaction)

    return data_list


def get_last_value(data, last_value):
    """Получает последнее значение из списка.
    :param data: список.
    :param last_value: последнее значение.
    :return: последнее значение."""
    return data[:last_value]


def hide_part_number_from(data, last_value):
    """Скрывает цифры из номера счета отправителя"""
    data = sorted(data, key=lambda x: x['date'], reverse=True)
    return data[:last_value]


def hide_sender_number(data):
    """Скрывает цифры из номера счета отправителя"""
    for i in data:
        part_first_word = i['from'].split(' ')[0]  # получаем первое слово из значения 'from'
        part_second_word = i['from'].split(' ')[1]  # получаем второе слово из значения 'from'
        if part_second_word.isalpha():
            part_first_word = f'{part_first_word}{part_second_word}'
            part_second_word1 = list(i['from'].split(' ')[-1])[
                                0:4]  # получаем первые 4 знака из третьего слова из значения 'from'
            part_second_word2 = list(i['from'].split(' ')[-1])[
                                4:6]  # получаем вторые 2 знака из третьего слова из значения 'from'
            part_second_word3 = list(i['from'].split(' ')[-1])[
                                -4:]  # получаем последние 4 знака из третьего слова из значения 'from'
        elif part_second_word.isdigit():
            part_second_word1 = list(i['from'].split(' ')[1])[
                                0:4]  # получаем первые 4 знака из третьего слова из значения 'from'
            part_second_word2 = list(i['from'].split(' ')[1])[
                                4:6]  # получаем вторые 2 знака из третьего слова из значения 'from'
            part_second_word3 = list(i['from'].split(' ')[1])[
                                -4:]  # получаем последние 4 знака из третьего слова из значения 'from'
        a = f"{part_first_word} {''.join(part_second_word1)} {''.join(part_second_word2)} {''.join(part_second_word3)}"
        return a


def hide_recipient_number(data):
    """Скрывает цифры из номера счета получателя"""
    hide_part = data[0]['to']  # получаем первое слово из значения 'to'
    hide_part_first_word = hide_part.split(' ')[
        0]  # получаем последние 4 знака из второго слова из значения 'to'
    hide_part_second_word = list(hide_part.split(' ')[1])[
                            -4:]  # получаем последние 4 знака из второго слова из значения 'to'
    return f"{hide_part_first_word} **{''.join(hide_part_second_word)}"
