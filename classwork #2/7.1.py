from itertools import *

count = 0
for a1, a2, a3, a4, a5 in product('012345678', repeat=5):
    if int(a1) > int(a2) > int(a3) > int(a4) > int(a5):
        count += 1

print(count)