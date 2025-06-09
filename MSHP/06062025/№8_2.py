from itertools import *
alph = 'МАНГУСТ'
counter = 0
for p in product(alph, repeat=6):
    s = ''.join(p)
    if s[0] != 'А' and s.count('У') >= 1 and s.count('М') == 2:
        counter += 1
print(counter)