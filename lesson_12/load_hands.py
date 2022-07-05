# Читаем объект из файла
# Откроем файл
with open('person.dat', 'rb') as f:
    # теперь нам надо знать как мы записоваем объект
    # Прочитаем файл в списке
    result = f.readlines()
# Теперь воссоздаем исходный объект
person = {}
# Первый элемент это имя
person['name'] = result[0].decode('utf-8').replace('\n', '')
# Далее идет телефон
phones = []
for bphone in result[1:]:
    phones.append(bphone.decode('utf-8').replace('\n', ''))
person['phones'] = phones
# Получили исходный объект. Это было достаточно тяжело))
# А что если он немного измениться ?
print(person)
