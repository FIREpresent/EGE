

f = open('17.txt', 'r')
lines = f.readlines()
a = []
count = 0
maximum = -1
maximum_triple = -1

for line in lines:
    a.append(int(line.strip()))

for i in range(len(a)):
    if str(a[i])[-2:] == '19' and a[i] > maximum:
        maximum = a[i]


for i in range(len(a)-2):
    j = i+1
    k = i+2
    if (len(str(a[i])) == 4 and len(str(a[j])) == 4 and len(str(a[k])) != 4) or (len(str(a[i])) == 4 and len(str(a[k])) == 4 and len(str(a[j])) != 4) or (len(str(a[j])) == 4 and len(str(a[k])) == 4 and len(str(a[i])) != 4):
        if (a[i] % 3 == 0) or (a[j] % 3 == 0) or (a[k] % 3 == 0):
            if (a[i] + a[j] + a[k]) > maximum:
               count += 1
               maximum_triple = max(maximum_triple, a[i]+a[j]+a[k])

print(count, maximum_triple)




