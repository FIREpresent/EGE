with open('9-9.csv') as f:
    count = 0
    for line in f:
        l = list(map(int, line.split()))
        uniq = [el for el in l if l.count(el) == 1]
        not_uniq = [el for el in l if l.count(el) > 1]
        if max(l) < sum(l)-max(l) and len(not_uniq) == 2:
            count += 1

    print(count)