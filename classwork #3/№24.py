f = open('24.txt')
s = f.readline()
mini = 10**10
count = 0
pos = []
for i in range(len(s)-1):
    if s[i] == 'T':
        pos.append(i)
for j in range(1, len(pos)-209):
    count = pos[j+209] - pos[j] + 1
    if count < mini:
        mini = count
print(mini)