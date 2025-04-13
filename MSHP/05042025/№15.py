for A in range(0, 1001):
    flag = 1
    for x in range(0, 10_000):
            k = (x & 25 != 0) <= ((x & 17 == 0) <= (x & A != 0))
            if not k:
                flag = 0
                break
    if flag:
        print(A)
        break
