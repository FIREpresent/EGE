with open('9-1.csv') as f:
    count = 0
    for line in f:
        b = 1
        l = list(map(int, line.split()))
        l2 = [elem for elem in l if elem != max(l) and elem != min(l)]
        for elem in l2:
            b *= elem
        if (max(l) * min(l)) ** 2 > 3*b:
            count += 1

print(count)