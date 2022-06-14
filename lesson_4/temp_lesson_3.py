def comm(z, x):
    print(z * x)


frends = 'leonidos'

print(len(frends))
print(frends[2:-2])
print(frends.lower())
print(frends.upper())
print(frends.isdigit())
print(frends.split('o'))
print(frends.find('o'))
# help(str)
print(f'Привет мой друг - {frends}')
print('Привет мой друг - {}'.format(frends))
print('Привет мой друг - ' + frends)
print('Привет мой друг - %a ' % (frends))

# ------------------------------->
top5 = 'Первые 5 мест на соревнованиях: 1. Иванов 2. Петров 3. Сидоров 4. Орлов 5.Соколов'
start = top5.find('1')
end = top5.find('4')
top3 = top5[start:end]
rezultat = 'Поздравляем наших победителей {} с успехом! '.format(top3.upper())
print(rezultat)
# ------------------------------->
friends = ['Иванов', 'Петров', 'Сидоров', 'Орлов', 'Соколов']
print(friends)
print(len(friends))  # считаем кол-во элементов
friends.append('Тони')  # Добавляем элемент
print(friends)
print(friends.pop())  # удаляем последний элемент
# friends.clear() # полностью очищаем список
friends.remove('Петров')  # удалить конкретный элемент
del friends[1]  # удалить конкретный элемент
print(friends)
# ------------------------------->
hero = 'Superman'
if hero.find('man') != -1:
    print('Yes')
if 'per' in hero:
    print('Да')
if 'Соколов' in friends:
    print('Yes')
# ------------------------------->

comm('=+', 50)
friend_name = 'max'
friends = ['vax', 'argo', 'cocho', 'koko', 'max', 'vito', 'sony']
roles = ('admin', 'guest', 'user')

if 'max' in friends:
    print('У меня есть этот друг')
if 'm' in friend_name:
    print('Буква (М) есть в его имени друга')

i = 0
while i < len(friends):
    frend = friends[i]
    print(frend)
    i += 1
comm('=', 30)
for friend in friends:  # Перебор список
    print(friend)
comm('=', 30)
for letter in frend:  # Перебор строки
    print(letter)
comm('=', 30)
for role in roles:  # Переборка кортежа
    print(role)

comm('=+', 50)
numbers = range(10)
print(list(numbers))
print(type(numbers))

comm('=', 30)
winners = ['max', 'leo', 'juliay']

# простой перебор
for win in winners:
    print(win)

# используем range
for i in range(len(winners)):
    print(i)
    print(winners[i])
    print(f'{i + 1}) {winners[i]}')
comm('=+', 50)

friendnd = {
    'name': 'max',
    'age': '18'
}
print(type(friendnd))
print(friendnd)
print(friendnd['age'])  # Добавляем элемент в словарь
friendnd['car'] = 'BMW'
print(friendnd)
# del friendnd['car']  # удаляем элемент в словаре
# print(friendnd)
if 'name' in friendnd:
    print('Да в словаре есть реквизит "name".')

comm('-', 25)  # по ключам
for key in friendnd.keys():
    print(key)
    print(friendnd[key])
for key in friendnd:
    print(key)
    print(friendnd[key])

comm('-', 25)  # по значениеям
for val in friendnd.values():
    print(val)

comm('-', 25)  # пары ключ и значения
for item in friendnd.items():
    print(item)

for key, val in friendnd.items():
    print(f'{key} {val}')

comm('=+', 50)  # Множество
cities = ['Moscow', 'New Yourk', 'Las Vegas', 'Moscow', 'Paris', 'Paris']
print(type(cities))
print(cities)
cities = set(cities)
print(type(cities))
print(cities)
cities = {'Moscow', 'New Yourk', 'Las Vegas', 'Paris'}
print(cities)

comm('-', 25)  # Действия со множеством
cities.add('Burma')
print(cities)
cities.remove('Moscow')
print(cities)
print(len(cities))
print('Paris' in cities)
print('Uzbekistan' in cities)
for city in cities:
    print(city)

comm('-', 25)  # операции со множеством
# Семейнаяара собирается в отпуск
# каждый из супругов собирает в поездку вещи
# макс взял эти вещи
max_things = {'Телефон', 'Бритва', 'Шорты', 'Рубашка', 'Майка'}
# Катя вот эти
kate_things = {'Телефон', 'Шорты', 'Зонтик', 'Крем', 'Помада', 'Фен', 'купальник'}
# Какие вещи взяли супруги ?
print(max_things | kate_things)
# Какие вещи повторяються ?
print(max_things & kate_things)
# Какие вещи взял макс но не взяла катя ?
print(max_things - kate_things)
# Какие вещи взяла катя но не взял макс ?
print(kate_things - max_things)
