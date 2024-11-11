from itertools import *
count = 0
s = []
for p in permutations('МАТВЕЙ'):
    if (p[0] != 'Й') and ('АЕ' not in p[0]+p[1]+p[2]+p[3]+p[4]+p[5]):
        count += 1
        # print(str(list(p)))

print(count)