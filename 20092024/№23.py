f = open('24.txt')
line = f.readline()


line = line.replace('A', '0')
line = line.replace('B', '0')
line = line.replace('C', '0')

lines = []

l = 0
for i in range(len(line)-1):
    if line[i] == '0' and line[i+1] == '0':
        l += 1
        lines.append(l)
        l = 0
    else:
        l += 1
lines.append(l)

print(max(lines))