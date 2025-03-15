def f(n, m):
    return n % m == 0


for A in range(0, 1001):
    flag = 1
    for x in range(0, 400):
        for y in range(0, 400):
            k = (3 * x + 4 * y != 60) or ((A >= x) and (A >= y))
            if not (k):
                flag = 0
                break
    if flag:
        print(A)
        break
