import sys
import functools
sys.setrecursionlimit(100_000)

@functools.lru_cache(None)
def f(n):
    if n < 3:
        return n
    return (n - 1) * f(n - 2)

print((f(2024)-f(2022))/f(2020))
#
# a = sum(i for i in range(0, 9))
# print(a)