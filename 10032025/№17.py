def func(a, b, d):
    c = 0
    if len(str(a)) == 5:
        c+=1
    if len(str(b)) == 5:
        c+=1
    if len(str(d)) == 5:
        c+=1

    if c==2:
        return 1
    return 0

def func1(a, b, d):
    if a % 5 == 0 or d % 5 == 0 or b % 5 == 0:
        return 1
    return 0

f = open('17.txt')

maximum = -1
v = []
counter = 0
max_sum = -10**10
for s in f:
    num = int(s)
    if num % 1000 == 321:
        maximum = max(maximum, num)
    v.append(num)

for i in range(len(v)-2):
    if func(v[i], v[i+1], v[i+2]) and func1(v[i], v[i+1], v[i+2]) and v[i] + v[i+1] + v[i+2] > maximum:
        counter += 1
        max_sum = max(v[i] + v[i+1] + v[i+2], max_sum)

print(counter, max_sum)