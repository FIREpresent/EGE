f = open('17-2.txt')
arr = []
minimum = 10**10
for line in f.readlines():
    num = int(line.strip())
    arr.append(num)
    minimum = min(num, minimum)

count = 0
index = 0
for i in range(len(arr)):
    if arr[i] == minimum:
        count += 1
        index = i
print(count, index+1)
