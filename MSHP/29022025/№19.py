v = []
for i in range(1, 10_000):
    num = list(bin(i)[2:])

    if num.count('1') % 2 == 0:
        num.append('0')
        num[0] = '1'
        num[1] = '0'
    else:
        num.append('1')
        num[0] = '1'
        num[1] = '1'
    s = ''.join([x for x in num])

    if int(s, 2) > 40:
        print(int(s, 2))
        break
