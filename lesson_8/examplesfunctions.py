def comm(a='-', b=100):
    return (a * b)


def comment(c, v, *args):
    print(c + v, args)


def comments(**kwargs):
    for x, y in kwargs.items():
        print(x, y)


numbers = []

# for i in range(3):
#     number = int(input('Введите число: '))
#     numbers.append(number)
#
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

print(comm('=-', 70))
comment(10, 20, 30, 40, 50)
print(comm())
comments(lm=10, mm=20, j=50, bm=40, hm=80, tu=90, ym=10)
print(comm())


# def my_filter(numbers):
#     result = []
#     for number in numbers:
#         if number % 2 == 0:
#             result.append(number)
#     return result

def my_filter(numbers, function):
    result = []
    for number in numbers:
        if function(number):
            result.append(number)
    return result


def is_even(numbers):
    return numbers % 2 == 0


def is_not_even(numbers):
    return numbers % 2 != 0


def big_4(numbers):
    return numbers > 4


numbers = [1, 2, 0, 2, 4, 5, 7, 8, 45, 35]
print(my_filter(numbers, is_even))
print(my_filter(numbers, is_not_even))
print(my_filter(numbers, big_4))

print(comm())

print(my_filter(numbers, lambda numbers: numbers % 2 == 0))
print(my_filter(numbers, lambda numbers: numbers % 2 != 0))
print(my_filter(numbers, lambda numbers: numbers > 4))

print(comm())

print(sorted(numbers))
print(sorted(numbers, reverse=True))
name = ['leo', 'Max', 'Rex', 'Wolf', 'Boss', 'Luliay', 'Stas', 'Rik', 'Gas', 'Stev', 'Svetlana', 'Roberto', 'Aleks']
print(sorted(name))

sities = [('Moskow', 700000, 100), ('USA', 5000, 200), ('China', 100000, 300)]
print(sorted(sities))


def by_count(city):
    return city[2]


print(sorted(sities, key=by_count))


def si_count(city):
    return city[1]


print(sorted(sities, key=si_count))
print(sorted(sities, key=si_count, reverse=True))
