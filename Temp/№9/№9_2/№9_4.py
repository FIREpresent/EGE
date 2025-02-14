with open('9-114.csv') as f:
    count = 0
    for line in f:
        l = sorted(list(map(int, line.split())))

        # uniq = [el for el in l if l.count(el) == 1]
        # not_uniq = [el for el in l if l.count(el) > 1]
        a = l[0]
        b = l[1]
        c = l[2]
        func = (c**2 - a**2 - b**2)/(-2*a*b)
        if func > 0 and a+b>c:
            count += 1
    print(count)