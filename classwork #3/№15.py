

for A in range(0, 1001):

    flag = True
    for x in range(1, 11000):
        y = (x & 25 != 0) <= ((x & 17 == 0) <= (x & A != 0))
        if not y:
            flag = False
            break

    if flag:
        print(A)
        break