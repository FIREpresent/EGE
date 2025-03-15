from itertools import *

count = 0

for var in product(sorted('АНДРЕЙ'), repeat=6):
    num = ''.join(var)
    if num.count('А') >= 1 and num.count('Й') <= 1:
        count += 1

print(count)
