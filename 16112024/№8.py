from itertools import *

alph = '0123456789ABCDEF'

count = 0
for i in product(alph, repeat=8):
    if i[0] != '0':
        if i.count('0') == 2 and (i.count('A') + i.count('B') + i.count('C') + i.count('D') + i.count('E') + i.count('F')) <= 4:
            count += 1
print(count)

