f = open('24_59848.txt')
a = str(f.read())

s = '0123456789ABCDEFGHIJKLMN'
count = 0
maximum = -1
for i in range(len(a)):
    if a[i] in s:
        count += 1
        if maximum < count:
            maximum = count
    else:
        count = 0

f.close()
print(maximum)