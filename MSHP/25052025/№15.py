def f(n, m):
    return n % m == 0


for A in range(0, 10_000):
    flag = 1
    for x in range(1, 300):
        for y in range(1, 300):
            k = (-2*y + 3*x < A) or (x > 20) or (y > 55)
            if not (k):
                flag = 0
                break
    if flag:
        print(A)
        break
