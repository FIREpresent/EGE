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

def check(arr):
    l = []
    for elem in arr:
        if elem % 2 == 0:
            l.append(elem)
    if len(l) == 4:
        return l
    return [0]

vec = []

for i in range(2943444, 2943530):
    if is_prime(i):
        print(i)


# print(*vec[1][1])