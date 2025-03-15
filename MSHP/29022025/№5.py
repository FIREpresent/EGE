from itertools import *

count = 0
st = sorted("СВЯТОСЛАВ")
for _ in product(st, repeat=7):
    s = ''.join(_)
    s = s.replace('Я', 'X').replace('О', 'X').replace('А', 'X')
    if 2*s.count('X') > len(s):
        count += 1
print(count)
