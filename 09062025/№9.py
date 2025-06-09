def func(arr):
    counter_chet = 0
    counter_nechet = 0
    for elem in arr:
        if elem % 2 == 0:
            counter_chet += 1
        else:
            counter_nechet += 1
    return counter_chet == counter_nechet

summ = 0
with open('9_22547.csv') as f:
    for line in f.readlines():
        v = list(map(int, line.split()))
        if v[0] < v[1] < v[2] < v[3] < v[4] < v[5] and func(v) == 1:
            summ = sum(v)

print(summ)