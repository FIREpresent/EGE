from itertools import *
alph = '0123456'
counter = 0
for p in product(alph, repeat=5):
    s = ''.join(p)
    if s[0] != '0':
        if int(s[0]) % 2 == 0 and s[-1] != 2 and s[-1] != 3 and s.count('1') >= 2:
            counter += 1
print(counter)