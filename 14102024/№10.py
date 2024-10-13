def func1(arr):
    c = 0
    for x in arr:
        if x % 2 == 0:
            c += 1
    if c > 2:
        return 1
    return 0

def func2(arr):
    sum1 = 0
    sum2 = 0
    for x in arr:
        if x % 2 == 0:
            sum1 += x
        else:
            sum2 += x

    return sum1 < sum2

f = open('091.csv')
lines = f.readlines()
count = 0
for line in lines:
    line = list(map(int, line.strip().split(',')))
    if len(set(line)) == len(line) and func1(line) and func2(line):
        count += 1
f.close()
print(count)
