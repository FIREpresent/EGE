f = open('17-1.txt')
arr = []
minimum = 10**10
for line in f.readlines():
    num = int(line.strip())
    arr.append(num)

count = 0
for i in range(1, len(arr)):
    if arr[i] > arr[i-1]:
        count += 1
        minimum = min(minimum, abs(arr[i] - arr[i-1]))

print(count, minimum)
