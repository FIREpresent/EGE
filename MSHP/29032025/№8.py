from itertools import *

count = 0
idx = 0
for var in product(sorted('ОЩХУ'), repeat=6):
    count += 1
    num = ''.join(var)
    if num[0:2] == 'ОО':
        idx = count

print(idx)
