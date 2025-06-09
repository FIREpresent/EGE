f_usl = 1
for x in [k*0.25 for k in range(0, 40_000)]:
    A = 0
    C = 29 <= x <= 100
    D = 7 <= x <= 68
    f = D <= ((not(C) and not(A)) <= (not(D)))
    if f != f_usl:
        print(x)
