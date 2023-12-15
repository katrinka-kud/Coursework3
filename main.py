from utils import *
from data.settings import OPERATIONS_PATH


def main():
    data = load_data(OPERATIONS_PATH)  # получаем данные из файла 'operations.json'
    all_executed = get_executed_transactions(data)  # получаем список выполненных транзакций
    last_five_transactions = get_last_value(all_executed, 5)  # получаем список последних 5 транзакций
    for i in last_five_transactions:
        date = get_converted_date(i['date'])  # получаем дату операции из транзакции
        operation = i['description']  # получаем описание операции из транзакции
        card_number_sender = hide_sender_number(last_five_transactions)  # получаем номер счета отправителя
        card_number_recipient = hide_recipient_number(last_five_transactions)  # получаем номер счета получателя
        print(date, operation)
        print(f"{card_number_sender} -> {card_number_recipient}")
        print(f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}\n")


if __name__ == '__main__':
    main()
