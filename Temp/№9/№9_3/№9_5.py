with open('9-5.csv') as f:
    count = 0
    for line in f:
        a = sorted(list(map(int, line.split())))

        # uniq = [el for el in l if l.count(el) == 1]
        # not_uniq = [el for el in l if l.count(el) > 1]
        if a[0] + a[2] == a[1] + a[3]:
            count += 1
    print(count)