import sys
from functools import lru_cache

sys.setrecursionlimit(5_000)


@lru_cache(None)
def f(n):
    if n < 9:
        return n
    return f(n % 9) + f(n // 9)


count = 0
for i in range(4 * 6 ** 20, 5 * 6 ** 20):
    if f(i) == 121:
        count += 1
