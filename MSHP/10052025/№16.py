import sys
from sys import setrecursionlimit
def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def f(n):
    if n == 0:
        return 1
    elif n > 0:
        return 7*(n-1)+f(n-1)

count = 0
for n in range(2, 201):
    try:
        if f(n):
            if is_prime(f(n)):
                count += 1
    except:
        print('bruh')

print(count)
