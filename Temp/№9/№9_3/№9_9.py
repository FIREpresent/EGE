with open('9-9.csv') as f:
    count = 0
    for line in f:
        l = list(map(int, line.split()))
        uniq = [el for el in l if l.count(el) == 1]
        not_uniq = list(set([el for el in l if l.count(el) > 1]))
        meme = [el for el in l if l.count(el) == 3]
        if len(meme) == 3 and len(not_uniq) == 1 and (3*not_uniq[0])**2 > sum(uniq)**2:
            count += 1

    print(count)