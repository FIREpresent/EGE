def div(x):
    l = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            l.add(i)
            l.add(x // i)
    vec = sorted(list(l))
    k = []
    for el in vec:
        if is_prime(el):
            k.append(el)
    if len(k) > 3:
        return sorted(list(l))
    return [0]

def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def check_progr(arr):
    d = arr[1] - arr[0]
    s = arr[0]
    if d <= 0:
        return False
    for i in range(1, len(arr)):
        s += d
        if s != arr[i]:
            return False
    return True

for i in range(100_000, 500_001):
    dels_ = div(i)
    if len(dels_) > 3 and check_progr(dels_):
        print(i, len(dels_) * (dels_[1]-dels_[0]))