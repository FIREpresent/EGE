with open('9-1.csv') as f:
    count = 0
    for line in f:
        l = list(map(int, line.split()))
        count += 1
        uniq = [el for el in l if l.count(el) == 1]
        not_uniq = [el for el in l if 3 > l.count(el) > 1]
        not_uniq1 = [el for el in l if l.count(el) > 1]
        if len(set(not_uniq)) and len(uniq) == 3 and max(l) in uniq:
            print(sum(l))
            break