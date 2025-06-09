import sys
from sys import setrecursionlimit
setrecursionlimit(10_000)
def f(n):
    if n < 3:
        return 1
    elif n > 2:
        if n % 2 == 0:
            return f(n - 2) - f(n - 1)
        elif n % 2 != 0:
            return f(n - 2) - f(n - 3)

print(f(50))
