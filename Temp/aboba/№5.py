
from itertools import *
i = 0
count = 0
s = 'НОБЕЛИЙ'
for var in permutations(s, r=7):
    i += 1
    s = ''.join(var)
    if s[0] != 'Й':
        if 'ИЙО' not in s:
            count += 1

print(count)