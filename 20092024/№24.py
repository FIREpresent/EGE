f = open('241.txt')
line = f.readline()
line = line.replace('XZZY', ' ')
print(max(len(s) for s in line.split())+6)
