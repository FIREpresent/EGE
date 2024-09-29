f = open('24.txt')
line = f.readline()

line = line.replace('D', 'C')
line = line.replace('F', 'C')
line = line.replace('O', 'A')

line = line.replace('CCA', '#')
line = line.replace('C', ',')
line = line.replace('A', ',')

line = line.split(',')

print(max(len(s) for s in line))

