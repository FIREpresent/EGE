for A in range(0, 1001):
    flag = 1
    for x in range(0, 300):
        for y in range(0, 300):
            k = (x * y < A) or (x < y) or (x >= 12)
            if not k:
                flag = 0
                break
    if flag:
        print(A)
        break
