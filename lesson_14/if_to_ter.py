word = 'Слово'
result = []

for i in range(len(word)):
    if i % 2 == 0:
        letter = word[i].lower()
    else:
        letter = word[i].upper()
    result.append(letter)
result = ''.join(result)
print(result)

