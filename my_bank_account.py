import pickle

def my_bank_account():
    """
    Программа "Мой банковский счёт"
    Описание работы программы:
    Пользователь запускает программу у него на счету 0
    Программа предлагает следующие варианты действий
    1. состояние счёта
    1. пополнить счёт
    2. покупка
    3. история покупок
    4. выход

    1. состояние счёта
    при выборе этого пункта показывается текущая сумма на счету

    2. пополнение счета
    при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
    после того как пользователь вводит сумму она добавляется к счету
    снова попадаем в основное меню

    3. покупка
    при выборе этого пункта пользователю предлагается ввести сумму покупки
    если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
    если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
    снимаем деньги со счета
    сохраняем покупку в историю
    выходим в основное меню

    4. история покупок
    выводим историю покупок пользователя (название и сумму)
    возвращаемся в основное меню

    5. выход
    выход из программы
    """

    with open('account.txt', 'r') as f:
        account = float(f.read())
    try:
        with open('history_purchase.data', 'br') as f:
            number_purchase, history_purchase = pickle.load(f)
    except EOFError:
        number_purchase = 0
        history_purchase = {}

    print()
    print('"Мой банковский счёт"')
    while True:
        print()
        print('1. состояние счёта')
        print('2. пополнение счета')
        print('3. покупка')
        print('4. история покупок')
        print('5. выход')
        print()
        choice = input('Выберите пункт меню: ')
        if choice == '1':
            print(f'На Вашем счету {account} руб.')
        elif choice == '2':
            cash = float(input('Введите сумму для пополнения счёта: '))
            account += cash
        elif choice == '3':
            purchase = float(input('Введите сумму покупки: '))
            if purchase > account:
                print('У Вас на счету недостаточно средств. Пополните счёт.')
                continue
            else:
                name_purchase = input('Введите название покупки: ')
                number_purchase += 1
                account -= purchase
                history_purchase[number_purchase] = {name_purchase: purchase}
                with open('history_purchase.data', 'bw') as f:
                    pickle.dump([number_purchase, history_purchase], f)
        elif choice == '4':
            if len(history_purchase):
                for item in list(iter(history_purchase)):
                    purchase_name = list(history_purchase[item].keys())
                    price = list(history_purchase[item].values())
                    print(f'{item}) {purchase_name[0]} - {price[0]} руб.')
            else:
                print('В истории пока нет записей')
        elif choice == '5':
            with open('account.txt', 'w') as f:
                f.write(str(account))
            break
        else:
            print('Неверный пункт меню')