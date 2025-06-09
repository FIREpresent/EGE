from itertools import *
alph = '0123456789QWERTYUIOPASDFGHJKLZXCVBNM'
alph = sorted(alph)[:13]
counter = 0
for p in permutations(alph, r=7):
    s = ''.join(p)
    for i in range(13):
        if i % 2 != 0:
            s = s.replace(alph[i], 'X')
    if 'XB' not in s and 'BX' not in s and 'XBX' not in s:
        counter += 1

print(counter)