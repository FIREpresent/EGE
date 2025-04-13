f = open('17.txt')
v = []
maximum = -10**10
min_sum = 10**10
for line in f.readlines():
    num = int(line.strip())
    if num % 111 == 0:
        maximum = max(num, maximum)
    v.append(int(line.strip()))

count = 0
for i in range(len(v)-1):
    a = v[i]
    b = v[i+1]
    if (a > maximum or b > maximum) and (a%10 == 7 or b%10 == 7):
        count += 1
        min_sum = min(min_sum, a+b)

print(count, min_sum)
