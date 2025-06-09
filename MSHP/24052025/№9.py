with open('9-1 (6).csv') as f:
    count = 0
    for line in f:
        l = list(map(int, line.split()))

        uniq = [el for el in l if l.count(el) == 1]
        not_uniq_2 = sorted([el for el in l if l.count(el) == 2])
        not_uniq = [el for el in l if l.count(el) > 1]

        if len(not_uniq) > 0 and max(l) in uniq and sum(not_uniq) < max(l):
            count += 1

print(count)