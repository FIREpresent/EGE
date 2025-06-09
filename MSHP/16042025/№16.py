import sys
from sys import setrecursionlimit

def f(n):
    if n <= 5:
        return n
    elif n > 5 and n % 4 == 0:
        return n + f(n/2-1)
    elif n > 5 and n % 4 != 0:
        return n + f(n + 2)
v = []
for n in range(1000):
    try:
        if f(n):
            v.append(f(n))
    except:
        print('bruh')

print(max(v))
