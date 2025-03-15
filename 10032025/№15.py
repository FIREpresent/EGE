counter = 0
for A in range(10_000, 0, -1):
    flag = True
    for x in range(1, 100_000):
        k = (120 % A == 0) and ((x % A != 0) <= ((x % 18 == 0) <= (x % 24 != 0)))
        if not(k):
            flag = False
            break
    if flag:
        print(A)
        break

