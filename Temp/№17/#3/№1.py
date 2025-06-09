
v = [int(elem) for elem in open('17-3 (2).txt')]
counter = 0
max_sum = -10**10

mini = min(v)

for i in range(len(v)-1):
    a = v[i]
    b = v[i+1]
    if a % 16 == mini or b % 16 == mini:
        counter += 1
        max_sum = max(max_sum, a+b)

print(counter, max_sum)
