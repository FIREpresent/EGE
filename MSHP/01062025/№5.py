for N in range(999, 99, -1):
    N_str = str(N)
    a = int(N_str[0]) * int(N_str[1])
    b = int(N_str[1]) * int(N_str[2])
    if a > b:
        k = str(b) + str(a)
    else:
        k = str(a) + str(b)
    if k == '621':
        print(N)
        break