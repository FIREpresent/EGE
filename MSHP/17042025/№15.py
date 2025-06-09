def f(n, m):
    return n % m == 0


for A in range(1, 10010):
    flag = 1
    for x in range(1, 400):
            k = (f(x, 175) <= (not(f(x, 25)))) or (2*x + A >= 1780)
            if not (k):
                flag = 0
                break
    if flag:
        print(A)
        break
