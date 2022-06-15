import random


def comm(z, x):
    print(z * x)


counter = 0
counter_win = 0
levels = {1: 10, 2: 20, 3: 30}
winners = []

while True:
    counter_win += 1
    number = random.randint(1, 100)
    print(number)
    print('Компьютер загадал число от 1 до 100')
    print('Попробуйте угадать загадоное компьютером число!')
    name = input('Введите Имя участника: ')
    print('Выберите уровень сложности: где 1 сложно, 2 нормально, 3 легко')
    tip = int(input(f'И так {name} Вы выбрали уровень: '))
    user_number = None
    print(f'{name} попробуйте угадать, загаданное компьютером число с {levels[tip]} попыток')
    max_counter = levels[tip]

    while number != user_number:
        if counter > max_counter:
            print(f'{name} Вы проиграли, у Вас закончались все {levels[tip]} попыток :(( ')
            print('Погнали по новой! ')
            break
        counter += 1
        user_number = int(input(f'Попытка №{counter} попробуйте отгадать загаданное число: '))
        if number < user_number:
            print('Нужно число меньше')
        elif number > user_number:
            print('Нужно число больше')
    else:

        print(f'Бинго - Вам удалось отгодать загадонное компьютером число c {counter}-й попытки')
        winners.append(f'{name} использовал {counter} попыток на {tip} уровне сложности')

        print('Таблица победителей!')
        for i in winners:
            print(i)

    print('Для выходы из игры нажмите "Q" или любую другую для продолжения :)) ')
    attempt = input('Ждем Вашего решения: ')

    if attempt == "Q":
        break
    else:
        print('Удачи В новой попытки !')
        print('Игра начинается !')
        counter = 0
