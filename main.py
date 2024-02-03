import datetime

passw = 0
balance = int(0)
limit = int(0)


def data_user_out():
    with open("data-man.txt", "w", encoding='utf-8') as out:
        out.write(f'{name},{year},{passw},{limit},{balance}')


def tran_write():
    with open("data-transaction.txt", "w", encoding='utf-8') as tran_out:
        for i in range(len(tran_name)):
            tran_out.write(str(tran_name[i]) + ",")
        tran_out.write('\n')
        for i in range(len(tran_sum)):
            tran_out.write(str(tran_sum[i]) + ",")
        tran_out.write('\n')
        for i in range(len(tran_count)):
            tran_out.write(str(tran_count[i]) + ",")
        tran_out.write('\n')


def tran_pay(balance):
    if int(tran_sum[to_do]) + int(balance) < limit:
        print(f'Транзакция {to_do}: "{tran_name[to_do]}" на сумму {tran_sum[to_do]} руб. успешно применена.')
        tran_count[to_do] -= 1
        balance += int(tran_sum[to_do])
        if int(tran_count[to_do]) > 0:
            print(f'Осталось {tran_count[to_do]} пополнений.')
        else:
            print('Вы внесли последний платеж. Поздравляем вас!')
    else:
        print(f'Транзакция {to_do}: {tran_name[to_do]} на сумму {tran_sum[to_do]} руб. не может '
              f'быть применена (превышен лимит).')
    return balance


def tran_data_open(num, body, fun):
    name = [num]
    if int(transaction_data[0]) == num:
        for i in range(len(transaction_data) - 2):
            name.append(fun(transaction_data[i + 1]))
        return name
    else:
        return body


def chek_pasw():
    while True:
        for a in range(3):
            passw3 = str(input("Введите пожалуйста пароль: "))
            if passw3 == passw:
                print()
                print(f"Добрый день, {name}. Вы успешно вощли в систему")
                return 1
            else:
                print("Пароль не верный. Осталось попыток: " + str(2 - a))
                if a == 2:
                    print("Ваши попытки закончились\n")
                    return 2


def generator(list_g, count=0):
    for i in range(len(list_g) - count):
        yield i


now = datetime.datetime.now()
print("Добро пожаловать в наш Банк")
while True:
    print("Вы можете:\n1. Создать аккаунт.\n2. Войти в личный кабинет.\n3. Выйти из программы.\n")
    op = int(input("Выберите операцию: "))
    if op == 1:
        print("Заполните пожалуйста данные для регистрации нового аккаунта.")
        name = str(input("Ваше ФИО: "))
        year = int(input("Год рождения: "))
        print(f"Создан Аккаунт: {name} ({now.year - year} лет)")
        while True:
            passw = str(input("Введите пожалуйста пароль: "))
            passw2 = str(input("Повторите пароль: "))
            if passw == passw2:
                break
            else:
                print("Пароли не совпадают. Попробуйте заново.")
        limit = int(input("Введите максимальную сумму, которая должна быть на счету: "))
        print(f"Максимальная сумма {limit} установлена.\n")
        with open("data-man.txt", "w", encoding='utf-8') as fout:
            fout.write(f'{name},{year},{passw},{limit},0')
        print("Ваш Аккаунт Успешно зарегистрирован!")
        print()
    elif op == 2:
        try:
            with open("data-man.txt", "r", encoding='utf-8') as fin:
                for line in fin:
                    men_data_input = line.split(",")
                    name = men_data_input[0]
                    year = int(men_data_input[1])
                    passw = men_data_input[2]
                    limit = int(men_data_input[3])
                    balance = int(men_data_input[4])
            del fin, men_data_input
            input_chek = chek_pasw()
        except:
            print(f"Нужно сначало зарегистрироваться.\n")
            continue
        if input_chek == 1:
            tran_name = [1]
            tran_sum = [2]
            tran_count = [3]
            while True:
                solution = int(input("Вы хотите востановить данные? (Да = 1 Нет = 0): "))
                if solution == 1:
                    try:
                        with open("data-transaction.txt", "r", encoding='utf-8') as fin:
                            for line in fin:
                                transaction_data = line.split(",")
                                tran_name = tran_data_open(1, tran_name, str)
                                tran_sum = tran_data_open(2, tran_sum, int)
                                tran_count = tran_data_open(3, tran_count, int)
                        del line, transaction_data, fin
                        break
                    except:
                        print(f"Данные отсутвуют.")
                        exit()
                elif solution == 0:
                    break
                else:
                    print(f"Неверный код операции.")
            del solution
            print()
            while True:
                print("Вы можете:\n"
                      "1. Положить деньги на счёт.\n"
                      "2. Изменить лимит.\n"
                      "3. Установить ожидаемое пополнение.\n"
                      "4. Применить транзакции.\n"
                      "5. Отфильтровать транзакции.\n"
                      "6. Показать статиститку по ожидаемым попролнениям.\n"
                      "7. Снять деньги.\n"
                      "8. Вывести баланс на экран.\n"
                      "9. Выйти из личного кабинета.\n")
                op2 = int(input("Выберите операцию: "))
                if op2 == 1:
                    while True:
                        balance_plus = int(input("Введите сумму пополнения: "))
                        if balance_plus == 0:
                            print("Ваш счёт не был изменён.\n")
                            break
                        if balance_plus < 0:
                            print("Сумма не должна быть отрицательной.")
                        if balance_plus + balance > limit:
                            print("Сумма превышает лимит. Пополнение невозможно.")
                        else:
                            balance += balance_plus
                            data_user_out()
                            print("Счёт успешно пополнен!\n")
                            break
                elif op2 == 2:
                    print(f"Ваш нынешний лимит: {limit} руб.")
                    limit = int(input("Введите максимальную сумму, которая должна быть на счету: "))
                    print(f"Максимальная сумма {limit} установлена.\n")
                    data_user_out()
                elif op2 == 3:
                    new_name = str(input("Выберите назначение новой транзакции: "))
                    new_sum = int(input("Выберите сумму пополнения: "))
                    new_count = int(input("Выберите количество пополнений: "))
                    tran_name.append(str(new_name))
                    tran_sum.append(int(new_sum))
                    tran_count.append(int(new_count))
                    tran_write()
                    print(f'Транзакция "{new_name}" на сумму {new_sum} руб. сохранена. \n')
                elif op2 == 4:
                    print("Ваши Ожидаемые пополнения:")
                    for y in range(len(tran_name) - 1):
                        print(f'Транзакция {y + 1}: "{tran_name[y + 1]}" на сумму {tran_sum[y + 1]} руб.')
                    print()
                    to_do = int(input('Выберите номер транзакции которую хотите применить. \n'
                                      'Чтобы выбрать сразу все нажмите "0".\nЧтобы выйти нажмите "99".\n'
                                      'Ваш выбор:'))
                    if to_do == 99:
                        print()
                        continue
                    if 0 < to_do <= (len(tran_name) - 1):
                        balance = tran_pay(balance)
                    if to_do == 0:
                        for to_do in range(len(tran_name) - 1):
                            to_do += 1
                            balance = tran_pay(balance)
                    for d in reversed(range(len(tran_count))):
                        if tran_count[d] == 0:
                            del tran_name[int(d)]
                            del tran_sum[int(d)]
                            del tran_count[int(d)]
                    data_user_out()
                    tran_write()
                    print()
                elif op2 == 5:
                    min_trans = int(input("Введите минимальную сумму которая должна быть в платежах: "))
                    for i in generator(tran_sum, 1):
                        if tran_sum[i + 1] >= min_trans:
                            print(f'Транзакция {i + 1}: "{tran_name[i + 1]}" на сумму {tran_sum[i + 1]} руб.')
                    print()
                elif op2 == 6:
                    print("Ваши Ожидаемые пополнения:")
                    for y in range(len(tran_name) - 1):
                        print(f'"{tran_name[y + 1]}" на сумму {tran_sum[y + 1]} руб. Осталось: '
                              f'{tran_count[y + 1]} платеж(а).')
                    print()
                elif op2 == 7:
                    while True:
                        take = int(input("Введите сумму которую хотите снять: "))
                        if take == 0:
                            print("Ваш счёт не был изменён.\n")
                            break
                        if (balance - take) < 0:
                            print("На вашем счёте не достаточно средств.")
                        else:
                            balance -= take
                            print("Операция успешно завершена.")
                            print(f"Ваш баланс: {balance} руб.\n")
                            break
                    data_user_out()
                elif op2 == 8:
                    print(f"Ваш баланс: {balance} руб.\n")
                elif op2 == 9:
                    break
                else:
                    print("Неверный код операции.")
                    print()
            break
    elif op == 3:
        print("Спасибо за пользование нашей программой, до свидания!")
        break
    else:
        print("Неверный код операции.")
        print()
