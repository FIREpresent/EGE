def f(x, base):
    alph = '0123456789QWERTYUIOPASDFGHJKLZXCVBNM'
    alph = sorted(alph)[:base]
    s = ''
    while x:
        s += alph[x%base]
        x //= base
    return s[::-1]

for N in range(1, 1000_000):
    N_7 = f(N, 7)
    k = sum(list(map(int, list(N_7))))
    if k % 2 == 0:
        N_7 = N_7 + '555'
    else:
        N_7 = '33' + N_7 + '6'
    R = int(N_7, 7)
    if R < 12717:
        print(N)
