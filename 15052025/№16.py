from functools import *
import sys
sys.setrecursionlimit(100_000)

def f(n):
    if n >= 1900:
        return n
    else:
        if n % 3 == 0:
            return n * f(n + 2) / 3
        return n * f(n + 1)

print(f(1875) / f(1880))