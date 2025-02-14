with open('9-7.csv') as f:
    count = 0
    for line in f:
        l = sorted(list(map(int, line.split())))
        uniq = [el for el in l if l.count(el) == 1]
        not_uniq = set([el for el in l if l.count(el) > 1])
        meme = [el for el in l if l.count(el) == 2]
        if len(meme) == 2 and l[3] + l[2] > 2*(l[1] + l[0]) and l[3] % l[0] != 0:
            count += 1
    print(count)