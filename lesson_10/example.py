'''
В зависимости от параметра вызывать различные функции скрипта
параметр ping - функция выводит - "pong"
2 параметр  name <Имя> - функция приветствия
параметр List показать содержимое текущей деректории
'''
import sys, os


def ping():
    print('pong')


def hello(name):
    print(f'Привет {name}')


def get_info():
    for li in os.listdir():
        print(li)


command = sys.argv[1]

if command == 'ping':
    ping()
elif command == 'list':
    get_info()
elif command == 'name':
    name = sys.argv[2]
    hello(name)
