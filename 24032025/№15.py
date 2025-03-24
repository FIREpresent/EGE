for A in range(0, 1_000):
    flag = True
    for n in range(0, 300):
        for m in range(0, 300):
            k = (3*m + 4*n > 66) or (m <= A) or (n < A)
            if not k:
                flag = False
                break
        if not flag:
            break
    if flag:
        print(A)
        break
