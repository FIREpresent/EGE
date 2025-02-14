
from itertools import *
i = 0
count = 0
s = '0123456'
for var in product(s, repeat = 4):
    i += 1
    s = ''.join(var)
    if s[0] != '0':
        if int(s[0]) > int(s[1]) > int(s[2]) > int(s[3]):
            count += 1

print(count)