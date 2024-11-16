
for A in range(0, 1001):

    flag = True
    for x in range(0, 11000):
        y = ((x & 45 > 0) or (x & 89 > 0)) <= (x & A > 0)
        if not y:
            flag = False
            break

    if flag:
        print(A)
        break