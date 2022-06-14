print(' -= СОРЕВНОВАНИЯ ПО PYTHON =- ')
count = int(input('Введите кол-во участников учавствующих в соревнованиях по Python: '))
listing = []
i = count

while i > 0:
    name = input(f' Кто занял {i} место?: ')
    listing.append(name)
    i -= 1
print(f' В соревновании по Python учавствовали: {sorted(listing)}')
listing.reverse()
rezultat = listing[:3]
print(f'Поздравляем тройку побидителей: {rezultat}')
