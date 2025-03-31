from itertools import *
s = 'ОЛЬГА'
count = 0
for p in permutations(s, r=5):
    v = ''.join(p)
    if v[0] != 'Ь' and 'ОЬ' not in v and 'АЬ' not in v:
        count += 1
print(count)