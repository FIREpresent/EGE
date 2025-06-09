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
    N_bin = func(N, 2)
    if N % 2 == 0:
        N_bin = '10' + N_bin + '1'
    else:
        N_bin = '1' + N_bin + '01'
    R = int(N_bin, 2)
    if R > 420:
        print(N)
        break
