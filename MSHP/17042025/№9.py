with open('9.csv') as f:
    count = 0
    for line in f:
        l = list(map(int, line.split()))

        uniq = [el for el in l if l.count(el) == 1]
        not_uniq_2 = sorted([el for el in l if l.count(el) == 2])
        not_uniq = [el for el in l if l.count(el) > 1]

        if len(set(not_uniq_2)) == 2 and not_uniq_2[0] < uniq[0] < not_uniq_2[2]:
            count += 1

print(count)