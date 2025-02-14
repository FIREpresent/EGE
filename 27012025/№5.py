for i in range(1, 10_000):
    num = bin(i)[2:]
    num = num + str(num.count('1') % 2)
    num = num + str(num.count('1') % 2)
    if int(num, 2) > 123:
        print(int(num, 2))
        break