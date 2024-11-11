from itertools import *

v = sorted('К,О,М,П,Ь,Т,Е,Р'.split(','))
i = 0
for a in product(v, repeat = 5):
    i += 1
    if ('К' not in a) and (a.count('Р') == 2):
        print(i, a)
        break