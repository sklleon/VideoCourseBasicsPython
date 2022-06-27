# Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр - armor = 1.2 (величина брони персонажа)
# Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно, у вас должно быть 2 функции:
# Наносит урон. Это улучшенная версия функции из задачи 3.
# Вычисляет урон по отношению к броне.
#
# Примечание. Функция номер 2 используется внутри функции номер 1 для вычисления урона и вычитания его из здоровья персонажа.

player_name = input('Введите имя игрока: ')
player = {'name': player_name, 'health': 100, 'damage': 50, 'armor': 1.2}

enemy_name = input('Введите имя врага: ')
enamy = {'name': enemy_name, 'health': 50, 'damage': 30, 'armor': 1}


def attack(unit, target):
    damage = get_damage(unit['damage'], target['armor'])
    target['health'] -= damage


def get_damage(damage, armor):
    return damage / armor


attack(player, enamy)
print(enamy)

attack(enamy, player)
print(player)
