from itertools import *
a = 'ОА'
b = 'РСМХ'
v = set()
for p in permutations('РОСОМАХА'):
        flag = True
        for i in range(len(p) - 1):
            if (p[i] in a and p[i + 1] in a) or (p[i] in b and p[i + 1] in b):
                flag = False
        if flag == True:
            v.add(p)

print(len(v))