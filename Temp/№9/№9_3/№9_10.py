with open('9-10.csv') as f:
    count = 0
    for line in f:
        l = list(map(int, line.split()))
        uniq = [el for el in l if l.count(el) == 1]
        not_uniq = [el for el in l if l.count(el) > 1]
        meme = set([el for el in l if l.count(el) >= 3])
        if len(not_uniq) == 0 and 2*sum(1 for el in l if el % 2 == 0) < len(l) and sum([el for el in l if el % 2 == 0]) > sum([el for el in l if el % 2 != 0]):
            count += 1

    print(count)