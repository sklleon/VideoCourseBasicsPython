import pickle

person = {'name': 'Max', 'phones': ['123', '231', '223']}

with open('person.dat', 'wb') as f:
    pickle.dump(person, f)
print('Объект записан')
