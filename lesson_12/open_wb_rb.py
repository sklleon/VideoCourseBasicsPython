# Открываем файл для записи байтов
with open('bates.txt', 'wb') as f:
    f.write(b'Some bytes\n')
    f.write('Some bytes')
    pass

with open('bates.txt', 'rb') as f:
    print(f.read())

# Открываем файл в текстовом режиме в указанием кодировки
with open('bates.txt', 'r', encoding='utf-8') as f:
    pass
