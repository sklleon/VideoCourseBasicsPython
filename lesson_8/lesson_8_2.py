# Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.


def get_max(a, b, c):
    rezult = max([a, b, c])
    return rezult

a = input('Введите число a: ')
b = input('Введите число b: ')
c = input('Введите число c: ')
print(get_max(a,b,c))
