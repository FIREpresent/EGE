f = open('17-1 (5).txt')

maximum = -10**10
counter = 0
v = []

k = 0
summ = 0
for s in f:
    num = int(s)
    k += 1
    summ += num
    v.append(num)

average = summ/k

for i in range(len(v)-1):
    j = i + 1
    if v[i] > average or v[j] > average:
        counter += 1
        maximum = max(maximum, v[i] + v[j])
print(counter, maximum)