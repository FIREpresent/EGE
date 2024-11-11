from itertools import *
count = 0
a = 'ГРСМ'
b = 'ЕАИ'

for p in permutations('ГЕРАСИМ'):
    flag = True
    for i in range(len(p) - 1):
        if (p[i] in a and p[i + 1] in a) or (p[i] in b and p[i + 1] in b):
            flag = False
    if flag == True:
        count += 1
print(count)
