def func(x):
    v = []
    for i in range(7):
        count = 0
        for j in range(7):
            if x[i] == x[j]:
                count += 1
        v.append(count)
    summ1, summ2 = 0, 0
    if v.count(2) == 4 and len(set(x)) == 5:
        for i in range(7):
            if v[i] == 1:
                summ1 += x[i]
            elif v[i] == 2:
                summ2 += x[i]
    if summ1/3 > summ2/4:
        return 1
    return 0

f = open('9.csv')
lines = f.readlines()
res = 0
for n in range(len(lines)):
    res += func(list(map(int, (lines[n].strip()).split(','))))
f.close()
print(res)

