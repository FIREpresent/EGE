with open('9_3.csv') as f:
    count = 0
    for line in f:
        l = sorted(list(map(int, line.split())))

        # uniq = [el for el in l if l.count(el) == 1]
        # not_uniq = [el for el in l if l.count(el) > 1]

        if l[0]**2 + l[1]**2 == l[2]**2:
            count += 1
    print(count)
