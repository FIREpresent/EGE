from itertools import *

from itertools import *
k = 0
c1 = 'ИОА'
c2 = 'МТРФН'
for a in permutations('МИТРОФАН', 6):
    s = ''.join(a)
    k1 = 0
    k2 = 0

    k1 += (s[0] in c1)
    k2 += (s[0] in c2)

    for i in range(len(s)-1):
        k1 += (s[i+1] in c1)
        k2 += (s[i+1] in c2)
        if s[i] in c1 and s[i+1] in c1:
            break
    else:
        if k2 > k1:
            k += 1
print(k)