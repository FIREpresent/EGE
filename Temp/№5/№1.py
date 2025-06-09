def f(n):
    s = ''
    while n:
        s += str(n%3)
        n //= 3
    return s[::-1]

for N in range(3, 100_000):
    N_tr = f(N)
    if N % 3 == 0:
        N_tr = N_tr + N_tr[-2:]
    else:
        N_tr = N_tr + f(N%3*3)
    R = int(N_tr, 3)
    if R <= 150:
        print(N)
