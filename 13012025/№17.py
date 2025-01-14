f = open('17.txt')

maximum = -1
v = []
counter = 0
max_sum = -10**10
for s in f:
    num = int(s)
    if abs(num)%10 == 3:
        maximum = max(maximum, num)
    v.append(num)

for i in range(len(v)-1):
    if (abs(v[i]) % 10 == 3 and abs(v[i + 1]) % 10 != 3) or (abs(v[i]) % 10 != 3 and abs(v[i + 1]) % 10 == 3):
        if (v[i]**2 + v[i+1]**2 >= maximum**2):
            counter += 1
            max_sum = max(max_sum, v[i]**2 + v[i+1]**2)

print(counter, max_sum)