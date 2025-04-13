from fnmatch import fnmatch
def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

for i in range(0, 10**9 + 1, 2423):
    if fnmatch(str(i), '3*51?5*7') and is_prime(sum(list(map(int, list(str(i)))))):
        print(i, i // 2423)