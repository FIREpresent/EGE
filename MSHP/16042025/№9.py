with open('9.csv') as f:
    count = 0
    for line in f:
        l = list(map(int, line.split()))

        uniq = [el for el in l if l.count(el) == 1]
        not_uniq_3 = [el for el in l if l.count(el) == 3]
        not_uniq = [el for el in l if l.count(el) > 1]

        if len(set(not_uniq_3)) == 1 and len(uniq) == 4 and sum(uniq)/len(uniq) <= not_uniq_3[0]:
            count += 1

print(count)