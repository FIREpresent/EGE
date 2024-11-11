from itertools import *

count = 0
for a1 in product('XYZ', repeat=1):
    for a2, a3, a4 in product('ABCD', repeat=3):
        count += 1

print(count)