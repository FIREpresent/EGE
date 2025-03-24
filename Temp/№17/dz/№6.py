f = open('17-4.txt')
arr = []
minimum = 10**10
for line in f.readlines():
    num = int(line.strip())
    arr.append(num)

count = 0
for i in range(len(arr)-2):
    a = arr[i]
    b = arr[i+1]
    c = arr[i+2]
    if a < b < c:
        count += 1
        minimum = min(minimum, c-a)

print(count, minimum)
