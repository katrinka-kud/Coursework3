import utils


def main():
    data = utils.load_data('operations.json')  # получаем данные из файла 'operations.json'
    all_executed = utils.get_executed_transactions(data)  # получаем список выполненных транзакций
    last_five_transactions = utils.get_last_value(all_executed, 5)  # получаем список последних 5 транзакций
    for i in last_five_transactions:
        date = utils.get_converted_date(i['date'])  # получаем дату операции из транзакции
        operation = i['operation']  # получаем описание операции из транзакции
        card_number_sender = utils.hide_sender_number(last_five_transactions)  # получаем номер счета отправителя
        card_number_recipient = utils.hide_recipient_number(last_five_transactions)  # получаем номер счета получателя
        print(date, operation)
        print(f"{card_number_sender} -> {card_number_recipient}")
        print(f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}\n")


if __name__ == '__main__':
    main()
