with open('9.csv') as f:
    count = 0
    for line in f:
        l = list(map(int, line.split()))
        uniq = [el for el in l if l.count(el) == 1]
        not_uniq = [el for el in l if l.count(el) > 1]
        if len(not_uniq) == 2 and len(set(not_uniq)) == 1 and sum(uniq)/len(uniq) <= sum(not_uniq):
            count += 1

    print(count)