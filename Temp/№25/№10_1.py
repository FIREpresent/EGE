from fnmatch import fnmatch

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

vec1 = []
vec2 = []
for i in range(2, 10 ** 8 + 1):
    if fnmatch(str(i), '124*5*79'):
        del_ = div(i)
        k = [el for el in del_ if el % 2 != 0]
        if i % sum(k) == 0:
            print(i, sum(del_))

