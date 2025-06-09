for N in range(0, 1_000):
    N_bin = bin(N)[2:]
    if N_bin.count('1') % 2 == 0:
        N_bin = '10' + N_bin[2:] + '0'
    else:
        N_bin = '11' + N_bin[2:] + '1'
    R = int(N_bin, 2)
    if R > 480:
        print(N)
        break