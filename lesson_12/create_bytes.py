# Создание обычной строки
s = 'Hello world'
print(type(s))

# Создание строки байт
sb = b'Hello world'
print(type(sb))
print(sb)

#Работа с индексом
print(s[1])
print(sb[1])

#Срезы
print(s[1:3])
print(sb[1:3])

#Перебор строки байт в цикле
for item in sb:
    print(item)