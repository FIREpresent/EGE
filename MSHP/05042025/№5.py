def func(x, base):
    v = []
    while x:
        v.append(str(x % base))
        x = x // base
    s = ''
    v = v[::-1]
    for i in range(len(v)):
        s = s + v[i]
    return s

for N in range(1, 10_000):
    N_bin = func(N, 3)
    N_bin = '1' + N_bin + '00' if N % 2 == 0 else N_bin + func(sum(list(map(int, list(N_bin)))),3)
    R = int(N_bin + N_bin[-1], 3)
    if R > 168:
        print(N)
        break
