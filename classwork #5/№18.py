import sys
sys.setrecursionlimit(10_000)

def f(n):
    if n < 7:
        return 7
    else:
        return 2*n + f(n-1)

print(f(2024)-f(2022))