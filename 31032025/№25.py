def div(x):
    l = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            l.add(i)
            l.add(x // i)
    return sorted(list(l))

for i in range(123456789, 223456789):
    k = div(i)
    if len(k) == 3:
        print(i, k[-1])
