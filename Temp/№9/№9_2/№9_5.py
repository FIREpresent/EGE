with open('9-123.csv') as f:
    count = 0
    for line in f:
        l = sorted(list(map(int, line.split())))

        # uniq = [el for el in l if l.count(el) == 1]
        # not_uniq = [el for el in l if l.count(el) > 1]

        meme = [el for el in l if el > 180]

        if l[0]+l[1]+l[2]+l[3] == 360 and len(meme) == 0:
            count += 1
    print(count)