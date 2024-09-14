def func(x):
    N = bin(x)[2:]
    K = sum(list(map(int, str(N))))
    N1 = N + str(int(K) % 2)
    K1 = sum(list(map(int, str(N1))))
    N2 = N1 + str(int(K1) % 2)
    return int(N2, 2)

a = []
for i in range(1, 1000):
    if func(i) < 100:
        a.append(func(i))

print(max(a))