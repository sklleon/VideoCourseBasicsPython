import json

favourite_song = [{'name':'Вечная любовь','artist':'Агата Кристи'},
    {'name':'Angel','artist':'Massive Attack'},
    {'name':'Jamming','artist':'Bob Marlley'},
    {'name':'Группа крови на рукове','artist':'Виктор Цой'}]

with open('track.json', 'w', encoding='utf-8') as f:
    json.dump(favourite_song, f)
print('Выполнено')

print('Загружаем')
with open('track.json', 'r') as f:
    tracks = json.load(f)
print(tracks)