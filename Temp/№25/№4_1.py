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

vec = []

for i in range(118811, 118973):
    dels_ = div(i)
    if len(dels_) == 6:
        vec.append((i, dels_))

print(*vec[2][1])