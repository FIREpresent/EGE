def func(x, lines):
    count = 0
    good = 0
    if len(set(x)) == len(x):
        for k in range(6):
            for i in range(len(lines)):
                for j in range(6):
                    if x[k] == lines[i][j]:
                        count += 1
            if count - 1 == 45:
                good += 1
    return good


f = open('9.2.csv')

lines = [list(map(int,s.split(','))) for s in open('9.2.csv')]
res = 0
for line in lines:
    res += func(line, lines)

print(res)