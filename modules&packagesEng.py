import os
import random as r
from fake_math import divide as fake_divide
from true_math import divide as true_divide

os.system('COLOR B')

LEFT = 1
RIGHT = 100

result1 = fake_divide(
    r.randint(LEFT, RIGHT),
    r.randint(LEFT, RIGHT))
result2 = fake_divide(
    r.randint(LEFT, RIGHT), 0)
result3 = true_divide(
    r.randint(LEFT, RIGHT),
    r.randint(LEFT, RIGHT))
result4 = true_divide(
    r.randint(LEFT, RIGHT), 0)

print('\n', result1, sep='')
print(result2)
print(result3)
print(result4, '\n')

try:
    os.system('PAUSE')
    os.system('CLS')
except:
    os.system('CLS')
