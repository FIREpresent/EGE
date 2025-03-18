f = open('17.txt')
v = []
counter = 0
max_sum = -10**10
for s in f:
    num = int(s)
    v.append(num)

for i in range(len(v)):
    for j in range(i, len(v)):
        if i != j:
            if abs(v[i] - v[j]) % 60 == 0 and (abs(v[i]) % 15 == 0 or abs(v[j]) % 15 == 0):
                counter += 1
                max_sum = max(max_sum, v[i] - v[j])

print(counter, max_sum)