from itertools import *

count = 0
i = 0
for var in product(sorted('ПАРУС'), repeat=5):
    i += 1
    num = ''.join(var)
    if num[0] == 'У' and 'АА' not in num:
        print(i)
        break

print(count)
