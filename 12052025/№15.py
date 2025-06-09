for A in range(0, 100_000):
    flag = 1
    for x in range(0, 400):
        for y in range(0, 400):
            k = (5 < y) or (x > 32) or (x + 2*y < A)
            if not k:
                flag = 0
                break
    if flag:
        print(A)
