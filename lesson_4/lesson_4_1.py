# Даны два произвольные списка. Удалите из первого списка элементы присутствующие во втором списке.
#     Примечание. Списки создайте вручную, например так:
# my_list_1 = [2, 5, 8, 2, 12, 12, 4]
# my_list_2 = [2, 7, 12, 3]
print('1.------------------------->')
# Вариант 1
my_list_1 = [2, 5, 8, 2, 20, 5, 6, 7, 9, 0, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]
full_list = set(my_list_1) - set(my_list_2)
print(list(full_list))
print('2.------------------------->')
# Вариант 2
for number in my_list_1:
    if number in my_list_2:
        print(number)
        my_list_1.remove(number)
print(my_list_1)
print('3.------------------------->')
my_list_1 = [2, 5, 8, 2, 20, 5, 6, 7, 9, 0, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]

# Вариант 3 - правельный
for number in my_list_1[:]:
    if number in my_list_2:
        print(number)
        my_list_1.remove(number)
print(my_list_1)
