f = open('17.txt')
lines = f.readlines()
maximum = -1
count = 0
for i in range(len(lines)-1):
    for j in range(i+1, len(lines)):
        if (int(lines[i]) * int(lines[j])) % 10 == 0:
            maximum = max(maximum, int(lines[i]) + int(lines[j]))
            count += 1
print(count, maximum)