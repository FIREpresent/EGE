import sys
from functools import lru_cache

sys.setrecursionlimit(5_000)
# @lru_cache(None)
def f(n):
  if n == 0:
    return 0
  elif n > 0 and n%3 == 0:
      return f(n/3)
  elif n%3 > 0:
      return n%3 + f(n - n%3)

for i in range(100_000):
    if f(i) == 11:
        print(i)
        break