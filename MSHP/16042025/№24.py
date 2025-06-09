count = 0
with open('24.txt') as f:
    for line in f.readlines():
        if line.count('K') > line.count('U'):
            count += 1
print(count)