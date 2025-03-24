f = open('17.txt')

minimum = 10**10
max_sum = -10**10
counter = 0
v = []
for s in f:
    num = int(s)
    if num % 21 == 0:
        minimum = min(minimum, num)
    v.append(num)
for i in range(len(v)-1):
    if v[i] % minimum == 0 or v[i+1] % minimum == 0:
        counter += 1
        max_sum = max(v[i] + v[i+1], max_sum)

print(counter, max_sum)