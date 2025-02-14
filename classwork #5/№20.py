import sys

from charset_normalizer.md import lru_cache

sys.setrecursionlimit(10_000)
#
# @lru_cache()
def f(n):
    if n == 1:
        return 1
    elif n > 1:
        return n*f(n - 1)

print(f(2023)/f(2020))