from itertools import *
i = 0
for a in product('КЛРТ', repeat = 4):
    i += 1
    if i == 67:
        print(i, a)
