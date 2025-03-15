with open('9-1_1.csv') as f:
    count = 0
    for line in f:
        l = list(map(int, line.split()))

        uniq = [el for el in l if l.count(el) == 1]
        not_uniq = [el for el in l if l.count(el) > 1]
        chet = [el for el in l if el % 2 == 0]
        not_chet = [el for el in l if el % 2 != 0]

        if len(not_uniq) > 0 and len(not_chet) != 3 or len(not_uniq) == 0 and len(not_chet) == 3:
            count += 1
    print(count)