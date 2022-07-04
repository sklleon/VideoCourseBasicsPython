import os

# Имя операционной системы
print(os.name)
# Текущая рабочая деректория
print(os.getcwd())
# Создать новый путь
new_path = os.path.join(os.getcwd(), 'new_f')
# создать папку по новому пути
os.mkdir(new_path)
