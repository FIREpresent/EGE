with open('9-10.csv') as f:
    count = 0
    for line in f:
        l = list(map(int, line.split()))
        uniq = [el for el in l if l.count(el) == 1]
        not_uniq = [el for el in l if l.count(el) > 1]
        meme = set([el for el in l if l.count(el) >= 3])
        if len(meme) > 0 and len(uniq) > 0 and sum(not_uniq)/len(not_uniq) < sum(uniq)/len(uniq):
            count += 1

    print(count)