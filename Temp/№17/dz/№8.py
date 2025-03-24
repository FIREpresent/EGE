def func(a, b, d):
    c = 0
    if len(str(a)) == 4:
        c+=1
    if len(str(b)) == 4:
        c+=1
    if len(str(d)) == 4:
        c+=1

    if c == 1:
        return 1
    return 0

f = open('17-6.txt')

maximum = -10**10
v = []
counter = 0
max_sum = -10**10
for s in f:
    num = int(s)
    if abs(num) % 100 == 15:
        maximum = max(maximum, num)
    v.append(num)

for i in range(len(v)-2):
    if func(abs(v[i]), abs(v[i+1]), abs(v[i+2])) and v[i] + v[i+1] + v[i+2] >= maximum:
        counter += 1
        max_sum = max(v[i] + v[i+1] + v[i+2], max_sum)

print(counter, max_sum)