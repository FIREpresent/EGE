f = open('26_demo.txt')
lines = f.readlines()
V = int((lines[0].split())[0])
del (lines[0])
l = len(lines)
lines = sorted([int(lines[i]) for i in range(l)])

s = 0
n = 0
for i in range(l):
    if s + lines[i] <= V:
        s += lines[i]
        n = i+1
    else:
        break

print(n)
res = 0
rest = V - s
for i in range(l):
    if lines[i] - lines[n - 1] <= rest:
        res = lines[i]
print(res)