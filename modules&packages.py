# Python 3.8.1

# os - библиотека для работы с консолью
# random - библиотека для работы со случайными данными
# fake_math - библиотека для работы с математическими функциями
# true_math - библиотека для работы с функциями высшей математики

import os
import random as r
from fake_math import divide as fake_divide
from true_math import divide as true_divide

# Зададим цвет шрифта консоли
os.system('COLOR B')

LEFT = 1 # LEFT - левая граница
RIGHT = 100 # RIGHT - правая граница

result1 = fake_divide(
    r.randint(LEFT, RIGHT),
    r.randint(LEFT, RIGHT))
# result1 - результат деления
result2 = fake_divide(
    r.randint(LEFT, RIGHT), 0)
# result2 - результат деления на нуль
result3 = true_divide(
    r.randint(LEFT, RIGHT),
    r.randint(LEFT, RIGHT))
# result3 - результат деления
result4 = true_divide(
    r.randint(LEFT, RIGHT), 0)
# result4 - результат деления на нуль

print('\n', result1, sep='')
print(result2)
print(result3)
print(result4, '\n')

try:
    os.system('PAUSE')
    os.system('CLS')
except:
    os.system('CLS')
