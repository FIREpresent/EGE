import sys
from functools import lru_cache

sys.setrecursionlimit(10_000)
@lru_cache(None)
def f(n):
  if n == 0:
    return 0
  elif n > 0 and n % 2 == 0:
      return f(n/2)
  elif n % 2 != 0:
    return 1 + f(n - 1)

for n in range(1, 10000):
    if f(n) == 12:
        print(n)
        break