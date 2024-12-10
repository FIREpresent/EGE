import sys
from sys import setrecursionlimit

setrecursionlimit(10000)
def f(n):
    if n < 11:
        return 10
    else:
        return n + f(n - 1)

print(f(2024)-f(2022))