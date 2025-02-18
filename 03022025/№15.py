for A in range(0, 100_000):
    flag = 1
    for x in range(0, 400):
        for y in range(0, 400):
            k = (y + 2*x != 48) or (A < x) or (A < y)
            if not k:
                flag = 0
                break
    if flag:
        print(A)
