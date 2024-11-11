from itertools import *

alph = '0123'
count = 0
for i in product(alph, repeat=3):
    if i[0] != '0':
        if (int(i[0]) + int(i[-1])) > int(i[1]):
            count += 1
print(count)