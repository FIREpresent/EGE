minimum = 10**10
for N in range(1, 1_000):
    new_N = bin(N)[2:]
    if N % 2 == 0:
        new_N += '01'
    else:
        new_N += '10'
    R = int(new_N, 2)
    if R > 102:
        minimum = min(R, minimum)

print(minimum)