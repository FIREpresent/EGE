import sys
sys.setrecursionlimit(10_000)

def F(n):
    if n < 3:
        return n
    return (n-1)*F(n-2)

print((F(2024) - F(2022)) / F(2020))