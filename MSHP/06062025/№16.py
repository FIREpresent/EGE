import sys
sys.setrecursionlimit(500_000)

def f(n):
    if n < 1000:
        return 66
    return f(n-5)+100

print(f(180_000) - f(100_000))