import sys
from sys import setrecursionlimit

setrecursionlimit(10000)
def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2:
        return f(n-2) * (n - 1)

print(f(8))