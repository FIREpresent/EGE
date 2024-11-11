for N in range(9999999,1,-1):
    R = bin(N)[2:]

    if N % 5 == 0:
        R += bin(5)[2:]
    else:
        R += '1'

    if int(R, 2) % 7 == 0:
        R += bin(7)[2:]
    else:
        R += '1'

    if int(R, 2) < 1728404:
        print(N)
        break

