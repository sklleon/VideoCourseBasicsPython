person = {'name': 'Max', 'phones': ['123', '231', '223']}

# открываем файл
with open('person.dat','wb') as f:
    # Запишим объект в файл построчно,
    # сначала возмем имя
    name = person['name']
    # Добавим перенос строки и переведем в байты
    f.write(f'{name}\n'.encode('utf-8'))
    # потом телефон
    phones = person['phones']
    for phone in phones:
        f.write(f'{phone}\n' .encode('utf-8'))
print('Объект записан')
