from itertools import *
s = '123456789AB'
for x, y in product(s, repeat=2):
    x, y = ''.join(x), ''.join(y)
    if (int(f'{y}AA{x}', 12) + int(f'{x}02{y}', 14)) % 80 == 0:
        print((int(f'{y}AA{x}', 12) + int(f'{x}02{y}', 14)) // 80)
        break
