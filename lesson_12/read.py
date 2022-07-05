f = open('first.txt', 'r')

# print(f.read()) #Читать весь файл целиком

# for line in f: # Читать файл по строчно
#     print(line)

# for line in f: # Читать файл по строчно c заменой символа (\n)
#     print(line.replace('\n',''))

# читать файл и сохронять результат в список
print(f.readlines())

