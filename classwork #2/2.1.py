from itertools import *

v = sorted('В,Е,Р,О,Н,И,К,А'.split(','))
i = 0
for a in product(v, repeat = 3):
    i += 1
    if 'А' not in a:
        print(i, a)
        break