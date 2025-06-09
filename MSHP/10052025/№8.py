from itertools import *
s = 'ГЕРАСИМ'
count = 0
for p in permutations(sorted(s), r=7):
    count += 1
    v = ''.join(p)
    if count == 1899:
        print(v)
print(count)