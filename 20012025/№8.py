
from itertools import *
i = 0
count = 0
for var in product(sorted('ЯНВАРЬ'), repeat = 5):
    i += 1
    s = ''.join(var)
    if (s[0] != 'Я') and (s.count('Ь') <= 1) and ('ЯЯ' not in s):
      count += 1
      print(i, s)

# print(count)