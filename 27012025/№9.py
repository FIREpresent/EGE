with open('9.csv') as f:
    count = 0
    for line in f:
        l = sorted(list(map(int, line.split())))
        if l[0] + l[1] > l[2]:
            count += 1
    print(count)