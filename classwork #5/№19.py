import sys
sys.setrecursionlimit(10_000)

def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2:
        if n % 2 == 0:
            return int((4 * n - f(n - 3)) / 8)
        return int((4 * n - f(n - 1) + f(n - 2)) / 8)

print(f(52)-f(38))