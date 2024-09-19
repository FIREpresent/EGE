f = open('24.txt')
line = f.readline()
line = line.replace('Q', '0')
line = line.replace('R', '0')
line = line.replace('S', '0')
line = line.replace('00', '0 ')

print(line)

print(max(len(s) for s in line.split())+1)