from itertools import *
s = 'ЗИМА'
count = 0
for p in product(s, repeat=5):
    v = ''.join(p)
    v = v.replace('З', 'X').replace('М', 'X')
    v = v.replace('И', 'Y').replace('А', 'Y')
    if v[0] == 'X' and v[-1] == 'Y':
        count += 1
print(count)