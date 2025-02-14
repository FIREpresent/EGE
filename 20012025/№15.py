for A in range(0, 1001):
    flag = 1
    for x in range(0, 300):
        for y in range(0, 300):
            k = (x - 3 * y < A) or (y > 400) or (x > 56)
            if not k:
                flag = 0
                break
    if flag:
        print(A)
        break
