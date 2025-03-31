for N in range(10_000, 100_000):
    N_str = str(N)
    a, b = str(int(N_str[0]) + int(N_str[2]) + int(N_str[4])), str(int(N_str[1]) + int(N_str[3]))
    if int(a) > int(b):
        R = int(b+a)
    else:
        R = int(a+b)

    if R == 723:
        print(N)
        break