f = open('17.txt')
l = []
sum_o = 0
count = 0
maximum = -10**10
for line in f.readlines():
    a = int(line)
    if a < 0:
        sum_o += a
    l.append(a)

for i in range(len(l)-2):
    j = i + 1
    k = i + 2
    if max(l[i], l[j], l[k]) * min(l[i], l[j], l[k]) > sum_o:
        count += 1
        maximum = abs(max(maximum, l[i] + l[j] + l[k]))
print(count, maximum)