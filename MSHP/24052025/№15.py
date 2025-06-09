def f(n, m):
    return n % m == 0


for A in range(0, 10010):
    flag = 1
    for x in range(0, 300):
        for y in range(0, 300):
            k = (11 <= y) or (7*y < x) or (A > x*y)
            if not (k):
                flag = 0
                break
    if flag:
        print(A)
        break
