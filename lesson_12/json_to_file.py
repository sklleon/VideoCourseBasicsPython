import json

friends = [{'name': 'Leo', 'age': '42', 'phone': ['89005456565', '89006680808']},
           {'name': 'Max', 'age': '18'}]

print(type(friends))

# Открываем файл
with open('friends.json', 'w') as f:
    # Преобразуем список друзей в Json  и сохроняем в файл
    json_friends = json.dump(friends, f)

# Обратно из файла в объект
with open('friends.json', 'r') as f:
    friends = json.load(f)

print(friends)
print(type(friends))
