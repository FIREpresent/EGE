def f(N):
    N = bin(N)[2:]
    N = N[::-1]
    return int(str(int(N)), 2)
for i in range(100, 0, -1):
    if f(i) == 13:
        print(i)
        break

