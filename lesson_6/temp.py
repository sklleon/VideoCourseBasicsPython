winners = {}
count =0
while True:
    count +=1
    name = input('Введите имя: ')
    win = input('Введите введите кол-во попыток: ')
    winners['№'] = count
    winners['Участник'] = name
    winners['Попытки'] = win
    print(winners)


    if count == 2:
        break

print(winners)