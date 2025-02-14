with open('9-7.csv') as f:
    count = 0
    for line in f:
        l = list(map(int, line.split()))
        count += 1
        uniq = [el for el in l if l.count(el) == 1]
        not_uniq = set([el for el in l if l.count(el) > 1])
        if len(uniq) == len(l)-4 and max(l) not in not_uniq:
            print(sum(l))
            break