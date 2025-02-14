def func1(cor, min_d):
    count = 0
    for elem in cor:
        if elem % 5 == min_d:
            count += 1
    if count <= 1:
        return 1
    return 0

def func2(cor, max_d):
    count = 0
    for elem in cor:
        if elem % 7 == max_d:
            count += 1
    if count >= 2:
        return 1
    return 0

f = open('17_1.txt')
max_sum = 0
v = [int(line.strip()) for line in f.readlines()]
min_d = min(v)%5
max_d = max(v)%7
counter = 0
for i in range(len(v)-2):
    c = (v[i], v[i+1], v[i+2])
    if len(str(c[0])) == 4 or len(str(c[1])) == 4 or len(str(c[2])) == 4:
        if func1(c, min_d) and func2(c, max_d):
            max_sum = max(max_sum, sum(c))
            counter += 1

print(counter, max_sum)

