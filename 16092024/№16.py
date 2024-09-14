import sys
sys.setrecursionlimit(10**6)

def func(n):
    if n < 11:
        return n
    elif n >= 11:
        return n + func(n - 1)

print(func(2024) - func(2021))