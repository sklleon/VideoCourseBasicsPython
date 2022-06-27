player_name = input('Введите имя игрока: ')
player = {'name': player_name, 'health': 100, 'damage': 50}

enemy_name = input('Введите имя врага: ')
enamy = {'name': enemy_name, 'health': 50, 'damage': 30}

def attack(unit, target):
    target['health'] -= unit['damage']

attack(player,enamy)
print(enamy)

attack(enamy,player)
print(player)