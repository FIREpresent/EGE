for x in [k*0.25 for k in range(0, 40_000)]:
    A = 0
    B = 23 <= x <= 37
    C = 41 <= x <= 73
    f = not(((not(B)) <= C) <= A)
    if f != 0:
        print(x)

