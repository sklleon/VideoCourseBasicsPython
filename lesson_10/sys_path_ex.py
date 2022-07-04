# Мы можем импортировать
import math
# но не можем импортировать на модуль например на диске c:
# как питон находит модули ?
import sys
print(sys.path)
print(type(sys.path))

for i in sys.path:
    print(i)

sys.path.append('I:')
import myPython