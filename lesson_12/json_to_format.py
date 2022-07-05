import json

friends = [{'name': 'Leo', 'age': '42', 'phone': ['89005456565', '89006680808']},
           {'name': 'Max', 'age': '18'}]

print(type(friends))
# Преобразуем список в json
json_friends = json.dumps(friends)

# Печатаем что получилось

print(json_friends)
print(type(json_friends))

# обратно в json в объект
friends = json.loads(json_friends)
print(friends)
print(type(friends))

