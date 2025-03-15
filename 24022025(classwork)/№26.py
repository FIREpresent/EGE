import sys

sys.setrecursionlimit(10_000)


def F(n):
    if n == 1:
        return n
    elif n > 1:
        return n - 1 + F(n - 1)


print(F(2024) - F(2022))
