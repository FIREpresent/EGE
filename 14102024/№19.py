import sys
sys.setrecursionlimit(10**6)
def f(n):
    if n < 11:
        return 10
    return n + f(n-1)

print(f(2204) - f(2202))