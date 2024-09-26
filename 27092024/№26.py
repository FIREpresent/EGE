f = open('24.txt')
line = f.readline()
v = line.split('D')[1:-1]
maximum = 0
c = 1
for i in range(len(v)):
    if v[i].count('O') <= 2:
        c += len(v[i]) + 1
        if maximum < c:
            maximum = c
    else:
        c = 1
print(maximum)



