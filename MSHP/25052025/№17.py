f = open('17.txt')

minimum = 10**10
max_i = -10**10
counter = 0
v = []

for s in f:
    num = int(s)
    if abs(num) % 100 == 40:
        minimum = min(minimum, num)
    v.append(num)

for i in range(len(v)-2):
    j = i + 1
    k = i + 2
    t = [v[i], v[j], v[k]]
    if len(set(t)) == 2 and v[i] > minimum and v[j] > minimum and v[k] > minimum:
        counter += 1
        if t.count(v[i]) == 1:
            max_i = max(max_i, i+1)
        elif t.count(v[j]) == 1:
            max_i = max(max_i, j+1)
        elif t.count(v[k]) == 1:
            max_i = max(max_i, k + 1)

print(counter, max_i)