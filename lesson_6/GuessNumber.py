import random


def comm(z, x):
    print(z * x)


counter = 0
counter_win = 0
winners = {}

while True:
    counter_win += 1
    number = random.randint(1, 100)
    print('Компьютер загадал число от 1 до 100')
    print('Попробуйте угадать загадоное им число!')

    name = input('Введите Ваше Имя: ')

    while True:
        counter += 1
        print(f'{name} попробуйте угадать, загаданное число с минимальным количеством попыток')
        user_number = int(input(f'Попытка №{counter} Введите Ваше число: '))
        if number == user_number:
            print(f'Бинго - Вам удалось отгодать число c {counter}-й попытки')
            break
        elif number < user_number:
            print('Нужно число меньше')
        else:
            print('Нужно число больше')

    winners['name'] = name
    winners['count'] = counter

    print('Таблица победителей!')
    for name, count in winners.items():
        print(f'Участник {name} угадал с {count} попытки')

    print('Для выходы из игры нажмите "Q" ')
    print('Или любую другую для продолжения :)) ')

    attempt = input('Ждем Вашего решения: ')

    if attempt == "Q":
        break
    else:
        print('Удачи В новой попытки !')
        print('Игра начинается !')

if counter_win == 1:
    print(f'Поздравляю Вас {name} с {counter_win}-й победой')
else:
    print(f'Поздравляю Вас {name} с {counter_win}-я победами')
