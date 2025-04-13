from itertools import *
s = 'ВАЯЮЩИЙ'
count = 0
for p in product(s, repeat=4):
    v = ''.join(p)
    if v[0] != 'Й' and ('А' in v or 'Я' in v or 'Ю' in v or 'И' in v):
        count += 1
print(count)