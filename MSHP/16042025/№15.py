def f(n, m):
    return n % m == 0


for A in range(0, 10010):
    flag = 1
    for x in range(0, 400):
        for y in range(0, 400):
            k = (x + y <= 22) or (y <= x - 6) or (y >= A)
            if not (k):
                flag = 0
                break
    if flag:
        print(A)
