def f(n, m):
    return n % m == 0

for A in range(0, 1001):
    flag = 1
    for x in range(0, 100000):
        k = ((x & 35 != 0) or (x & 22 != 0)) <= ((x & 15 == 0) <= (x & A != 0))
        if not k:
            flag = 0
            break
    if flag:
        print(A)
        break
