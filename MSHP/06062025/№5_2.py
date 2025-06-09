for N in range(100, 1000):
    N_str = str(N)
    a = int(N_str[0]) + int(N_str[1])
    b = int(N_str[1]) + int(N_str[2])
    if a > b:
        s = str(b) + str(a)
    else:
        s = str(a) + str(b)
    R = int(s)
    if R == 714:
        print(N)
        break