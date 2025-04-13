from fnmatch import *

def div(x):
    l = set()
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            l.add(i)
            l.add(x // i)
    return sorted(list(l))

def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

for i in range(1020201, 10**10 + 1):
    k = div(i)
    if fnmatch(str(i), '1?2*0*2?1') and len(k) == 3:
        print(i, k[1])

