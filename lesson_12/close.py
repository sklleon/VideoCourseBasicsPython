f = open('first.txt', 'r')
for line in f:
    print(line.replace('\n', ''))

# Закрытие файла
f.close()

# Закрытие вариант 2
with open('first.txt', 'r') as f:
    for line in f:
        print(line.replace('\n', ''))

print('end')
