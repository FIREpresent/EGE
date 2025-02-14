with open('9-107.csv') as f:
    count = 0
    for line in f:
        l = sorted(list(map(int, line.split())))

        # uniq = [el for el in l if l.count(el) == 1]
        # not_uniq = [el for el in l if l.count(el) > 1]

        if l[0]+l[1]+l[2] == 180 and l[2] > 90:
            count += 1
    print(count)