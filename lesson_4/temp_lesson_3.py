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
print('Привет мой друг - '+frends)
print('Привет мой друг - %a '%(frends))

#------------------------------->
top5 = 'Первые 5 мест на соревнованиях: 1. Иванов 2. Петров 3. Сидоров 4. Орлов 5.Соколов'
start = top5.find('1')
end = top5.find('4')
top3 = top5[start:end]
rezultat = 'Поздравляем наших победителей {} с успехом! '.format(top3.upper())
print(rezultat)
#------------------------------->
friends = ['Иванов','Петров','Сидоров','Орлов','Соколов']
print(friends)
print(len(friends)) # считаем кол-во элементов
friends.append('Тони') # Добавляем элемент
print(friends)
print(friends.pop()) # удаляем последний элемент
# friends.clear() # полностью очищаем список
friends.remove('Петров') # удалить конкретный элемент
del friends[1] # удалить конкретный элемент
print(friends)
#------------------------------->
hero = 'Superman'
if hero.find('man') != -1:
    print('Yes')
if 'per' in hero:
    print('Да')
if 'Соколов' in friends:
    print('Yes')
#------------------------------->
