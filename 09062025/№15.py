for A in range(0, 1000):
    flag = 1
    for x in range(0, 300):
        for y in range(0, 300):
            k = (x**2 <= 136) or (y < 4*x + A - 70) or (2*y > 51)
            if not k:
                flag = 0
    if flag:
        print(A)
        break