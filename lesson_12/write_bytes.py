# Открывает файл для записи байтов
with open('bytes.txt', 'wb') as f:
    f.write(b'Hello bytes')

# Читаем как текст
with open('bytes.txt', 'r', encoding='ascii') as f:
    print(f.read())

# открываем файл для записи байтов
with open('bytes.txt', 'wb') as f:
    str = 'Привет мир'
    f.write(str.encode('utf-8'))

# Читаем как текст с кодировкой utf-8
with open('bytes.txt','r', encoding='utf-8') as f:
    print(f.read())
