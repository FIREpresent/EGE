f = open('9_000.csv')
lines = f.readlines()
count = 0
v = []
for line in lines:
    line = line.strip().split(' ')
    v.append(line)

maximum = -10**10
for i in range(len(v)):
    for j in range(len(v[i])):
        v[i][j] = v[i][j].replace(',', '.')
        v[i][j] = float(v[i][j])
        maximum = max(v[i][j], maximum)
s = 0
for i in range(len(v)):
    s += sum(v[i])

print(maximum - (s/(len(v) * len(v[0]))))
f.close()