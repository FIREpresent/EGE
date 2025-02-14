with open('9_3.csv') as f:
    maximum = -10**10
    for line in f:
        l = sorted(list(map(int, line.split())))

        # uniq = [el for el in l if l.count(el) == 1]
        # not_uniq = [el for el in l if l.count(el) > 1]

        maximum = max(maximum, (l[0]**2 + l[1]**2)**0.5)
    print(maximum)
