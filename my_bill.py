# пополнение счёта
def refill():
    while True:
        try:
            print()
            sum = float(input('Введите сумму пополнения: '))
            if sum <=0:
                raise ()
            break
        except:
            print('Ошибка ввода суммы')
    return sum


# покупка
# возвращает tuple с названием и суммой покупки,
# действие с историей происходит за пределами функции
def purchase(current_bill):
    print()

    if (current_bill == 0):
        print('Недостаточно средств для совершения покупки, пополните счёт')
        return None

    while True:
        try:
            purchase_sum = float(input('Введите сумму покупки: '))
            if purchase_sum <= 0:
                raise ()
            break
        except:
            print('Ошибка ввода суммы')

    if (purchase_sum > current_bill):
        print('Недостаточно средств для совершения покупки')
        return None

    purchase_name = input('Введите название покупки: ') # оставлена возможность ввода пустой строки
    return (purchase_name, purchase_sum)


# вывод истории покупок
def show_history(history):
    print()

    if (len(history) == 0):
        print('Ещё не было покупок')
        return

    print('История покупок:')
    for hist in history:
        print(hist[0], ': ', hist[1], sep='')

def my_bill():
    bill = 0.0
    history = []

    while True:
        print()
        print('Текущий счёт:', bill)
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        print()

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            bill += refill()
        elif choice == '2':
            hist = purchase(bill)
            if (hist != None):
                history.append(hist)
                bill -= hist[1]
        elif choice == '3':
            show_history(history)
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')
