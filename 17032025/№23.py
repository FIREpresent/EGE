vec = open("24.txt").readline().replace('A', 'A.').replace('B', 'B.').split('.')
maximum = 0
for i in range(len(vec)-2):
    if (vec[i] + vec[i + 1] + vec[i + 2][:-1]).count('A') == 1 and (vec[i] + vec[i + 1] + vec[i + 2][:-1]).count('B') == 1:
        maximum = max(maximum, len(vec[i] + vec[i + 1] + vec[i + 2][:-1]))
print(maximum)