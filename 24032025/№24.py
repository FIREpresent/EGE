def func(x):
    dels = []
    for d in range(2, x//2+1):
        if x % d == 0:
            dels.append(d)
    if len(dels) == 3:
        return 1, max(dels)
    return 0, -10**10

for n in range(289123456, 389123457):
    a, b = func(n)
    if a:
        print(n, b)