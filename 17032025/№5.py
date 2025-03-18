
for N in range(100, 1000):
    a, b = int(str(N)[0]) + int(str(N)[1]), int(str(N)[1]) + int(str(N)[2])
    if a < b:
        P = str(b) + str(a)
    else:
        P = str(a) + str(b)
    if P == '159':
        print(N)
        break