import os
import math
import random as rd

print(math.pi)
print(math.sin(38))

# 1.Загадайте случайное число от 1 до 10
print(rd.randint(1, 10))

# 2.Выберать победителя лотереи из списка
players = ['Max', 'Leo', 'Juliya', 'Robert', 'lara', 'Tim','Jira','Simona']
print(rd.choice(players))

# 3.Выбрать трех победителей из списка
print(rd.sample(players, 3))
# 4. Перемешать карты в стопке (списка) cards
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'V', 'D', 'K', 'T', 'J']
print(cards)
rd.shuffle(cards)
print(cards)

print(rd.random())
