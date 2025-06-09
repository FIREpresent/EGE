import sys
sys.setrecursionlimit(100_000)

def f(n):
    if n > 80_000:
        return 100
    return f(n + 1) * n

print((f(50)/100 + f(53))/f(55))