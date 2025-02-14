with open('9-6.csv') as f:
    count = 0
    for line in f:
        l = list(map(int, line.split()))
        count += 1
        uniq = [el for el in l if l.count(el) == 1]
        not_uniq = [el for el in l if l.count(el) > 1]
        if len(uniq) == len(l)-2 and not_uniq[0] >= sum(uniq)/4:
            print(count)
            break