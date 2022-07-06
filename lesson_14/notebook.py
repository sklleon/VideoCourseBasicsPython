is_has_name = True  # False
name = 'Max' if is_has_name else 'Leo'
print(name)

is_one = False
number = 1 if is_one else 2
print(number)

is_russian = True
print('Привет' if is_russian else 'Hello')

#  example
# 1. Создать список из случайных чисел от 1 до 100
import random
numbers = [random.randint(1,100) for i in range(10)]
print(numbers)

# 2. Создать список квадратов числе
numbers = [1, 2, 3, -4]
numbers = [number**2 for number in numbers]
print(numbers)

# 3. Создать список Имен на букву 'A'
name = ['Андрей', 'Алексей', 'Руслан', 'Максим', 'Артем', 'Артур']
