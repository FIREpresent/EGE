from itertools import *

count = 0

for var in product(sorted('ABCDX'), repeat=4):
    num = ''.join(var)
    if num.count('X') == 1:
        count += 1

print(count)
