with open('9_3.csv') as f:
    count = 0
    for line in f:
        l = sorted(list(map(int, line.split())))

        uniq = [el for el in l if l.count(el) == 1]
        not_uniq = [el for el in l if l.count(el) > 1]

        if len(set(l)) == 4 and sorted(not_uniq)[2] < sum(l)/len(l):
            count += 1
    print(count)
