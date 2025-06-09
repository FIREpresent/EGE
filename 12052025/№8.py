from itertools import *

s = 'ДГИАШЭ'
count = 0
for p in product(s, repeat = 5):
    t = ''.join(p)
    t = t.replace('И', 'Y').replace('А', 'Y').replace('Э', 'Y')
    t = t.replace('Д', 'X').replace('Г', 'X').replace('Ш', 'X')
    if t[0] != 'Y' and t[-1] != 'X':
        count += 1

print(count)