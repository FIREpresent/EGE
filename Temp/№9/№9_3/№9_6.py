with open('9-6.csv') as f:
    count = 0
    for line in f:
        l = list(map(int, line.split()))
        uniq = [el for el in l if l.count(el) == 1]
        not_uniq = [el for el in l if l.count(el) > 1]
        if min(l) in uniq and len(not_uniq) > 0 and max(l) + min(l) < sum(not_uniq):
            count += 1
    print(count)