v = []
for N in range(1, 100_000):
    N_bin = bin(N)[2:]
    N_bin = N_bin + bin(N_bin.count('1') % 2)[2:]
    R = N_bin + bin(N_bin.count('1') % 2)[2:]
    if int(R, 2) > 123:
        v.append(int(R, 2))

print(min(v))