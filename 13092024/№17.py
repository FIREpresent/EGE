def min_5(array):
    arr = []
    for i in range(len(array)):
        if array[i] % 10 == 5:
            arr.append(array[i])
    return min(arr)**2

f = open('17.txt', 'r')
lines = f.readlines()
a = []

for line in lines:
    a.append(int(line.strip()))
maximum = -1
c = min_5(a)
count = 0
for i in range(len(a)-1):
    if min(a[i], a[i+1]) % 10 == 5 and a[i]**2 + a[i+1]**2 < c:
        count += 1
        if a[i]**2 + a[i+1]**2 > maximum:
            maximum = a[i]**2 + a[i+1]**2
f.close()
print(count, maximum)