count = 0
for N in range(1, 100_000):
    N_bin = bin(N)[2:]
    if N % 2 == 0:
        N_bin += bin(sum(list(map(int, list(N_bin)))))[2:]
    else:
        N_bin = '1' + N_bin + '00'
    R = int(N_bin, 2)
    if 500 <= R <= 700:
        count += 1
    print(R)
print(count)