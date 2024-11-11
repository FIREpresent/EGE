from itertools import *

v = sorted('А,Л,Г,О,Р,И,Т,М'.split(','))
print(v)
i = 0
for a in product(v, repeat = 4):
    i += 1
    print(*a)
    if a[0:2] == ('И', 'Г'):
        print(i, a)
        break