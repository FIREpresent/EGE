
def M(N):
    v = set()
    for d in range(2, int(N**0.5)+1):
        if N % d == 0:
            v = v | {d, N//d}
    return sorted(v)

for num in range(110_250_000, 110_300_001):
    vec = M(num)
    if len(vec) >= 2:
        k = vec[-2] + vec[-1]
        if k%10_000 == 1002:
            print(num)
