with open('24-1.txt') as f:
    s = f.readline()

    print(s[:100])
    for c in 'CDF':
        s = s.replace(c, '*')
    for c in 'AO':
        s = s.replace(c, '?')
    print(s[:100])

    for i in range(1, 1000):
        if '*?' * i in s:
            print(i)
        else:
            break
#replace, split

