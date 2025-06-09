a = [int(elem) for elem in open('17-1 (7).txt')]
min_sum = 10**10
counter = 0
for elem in a:
    summ = 0
    s = str(elem)
    for i in s:
        summ += int(i)
    # summ = sum(list(map(int, list(str(elem)))))
    min_sum = min(summ, min_sum)

v = []
for elem in a:
    summ = 0
    s = str(elem)
    for i in s:
        summ += int(i)
    if summ == min_sum:
        v.append(elem)

max_el = max(v)
maximum = -10**10

for i in range(len(a)-1):
    if a[i] > max_el and a[i+1] > max_el:
        counter += 1
        maximum = max(maximum, sum(list(map(int, list(str(a[i]))))) + sum(list(map(int, list(str(a[i+1]))))))
print(counter, maximum)

