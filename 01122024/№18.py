def func(array):
   k = 0
   for i in range(len(array)):
       if array[i] % 32 == 0:
           k += 1
   return k


f = open('69927.txt', 'r')
lines = f.readlines()
a = []

for line in lines:
    a.append(int(line.strip()))
maximum = -1
c = func(a)
count = 0
for i in range(len(a)-1):
    if (a[i] < 0 or a[i+1] < 0) and (a[i] + a[i+1] < c):
        count += 1
        if a[i] + a[i+1] > maximum:
            maximum = a[i] + a[i+1]
f.close()
print(count, maximum)