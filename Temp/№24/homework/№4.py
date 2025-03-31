with open('24-4.txt') as f:
    alph = sorted('QWERTYUIOPASDFGHJKLZXCVBNM')
    count = 0
    for line in f.readlines():
        for a in alph:
            if f'Z{a}RO' in line:
                count += 1
                break
    print(count)