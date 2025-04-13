with open('9.csv', 'r') as f:
    count = 0
    for line in f.readlines():
        v = sorted(list(map(int, line.strip().split(' '))))
        if v[3] - v[0] >= 50 and v[2] * v[1] <= 1000:
            count += 1

    print(count)
