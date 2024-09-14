f = open('24.txt')
a = str(f.read())

count = 0
maximum = -1
for i in range(len(a)-1):
    if (a[i] == 'a' and a[i+1] == 'd') or (a[i] == 'd' and a[i+1] == 'a'):
        if maximum < count+1:
            maximum = count+1
        count = 0
    else:
        count += 1

f.close()
print(maximum)