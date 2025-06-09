for N in range(1, 1_000_000_000):
    N_bin = bin(N)[2:]
    print(N_bin)

    count_1 = N_bin.count('1')
    count_0 = N_bin.count('0')

    print(count_1, count_0)

    count_1_bin = bin(count_1)[2:]
    count_0_bin = bin(count_0)[2:]

    print(count_1_bin, count_0_bin)

    R = int(count_1_bin + count_0_bin, 2)

    print(R)
    if R == 183:
        print(N)
        break