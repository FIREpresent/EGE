from itertools import *


count = 0
for i in range(1, 11):
    for x in permutations("0123456789", r=i):
        s = ''.join(x)
        if s[0] != '0' and int(s) % 5 == 0:
            count += 1

print(count)
