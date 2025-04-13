for N in range(1, 10_000):
    N_bin = bin(N)[2:]
    N_bin = N_bin[::-1]
    R = int(N_bin + N_bin[-1], 2)
    if R > 99:
        print(N)
        break
