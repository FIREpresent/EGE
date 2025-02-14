f = open('9_1.csv')
lines_0 = f.readlines()
count = 0
v = []
for line in lines_0:
    line = line.strip().split(' ')
    v.append(line)

maximum = -10**10
for i in range(len(v)):
    for j in range(len(v[i])):
        v[i][j] = v[i][j].replace(',', '.')
        v[i][j] = float(v[i][j])
        maximum = max(v[i][j], maximum)

f.close()

b = open('9_1_1.csv')
lines = b.readlines()
vec = []
for line in lines:
    line = line.strip().split(' ')
    vec.append(line)

for i in range(len(vec)):
    for j in range(len(vec[i])):
        vec[i][j] = vec[i][j].replace(',', '.')
        vec[i][j] = float(vec[i][j])
s = 0
for i in range(len(vec)):
    s += sum(vec[i])

print(maximum - (s/(len(vec) * len(vec[0]))))
b.close()