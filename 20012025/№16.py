import sys
from functools import lru_cache

sys.setrecursionlimit(5_000)
# @lru_cache(None)
def f(n):
  if n < 5:
    return n
  else:
    return 2*n*f(n-4)

print((f(13766) - 9*f(13762))/f(13758))