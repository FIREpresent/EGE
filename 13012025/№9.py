f = open('107_9.csv')

counter = 0
for s in f:
    flag = True
    a = sorted(list(map(int, s.strip().split(','))))
    if a[0] + a[1] < a[2] or a[0] + a[1] < a[3] or a[1] + a[2] < a[3]:
        counter += 1

print(counter)