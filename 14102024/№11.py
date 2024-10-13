f = open('092.csv')
lines = f.readlines()
count = 0
for line in lines:
    line = list(map(int, line.strip().split(',')))
    if len(set(line)) == len(line) and max(line) < sum(line) - max(line):
        count += 1
f.close()
print(count)