count = 0
for s in open('9.csv'):
    s = sorted([int(i) for i in s.split()])
    if (6 * s[0]) < (s[1] + s[2] + s[3]):
        if (s[1] * s[2]) < (s[3] * s[0]):
            count += 1
print(count)