word1 = 'Благодарю'
result1 = []

for i in range(len(word1)):
    if i % 2 != 0:
        letter = word1[i].lower()
    else:
        letter = word1[i].upper()
    result1.append(letter)
result1 = ''.join(result1)
print(result1)

word = 'Слово'
result = []

for i in range(len(word)):
    letter = word[i].lower() if i % 2 == 0 else word[i].upper()
    result.append(letter)
result = ''.join(result)
print(result)
