with open('9_4.csv') as f:
    count = 0
    for line in f:
        l = list(map(int, line.split()))

        # uniq = [el for el in l if l.count(el) == 1]
        # not_uniq = [el for el in l if l.count(el) > 1]
        a = l[0]
        b = l[1]
        c = l[2]
        if b**2 - 4*a*c < 0:
            count += 1
    print(count)