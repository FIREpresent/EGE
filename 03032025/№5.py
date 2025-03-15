vec = []
for N in range(1, 100_000):
    N_bin = bin(N)[2:]
    N_bin += str(sum(list(map(int, list(N_bin)))) % 2)
    N_bin += str(sum(list(map(int, list(N_bin)))) % 2)
    P = int(N_bin, 2)
    if P > 93:
        vec.append(P)

print(min(vec))