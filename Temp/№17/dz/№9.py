f = open('17-6.txt')

maximum = -10**10
v = []
counter = 0
max_sum = -10**10
for s in f:
    num = int(s)
    if abs(num) % 10 == 3 and 99 < num < 1000:
        maximum = max(maximum, num)
    v.append(num)
print(v)
for i in range(len(v)-2):
    a = abs(v[i])
    b = abs(v[i+1])
    c = abs(v[i+2])

    if (a % 10 == 3 and 99 < a < 1000 or b % 10 == 3 and 99 < b < 1000 or c % 10 == 3 and 99 < c < 1000) and v[i] + v[i+1] + v[i+2] < maximum:
        counter += 1
        max_sum = max(v[i] + v[i+1] + v[i+2], max_sum)

print(counter, max_sum)