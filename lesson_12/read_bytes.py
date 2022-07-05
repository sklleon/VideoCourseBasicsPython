# Открывает файл для записи байтов
with open('bytes.txt', 'wb') as f:
    str = 'Привет мир'
    f.write(str.encode('utf-8'))

# открываем файл в режиме чтения байтов
with open('bytes.txt', 'rb') as f:
    result = f.read()
    print(result)
    print(type(result))
    # декодируем для получения строки
    s = result.decode('utf-8')
    print(s)
