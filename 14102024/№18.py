for A in range(0, 1001):
    flag = 1
    for x in range(0, 300):
        for y in range(0, 300):
            k = (x < A) or (y < A) or (x + 2*y > 50)
            if not k:
                flag = 0
                break
    if flag:
        print(A)
