with open('9.csv') as f:
    count = 0
    for line in f.readlines():
        l = list(map(int, line.strip().split()))
        uniq = [el for el in l if l.count(el) == 1]
        not_uniq = [el for el in l if l.count(el) > 1]
        if len(uniq) == 1 and len(set(not_uniq)) == 2:
            if not_uniq.count(list(set(not_uniq))[0]) == 3 and not_uniq.count(list(set(not_uniq))[1]) == 3:
                if max(list(set(not_uniq))[0], list(set(not_uniq))[1]) > uniq[0]:
                    count += 1

    print(count)