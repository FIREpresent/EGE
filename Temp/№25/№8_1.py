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
count = 0
for i in range(65000, 10 ** 7):
    if fnmatch(str(i), '6*97*5?'):
        k = [el for el in div(i) if el % 2 == 0]
        if len(k) >= 4 and count != 7:
            count += 1
            print(i, sum(k))

