import sys
from functools import lru_cache

sys.setrecursionlimit(10_000)
@lru_cache(None)
def F(n):
    if n < 10:
        return n
    return F(n % 10) + F(n // 10)

