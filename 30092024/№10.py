def func(x):
    if len(set(x)) == len(x) and (sum(x) - x[0] - x[5])/4 < (x[0] + x[5])/2:
        return 1
    return 0


f = open('9.1.csv')

lines = f.readlines()
count = 0
for line in lines:
    count += func(sorted(list(map(int, line.strip().split(',')))))

print(count)
