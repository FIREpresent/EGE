
f = open('27881.txt')
lines = f.readlines()
based = int((lines[0].split())[0])
del(lines[0])
lines = sorted(map(int,lines))
s = 0
l = len(lines)
a = 0
res = 0
for i in range(l):
    if s + lines[i] > based:
        a = i
        print(a)
        break
    s += lines[i]

for i in range(l):
    if lines[i]-lines[a-1] <= based - s:
        res = lines[i]
print(res)