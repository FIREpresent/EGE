import sys
from sys import setrecursionlimit
setrecursionlimit(10_000)
def f(n):
    if n == 0:
        return 1
    elif n > 0 and n % 2 != 0:
        return 1 + f(n - 1)
    return f(n/2)
count = 0
for n in range(1500000):
    if f(n) == 4:
        count += 1
        print(f(n), '---------------')
    else:
        print(f(n))

print(count)
